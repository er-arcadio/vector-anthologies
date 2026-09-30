#!/usr/bin/env python3
"""
Build the encrypted board payload for the private Kanban tab.

Reads board/ (tickets, user stories, project charter, decisions, audits),
serialises it to JSON, and encrypts it with AES-256-GCM using a key derived
from a passphrase via PBKDF2-HMAC-SHA256. The browser decrypts it with
WebCrypto after the author types the passphrase.

The passphrase comes from the BOARD_PASSPHRASE environment variable (a
GitHub Actions secret in CI). With no passphrase set, this module reports
that it is unconfigured and the site build omits the board tab entirely --
it never emits the board in plaintext.

Usage:
    BOARD_PASSPHRASE='...' python3 scripts/build_board.py --out _site
"""

import argparse
import base64
import json
import os
import re
import secrets
import sys
from pathlib import Path

PBKDF2_ITERATIONS = 310_000
KEY_LEN = 32
SALT_LEN = 16
IV_LEN = 12
MIN_PASSPHRASE_LEN = 12

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?\n)---\s*\n?(.*)$", re.DOTALL)

COLUMNS = [
    {"id": "backlog", "label": "Backlog"},
    {"id": "ready", "label": "Ready"},
    {"id": "in_progress", "label": "In progress"},
    {"id": "in_review", "label": "In review"},
    {"id": "awaiting_author", "label": "Needs you"},
    {"id": "done", "label": "Done"},
]


def parse_md(path: Path):
    """Parse flat key: value frontmatter plus ## sections. No YAML dependency."""
    text = path.read_text(encoding="utf-8")
    m = FRONTMATTER_RE.match(text)
    meta, body = {}, text
    if m:
        body = m.group(2)
        for line in m.group(1).splitlines():
            if ":" in line and not line.startswith(("#", " ", "\t", "-")):
                k, v = line.split(":", 1)
                meta[k.strip()] = re.sub(r"\s+#.*$", "", v).strip()
    sections, intro, cur = {}, [], None
    for line in body.splitlines():
        h = re.match(r"^##\s+(.*)$", line)
        if h:
            cur = h.group(1).strip()
            sections[cur] = []
        elif cur:
            sections[cur].append(line)
        else:
            intro.append(line)
    return meta, "\n".join(intro).strip(), {k: "\n".join(v).strip() for k, v in sections.items()}


def read_dir(board: Path, sub: str):
    out = []
    d = board / sub
    if not d.exists():
        return out
    for f in sorted(d.glob("*.md")):
        meta, intro, sections = parse_md(f)
        if meta.get("id"):
            meta["intro"] = intro
            meta["sections"] = sections
            out.append(meta)
    return out


def read_text(board: Path, name: str) -> str:
    p = board / name
    return p.read_text(encoding="utf-8") if p.exists() else ""


def collect_board(board: Path) -> dict:
    tickets = read_dir(board, "tickets")
    for t in tickets:
        t["blocked_by"] = [x for x in re.split(r"[,\s]+", t.get("blocked_by", "") or "") if x]
    by_id = {t["id"]: t for t in tickets}
    for t in tickets:
        t["blocked"] = any(by_id.get(b, {}).get("status") not in (None, "done") for b in t["blocked_by"])

    stories = read_dir(board, "stories")
    for s in stories:
        own = [t for t in tickets if t.get("story") == s["id"]]
        s["ticketIds"] = [t["id"] for t in own]
        s["ticketsTotal"] = len(own)
        s["ticketsDone"] = sum(1 for t in own if t.get("status") == "done")

    audits = []
    adir = board / "audit"
    if adir.exists():
        for f in sorted(adir.glob("*.md")):
            audits.append({"name": f.name, "text": f.read_text(encoding="utf-8")})

    return {
        "columns": COLUMNS,
        "tickets": tickets,
        "stories": stories,
        "project": read_text(board, "PROJECT.md"),
        "decisions": read_text(board, "DECISIONS.md"),
        "audits": audits,
    }


def encrypt(payload: dict, passphrase: str) -> dict:
    try:
        from cryptography.hazmat.primitives.ciphers.aead import AESGCM
    except ImportError:
        print("  ! board: the 'cryptography' package is required to encrypt the board payload.\n"
              "    Install it (pip install -r scripts/requirements.txt) or the board tab is skipped.",
              file=sys.stderr)
        return {}
    import hashlib

    salt = secrets.token_bytes(SALT_LEN)
    iv = secrets.token_bytes(IV_LEN)
    key = hashlib.pbkdf2_hmac("sha256", passphrase.encode("utf-8"), salt, PBKDF2_ITERATIONS, KEY_LEN)
    data = json.dumps(payload, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    ct = AESGCM(key).encrypt(iv, data, None)
    b64 = lambda b: base64.b64encode(b).decode("ascii")
    return {"v": 1, "kdf": "PBKDF2-SHA256", "iterations": PBKDF2_ITERATIONS,
            "salt": b64(salt), "iv": b64(iv), "ct": b64(ct)}


def get_passphrase():
    """Return (passphrase, reason_if_unavailable)."""
    pw = os.environ.get("BOARD_PASSPHRASE", "")
    if not pw:
        return None, "BOARD_PASSPHRASE is not set"
    if len(pw) < MIN_PASSPHRASE_LEN:
        return None, (f"BOARD_PASSPHRASE is shorter than {MIN_PASSPHRASE_LEN} characters. "
                      "The encrypted payload is public, so a short passphrase is brute-forceable offline")
    return pw, None


def build_board(repo_root: Path, out_dir: Path) -> bool:
    """Write the encrypted payload. Returns True if the board tab should be included."""
    pw, reason = get_passphrase()
    if not pw:
        print(f"  · board tab skipped: {reason}.")
        return False
    board = repo_root / "board"
    if not board.exists():
        print("  · board tab skipped: no board/ directory.")
        return False
    payload = collect_board(board)
    blob = encrypt(payload, pw)
    if not blob:
        return False
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "board-data.json").write_text(json.dumps(blob), encoding="utf-8")
    print(f"  · board tab built: {len(payload['tickets'])} ticket(s), "
          f"{len(payload['stories'])} user story(ies), encrypted "
          f"({len(json.dumps(blob))} bytes).")
    return True


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", default="_site")
    ap.add_argument("--repo-root", default=".")
    a = ap.parse_args()
    ok = build_board(Path(a.repo_root).resolve(), Path(a.out).resolve())
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()


# ------------------------------------------------------------ board page --

BOARD_CSS = """
.board-wrap { max-width: 1180px; margin: 0 auto; padding: 22px 16px 80px; }
.lock-card { max-width: 380px; margin: 60px auto; background: var(--surface);
  border: 1px solid var(--border); border-radius: 14px; padding: 26px; box-shadow: var(--shadow); }
.lock-card h1 { font-size: 1.15rem; margin: 0 0 4px; }
.lock-card p { color: var(--text-secondary); font-size: 0.88rem; margin: 0 0 16px; }
.lock-card input { width: 100%; padding: 10px 12px; font-size: 16px; border-radius: 8px;
  border: 1px solid var(--border); background: var(--bg); color: var(--text); }
.lock-card button { margin-top: 12px; width: 100%; padding: 10px; border: 0; border-radius: 8px;
  background: var(--accent); color: var(--accent-contrast); font-size: 0.95rem; font-weight: 600; cursor: pointer; }
.lock-card button:disabled { opacity: 0.6; cursor: default; }
.lock-err { color: #b4531a; font-size: 0.86rem; margin-top: 12px; }
@media (prefers-color-scheme: dark) { .lock-err { color: #f0a066; } }

.board-bar { display: flex; align-items: center; gap: 8px; flex-wrap: wrap; margin-bottom: 16px; }
.board-tabs { display: flex; gap: 4px; }
.btab { border: 0; background: none; color: var(--text-secondary); padding: 6px 12px;
  border-radius: 8px; cursor: pointer; font-size: 0.9rem; font-family: inherit; }
.btab[aria-selected="true"] { background: var(--surface); color: var(--text); font-weight: 700;
  border: 1px solid var(--border); }
.board-bar .spacer { flex: 1; }
.board-bar select, .board-bar button.ghost { background: var(--surface); color: var(--text);
  border: 1px solid var(--border); border-radius: 8px; padding: 6px 10px; font-size: 0.85rem;
  font-family: inherit; cursor: pointer; }

.needs-you { background: color-mix(in srgb, var(--accent) 14%, transparent);
  border: 1px solid var(--accent); border-radius: 10px; padding: 10px 14px; margin-bottom: 14px;
  font-size: 0.9rem; cursor: pointer; }
.needs-you strong { color: var(--accent-strong); }
@media (prefers-color-scheme: dark) { .needs-you strong { color: var(--accent-strong); } }

.kanban { display: grid; grid-auto-flow: column; grid-auto-columns: minmax(190px, 1fr);
  gap: 10px; overflow-x: auto; padding-bottom: 10px; align-items: start; }
.kcol { background: color-mix(in srgb, var(--text) 5%, transparent); border-radius: 12px; padding: 10px; min-height: 90px; }
.kcol.flagged { outline: 2px solid var(--accent); }
.kcol h2 { font-size: 0.68rem; text-transform: uppercase; letter-spacing: 0.07em;
  color: var(--text-secondary); margin: 2px 4px 10px; display: flex; justify-content: space-between; }
.kcard { background: var(--surface); border: 1px solid var(--border); border-radius: 9px;
  padding: 10px 12px; margin-bottom: 8px; cursor: pointer; text-align: left; width: 100%;
  font: inherit; color: inherit; display: block; }
.kcard:hover { border-color: var(--accent); }
.kcard .kid { font-size: 0.72rem; color: var(--text-secondary); }
.kcard .ktitle { font-weight: 650; margin: 2px 0 7px; font-size: 0.92rem; line-height: 1.35; }
.chips { display: flex; gap: 5px; flex-wrap: wrap; }
.chip { font-size: 0.7rem; padding: 1px 8px; border-radius: 999px; color: var(--text-secondary);
  border: 1px solid var(--border); }
.chip.hot { color: var(--accent); border-color: var(--accent); }
.chip.gate { background: color-mix(in srgb, var(--accent) 16%, transparent); color: var(--accent-strong); border-color: transparent; }

.usgroup { margin-bottom: 24px; }
.usgroup > h2 { font-size: 1rem; margin: 0 0 10px; }
.uscard { background: var(--surface); border: 1px solid var(--border); border-radius: 12px;
  padding: 14px 16px; margin-bottom: 10px; }
.uscard .ustop { display: flex; gap: 9px; align-items: baseline; flex-wrap: wrap; }
.uscard .ustop b { font-size: 0.98rem; }
.progress { height: 6px; border-radius: 4px; background: color-mix(in srgb, var(--text) 10%, transparent);
  margin: 10px 0 6px; overflow: hidden; }
.progress i { display: block; height: 100%; background: var(--accent); }
.asa { color: var(--text-secondary); margin: 6px 0; font-size: 0.9rem; }
.checks { list-style: none; padding: 0; margin: 6px 0 10px; font-size: 0.87rem; }
.doc { background: var(--surface); border: 1px solid var(--border); border-radius: 12px; padding: 16px 18px; }
.doc pre { white-space: pre-wrap; font: inherit; margin: 0; }
.audit-pick { margin-bottom: 12px; }

dialog.tdlg { border: 1px solid var(--border); border-radius: 14px; background: var(--surface);
  color: var(--text); width: min(700px, 94vw); padding: 0; }
dialog.tdlg::backdrop { background: rgba(0,0,0,0.5); }
.tdlg .dh { display: flex; justify-content: space-between; gap: 12px; padding: 15px 18px;
  border-bottom: 1px solid var(--border); align-items: flex-start; }
.tdlg .dh h3 { margin: 0; font-size: 1.02rem; }
.tdlg .dbody { padding: 6px 18px 20px; overflow: auto; max-height: 68vh; }
.tdlg h4 { font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.07em;
  color: var(--text-secondary); margin: 15px 0 4px; }
.tdlg ul { list-style: none; padding: 0; margin: 0; font-size: 0.9rem; }
.tdlg li { margin: 3px 0; }
.board-foot { color: var(--text-secondary); font-size: 0.75rem; margin-top: 18px; }
@media (max-width: 680px) { .kanban { grid-auto-flow: row; grid-auto-columns: auto; } }
"""

BOARD_JS = r"""
(function () {
  var DATA = null, view = 'kanban', epicFilter = '', auditIdx = 0;
  var $ = function (s) { return document.querySelector(s); };
  function el(t, c, txt) { var e = document.createElement(t); if (c) e.className = c; if (txt != null) e.textContent = txt; return e; }
  function chip(t, c) { return el('span', 'chip' + (c ? ' ' + c : ''), t); }
  function b64(s) { var raw = atob(s), a = new Uint8Array(raw.length); for (var i = 0; i < raw.length; i++) a[i] = raw.charCodeAt(i); return a; }

  async function unlock(passphrase, blob) {
    var enc = new TextEncoder();
    var base = await crypto.subtle.importKey('raw', enc.encode(passphrase), 'PBKDF2', false, ['deriveKey']);
    var key = await crypto.subtle.deriveKey(
      { name: 'PBKDF2', salt: b64(blob.salt), iterations: blob.iterations, hash: 'SHA-256' },
      base, { name: 'AES-GCM', length: 256 }, false, ['decrypt']);
    var plain = await crypto.subtle.decrypt({ name: 'AES-GCM', iv: b64(blob.iv) }, key, b64(blob.ct));
    return JSON.parse(new TextDecoder().decode(plain));
  }

  function bullets(parent, text) {
    if (!text) return;
    var ul = el('ul');
    text.split('\n').forEach(function (raw) {
      var line = raw.trim(); if (!line) return;
      var box = line.match(/^-\s+\[( |x|X)\]\s+(.*)$/), bl = line.match(/^[-*]\s+(.*)$/);
      var li = el('li');
      if (box) li.textContent = (box[1] === ' ' ? '☐ ' : '☑ ') + box[2];
      else if (bl) li.textContent = '• ' + bl[1];
      else li.textContent = line;
      ul.appendChild(li);
    });
    parent.appendChild(ul);
  }

  function openTicket(t) {
    $('#dlgTitle').textContent = t.id + '  ' + t.title;
    var b = $('#dlgBody'); b.textContent = '';
    var row = el('div', 'chips');
    [String(t.status || '').replace(/_/g, ' '), t.assignee, t.priority,
     (t.gate && t.gate !== 'none') ? 'Gate ' + t.gate : '', t.story, t.estimate]
      .forEach(function (x) { if (x) row.appendChild(chip(x)); });
    if (t.blocked) row.appendChild(chip('blocked', 'hot'));
    b.appendChild(row);
    if (t.blocked_by && t.blocked_by.length) {
      var p = el('p', null, 'Blocked by ' + t.blocked_by.join(', ')); p.style.fontSize = '0.87rem'; b.appendChild(p);
    }
    ['Decision needed', 'Goal', 'Inputs', 'Outputs', 'Definition of done', 'Work log', 'Decision log']
      .forEach(function (k) {
        var v = t.sections && t.sections[k]; if (!v) return;
        b.appendChild(el('h4', null, k)); bullets(b, v);
      });
    $('#tdlg').showModal();
  }

  function applyFilter(arr) { return epicFilter ? arr.filter(function (x) { return x.epic === epicFilter; }) : arr; }

  function renderKanban(root) {
    var grid = el('div', 'kanban');
    DATA.columns.forEach(function (col) {
      var items = applyFilter(DATA.tickets).filter(function (t) { return t.status === col.id; });
      var c = el('div', 'kcol' + (col.id === 'awaiting_author' && items.length ? ' flagged' : ''));
      var h = el('h2'); h.appendChild(el('span', null, col.label)); h.appendChild(el('span', null, String(items.length)));
      c.appendChild(h);
      items.forEach(function (t) {
        var card = el('button', 'kcard'); card.type = 'button';
        card.appendChild(el('div', 'kid', t.id + (t.epic ? '  ·  ' + t.epic : '')));
        card.appendChild(el('div', 'ktitle', t.title));
        var ch = el('div', 'chips');
        if (t.assignee) ch.appendChild(chip(t.assignee));
        if (t.priority === 'high') ch.appendChild(chip('high', 'hot'));
        if (t.gate && t.gate !== 'none') ch.appendChild(chip('Gate ' + t.gate, 'gate'));
        if (t.blocked) ch.appendChild(chip('blocked', 'hot'));
        card.appendChild(ch);
        card.addEventListener('click', function () { openTicket(t); });
        c.appendChild(card);
      });
      grid.appendChild(c);
    });
    root.appendChild(grid);
  }

  function renderStories(root) {
    var list = applyFilter(DATA.stories);
    if (!list.length) { root.appendChild(el('p', 'asa', 'No user stories yet.')); return; }
    var groups = {};
    list.forEach(function (s) { var k = s.epic || 'No epic'; (groups[k] = groups[k] || []).push(s); });
    Object.keys(groups).forEach(function (k) {
      var g = el('div', 'usgroup'); g.appendChild(el('h2', null, k));
      groups[k].forEach(function (s) {
        var card = el('div', 'uscard'), top = el('div', 'ustop');
        top.appendChild(el('span', 'kid', s.id));
        top.appendChild(el('b', null, s.title));
        top.appendChild(chip(String(s.status || '').replace(/_/g, ' ')));
        if (s.priority === 'high') top.appendChild(chip('high', 'hot'));
        card.appendChild(top);
        var total = Number(s.ticketsTotal) || 0, done = Number(s.ticketsDone) || 0;
        var bar = el('div', 'progress'), fill = el('i');
        fill.style.width = (total ? Math.round(100 * done / total) : 0) + '%';
        bar.appendChild(fill); card.appendChild(bar);
        card.appendChild(el('div', 'kid', done + ' of ' + total + ' tickets done'));
        if (s.intro) card.appendChild(el('p', 'asa', s.intro.replace(/\*\*/g, '')));
        if (s.sections && s.sections['Acceptance criteria']) {
          var holder = el('div'); bullets(holder, s.sections['Acceptance criteria']);
          var ul = holder.firstChild; if (ul) { ul.className = 'checks'; card.appendChild(ul); }
        }
        var chips = el('div', 'chips');
        (s.ticketIds || []).forEach(function (id) {
          var t = DATA.tickets.filter(function (x) { return x.id === id; })[0]; if (!t) return;
          var btn = el('button', 'chip'); btn.type = 'button';
          btn.textContent = id + ' · ' + String(t.status || '').replace(/_/g, ' ');
          btn.style.cursor = 'pointer';
          btn.addEventListener('click', function () { openTicket(t); });
          chips.appendChild(btn);
        });
        card.appendChild(chips);
        g.appendChild(card);
      });
      root.appendChild(g);
    });
  }

  function renderDoc(root, title, text) {
    var d = el('div', 'doc'); d.appendChild(el('h2', null, title));
    var pre = el('pre'); pre.textContent = text || 'Nothing recorded yet.'; d.appendChild(pre);
    root.appendChild(d);
  }

  function renderAudits(root) {
    var list = DATA.audits || [];
    if (!list.length) { root.appendChild(el('p', 'asa', 'No audit reports yet.')); return; }
    var sel = el('select', 'audit-pick');
    list.forEach(function (a, i) { var o = el('option', null, a.name); o.value = String(i); sel.appendChild(o); });
    sel.value = String(auditIdx);
    sel.addEventListener('change', function () { auditIdx = Number(sel.value); render(); });
    root.appendChild(sel);
    renderDoc(root, list[auditIdx].name, list[auditIdx].text);
  }

  function render() {
    var root = $('#boardView'); root.textContent = '';
    if (view === 'kanban') renderKanban(root);
    else if (view === 'stories') renderStories(root);
    else if (view === 'project') { renderDoc(root, 'Project charter', DATA.project); renderDoc(root, 'Decision log', DATA.decisions); }
    else renderAudits(root);

    var needs = DATA.tickets.filter(function (t) { return t.status === 'awaiting_author'; });
    var banner = $('#needsYou');
    if (needs.length) {
      banner.style.display = 'block'; banner.textContent = '';
      banner.appendChild(el('strong', null, needs.length + (needs.length > 1 ? ' items need you: ' : ' item needs you: ')));
      banner.appendChild(document.createTextNode(needs.map(function (t) { return t.id + ' ' + t.title; }).join('  ·  ')));
      banner.onclick = function () { openTicket(needs[0]); };
    } else { banner.style.display = 'none'; }
  }

  function fillEpics() {
    var sel = $('#epicFilter'); sel.textContent = '';
    var all = el('option', null, 'All epics'); all.value = ''; sel.appendChild(all);
    var seen = {};
    DATA.tickets.concat(DATA.stories).forEach(function (x) {
      if (x.epic && !seen[x.epic]) { seen[x.epic] = 1; var o = el('option', null, x.epic); o.value = x.epic; sel.appendChild(o); }
    });
    sel.value = epicFilter;
  }

  function show(data) {
    DATA = data;
    $('#lockScreen').style.display = 'none';
    $('#boardApp').style.display = 'block';
    fillEpics(); render();
  }

  var blobPromise = fetch('board-data.json', { cache: 'no-store' }).then(function (r) {
    if (!r.ok) throw new Error('board-data.json not found'); return r.json();
  });

  document.addEventListener('DOMContentLoaded', function () {
    var form = $('#lockForm'), input = $('#pw'), err = $('#lockErr'), btn = $('#lockBtn');

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      err.textContent = ''; btn.disabled = true; btn.textContent = 'Unlocking…';
      blobPromise.then(function (blob) { return unlock(input.value, blob); })
        .then(function (data) {
          try { sessionStorage.setItem('va_board_pw', input.value); } catch (_) {}
          show(data);
        })
        .catch(function (ex) {
          err.textContent = /not found/.test(String(ex && ex.message))
            ? 'The board data file is missing from this build.'
            : 'That passphrase did not work.';
          btn.disabled = false; btn.textContent = 'Unlock';
          input.select();
        });
    });

    document.querySelectorAll('.btab').forEach(function (b) {
      b.addEventListener('click', function () {
        view = b.getAttribute('data-view');
        document.querySelectorAll('.btab').forEach(function (x) {
          x.setAttribute('aria-selected', x === b ? 'true' : 'false');
        });
        if (DATA) render();
      });
    });
    $('#epicFilter').addEventListener('change', function (e) { epicFilter = e.target.value; render(); });
    $('#lockBtn2').addEventListener('click', function () {
      try { sessionStorage.removeItem('va_board_pw'); } catch (_) {}
      location.reload();
    });
    $('#dlgClose').addEventListener('click', function () { $('#tdlg').close(); });

    var saved = null;
    try { saved = sessionStorage.getItem('va_board_pw'); } catch (_) {}
    if (saved) {
      blobPromise.then(function (blob) { return unlock(saved, blob); })
        .then(show)
        .catch(function () { try { sessionStorage.removeItem('va_board_pw'); } catch (_) {} });
    }
  });
})();
"""


def render_board_page(page_shell, base_css_marker=None) -> str:
    body = """
<div class="board-wrap">

  <div id="lockScreen">
    <form class="lock-card" id="lockForm" autocomplete="off">
      <h1>Editorial board</h1>
      <p>Private project board. Enter the passphrase to decrypt it in your browser.</p>
      <input type="password" id="pw" placeholder="Passphrase" aria-label="Passphrase" autofocus required>
      <button type="submit" id="lockBtn">Unlock</button>
      <div class="lock-err" id="lockErr" role="alert"></div>
    </form>
  </div>

  <div id="boardApp" style="display:none">
    <div class="board-bar">
      <div class="board-tabs" role="tablist">
        <button class="btab" type="button" role="tab" data-view="kanban" aria-selected="true">Kanban</button>
        <button class="btab" type="button" role="tab" data-view="stories" aria-selected="false">User stories</button>
        <button class="btab" type="button" role="tab" data-view="project" aria-selected="false">Project</button>
        <button class="btab" type="button" role="tab" data-view="audits" aria-selected="false">Audits</button>
      </div>
      <span class="spacer"></span>
      <select id="epicFilter" aria-label="Filter by epic"></select>
      <button class="ghost" type="button" id="lockBtn2">Lock</button>
    </div>
    <div class="needs-you" id="needsYou" style="display:none"></div>
    <div id="boardView"></div>
    <p class="board-foot">Decrypted in your browser. Nothing is sent anywhere.</p>
  </div>

  <dialog class="tdlg" id="tdlg">
    <div class="dh"><h3 id="dlgTitle"></h3><button class="ghost" type="button" id="dlgClose">Close</button></div>
    <div class="dbody" id="dlgBody"></div>
  </dialog>
</div>
"""
    head = ('<meta name="robots" content="noindex, nofollow">\n<style>'
            + BOARD_CSS + '</style>\n<script>' + BOARD_JS + '</script>')
    return page_shell("Editorial board", body, head)
