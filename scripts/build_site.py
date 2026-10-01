#!/usr/bin/env python3
"""
Build the Vector Anthologies reading site (GitHub Pages) from stories/*.md.

Scans stories/**/*.md, parses YAML frontmatter, renders each story to its
own HTML page, and generates a timeline-feed index.html linking out to
them. Designed to run standalone locally or inside GitHub Actions
(.github/workflows/pages.yml) on every push to main.

Usage:
    python3 scripts/build_site.py [--out _site] [--repo-root .]
"""

import argparse
import html
import os
import re
import sys
from datetime import datetime
from pathlib import Path

import markdown
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_board  # noqa: E402  (needs sys.path set above)

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?\n)---\s*\n?(.*)$", re.DOTALL)

SITE_TITLE = "Vector Anthologies"
SITE_TAGLINE = "Stories from the Vector universe, as they're written."

# --------------------------------------------------------- publish policy --
#
# What reaches the public reading site, and in what order.
#
# PUBLISH_POLICY
#   "all"      publish every story (the original behaviour, and the default)
#   "approved" publish only stories that are neither canon_status: draft
#              nor eval_status: flagged
#
# A story can always override the policy with `publish: true` / `publish: false`
# in its own frontmatter. An explicit `publish:` value always wins.
#
# ORDER_MODE
#   "date"     newest first by the `date` written (the original behaviour)
#   "reading"  by each story's `order:` frontmatter, ascending, so the feed can
#              be read front to back; stories without `order:` fall to the end,
#              newest first among themselves.
#
# Both can be overridden per build: --publish-policy / --order, or the
# PUBLISH_POLICY / ORDER_MODE environment variables.

PUBLISH_POLICY = os.environ.get("PUBLISH_POLICY", "all")
ORDER_MODE = os.environ.get("ORDER_MODE", "date")

UNAPPROVED_CANON = {"draft"}
UNAPPROVED_EVAL = {"flagged"}


# ---------------------------------------------------------------- parsing --

def parse_story_file(path: Path, stories_root: Path):
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)
    if not match:
        print(f"  ! skipping {path} — no YAML frontmatter found", file=sys.stderr)
        return None

    raw_frontmatter, body_md = match.group(1), match.group(2)
    try:
        meta = yaml.safe_load(raw_frontmatter) or {}
    except yaml.YAMLError as exc:
        print(f"  ! skipping {path} — bad frontmatter: {exc}", file=sys.stderr)
        return None

    title = str(meta.get("title") or path.stem.replace("-", " ").title())
    tags = meta.get("tags") or []
    if isinstance(tags, str):
        tags = [tags]
    canon_status = str(meta.get("canon_status") or "draft")
    eval_status = str(meta.get("eval_status") or "unreviewed")

    publish_raw = meta.get("publish")
    if isinstance(publish_raw, bool):
        publish_override = publish_raw
    elif isinstance(publish_raw, str) and publish_raw.strip().lower() in ("true", "yes", "false", "no"):
        publish_override = publish_raw.strip().lower() in ("true", "yes")
    else:
        publish_override = None

    order_raw = meta.get("order")
    try:
        order_key = int(order_raw) if order_raw is not None else None
    except (TypeError, ValueError):
        print(f"  ! {path} has a non-numeric 'order' ({order_raw!r}) — ignoring it", file=sys.stderr)
        order_key = None

    date_raw = meta.get("date")
    date_obj = None
    if date_raw is not None:
        # YAML already parses bare ISO dates (YYYY-MM-DD) into datetime.date.
        if isinstance(date_raw, datetime):
            date_obj = date_raw.date()
        elif hasattr(date_raw, "isoformat") and not isinstance(date_raw, str):
            date_obj = date_raw
        else:
            for fmt in ("%Y-%m-%d", "%Y/%m/%d", "%B %d, %Y"):
                try:
                    date_obj = datetime.strptime(str(date_raw), fmt).date()
                    break
                except ValueError:
                    continue
    if date_obj is None:
        print(f"  ! {path} has no usable 'date' in frontmatter — "
              f"it will sort last and show 'date unknown'", file=sys.stderr)

    rel = path.relative_to(stories_root)
    parts = rel.parts[:-1]  # directory components, excluding the filename

    if parts and parts[0] == "vector":
        category = "Vector"
        arc_label = None
        for part in parts[1:]:
            m = re.match(r"arc-0*(\d+)", part)
            if m:
                arc_label = f"Arc {int(m.group(1))}"
                break
        subtitle = arc_label or "Vector"
    elif parts and parts[0] == "anthology":
        category = "Anthology"
        subtitle = parts[1].replace("-", " ").title() if len(parts) > 1 else "Anthology"
    else:
        category = "Story"
        subtitle = category

    slug = "-".join(rel.with_suffix("").parts)
    slug = re.sub(r"[^a-zA-Z0-9\-]+", "-", slug).strip("-").lower()

    body_html = markdown.markdown(body_md, extensions=["extra", "sane_lists"])
    excerpt = make_excerpt(body_html)

    return {
        "title": title,
        "tags": [str(t) for t in tags],
        "canon_status": canon_status,
        "eval_status": eval_status,
        "publish_override": publish_override,
        "order_key": order_key,
        "date_obj": date_obj,
        "date_display": date_obj.strftime("%b %-d, %Y") if date_obj else "Date unknown",
        "date_sort_key": date_obj or datetime.min.date(),
        "category": category,
        "subtitle": subtitle,
        "slug": slug,
        "body_html": body_html,
        "excerpt": excerpt,
        "source_path": str(rel),
    }


def make_excerpt(body_html: str, max_len: int = 220) -> str:
    text = re.sub(r"<[^>]+>", " ", body_html)
    text = re.sub(r"\s+", " ", text).strip()
    text = re.sub(r"\s+([.,!?;:])", r"\1", text)
    if len(text) <= max_len:
        return text
    cut = text[:max_len].rsplit(" ", 1)[0]
    return cut + "…"


def should_publish(story, policy: str):
    """(publish?, reason). An explicit `publish:` in frontmatter always wins."""
    if story["publish_override"] is True:
        return True, "publish: true"
    if story["publish_override"] is False:
        return False, "publish: false in frontmatter"
    if policy == "approved":
        if story["canon_status"].lower() in UNAPPROVED_CANON:
            return False, f'canon_status: {story["canon_status"]}'
        if story["eval_status"].lower() in UNAPPROVED_EVAL:
            return False, f'eval_status: {story["eval_status"]}'
    return True, ""


def sort_stories(stories, order_mode: str):
    """date: newest first. reading: by `order:` ascending, unordered last."""
    if order_mode == "reading":
        # (0, order) sorts before (1, ...), so ordered stories lead; unordered
        # keep newest-first among themselves via the negated ordinal.
        return sorted(
            stories,
            key=lambda s: (
                (0, s["order_key"], 0)
                if s["order_key"] is not None
                else (1, 0, -s["date_sort_key"].toordinal())
            ),
        )
    return sorted(stories, key=lambda s: s["date_sort_key"], reverse=True)


def collect_stories(stories_root: Path, policy: str = None, order_mode: str = None):
    policy = policy or PUBLISH_POLICY
    order_mode = order_mode or ORDER_MODE
    stories, withheld = [], []
    if not stories_root.exists():
        return stories
    for path in sorted(stories_root.rglob("*.md")):
        if path.name.upper() == "CLAUDE.MD":
            continue
        # Sidecar files that live next to a story but are not stories:
        # <story-slug>.board-review.md, and anything else *.<kind>-review.md
        if path.name.lower().endswith("-review.md"):
            continue
        story = parse_story_file(path, stories_root)
        if not story:
            continue
        ok, reason = should_publish(story, policy)
        if ok:
            stories.append(story)
        else:
            withheld.append((story, reason))

    if withheld:
        print(f"  · {len(withheld)} story(ies) withheld from the public site "
              f"(policy: {policy}):")
        for s, reason in withheld:
            print(f"      - {s['title']}  ({s['source_path']})  — {reason}")

    return sort_stories(stories, order_mode)


# --------------------------------------------------------------- template --

BASE_CSS = """
:root {
  --bg: #F5F6F7;
  --surface: #FFFFFF;
  --text: #110705;
  --text-secondary: #5B6062;
  --border: #E2E4E5;
  --accent: #895327;
  --accent-strong: #421F02;
  --accent-contrast: #F5F6F7;
  --timeline-line: #D9C9BC;
  --badge-canon: #895327;
  --badge-draft: #71797B;
  --badge-noncanon: #9A9FA1;
  --shadow: 0 1px 2px rgba(17, 7, 5, 0.06), 0 1px 1px rgba(17, 7, 5, 0.04);
}

@media (prefers-color-scheme: dark) {
  :root {
    --bg: #150C0A;
    --surface: #1E1310;
    --text: #F5F6F7;
    --text-secondary: #A9AEB0;
    --border: #34241D;
    --accent: #C98A4B;
    --accent-strong: #E0A469;
    --accent-contrast: #150C0A;
    --timeline-line: #4A362B;
    --badge-canon: #C98A4B;
    --badge-draft: #8E9599;
    --badge-noncanon: #6B7072;
    --shadow: 0 1px 2px rgba(0, 0, 0, 0.4), 0 1px 1px rgba(0, 0, 0, 0.3);
  }
}

* { box-sizing: border-box; }

html, body {
  margin: 0;
  padding: 0;
  background: var(--bg);
  color: var(--text);
}

body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  line-height: 1.5;
  -webkit-font-smoothing: antialiased;
}

a { color: var(--accent); text-decoration: none; }
a:hover { text-decoration: underline; }

.topbar {
  position: sticky;
  top: 0;
  z-index: 10;
  background: var(--accent-strong);
  color: var(--accent-contrast);
  padding: 14px 20px;
  display: flex;
  align-items: baseline;
  gap: 10px;
  box-shadow: var(--shadow);
}

.topbar a.brand {
  color: var(--accent-contrast);
  font-weight: 800;
  font-size: 1.05rem;
  letter-spacing: 0.02em;
  text-decoration: none;
}

.topbar .tagline {
  color: var(--accent-contrast);
  opacity: 0.75;
  font-size: 0.85rem;
}

.wrap {
  max-width: 700px;
  margin: 0 auto;
  padding: 28px 16px 80px;
}

.feed {
  position: relative;
  padding-left: 26px;
}

.feed::before {
  content: "";
  position: absolute;
  left: 6px;
  top: 6px;
  bottom: 6px;
  width: 2px;
  background: var(--timeline-line);
}

.entry {
  position: relative;
  margin-bottom: 22px;
}

.entry::before {
  content: "";
  position: absolute;
  left: -25px;
  top: 22px;
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: var(--accent);
  border: 2px solid var(--bg);
  box-shadow: 0 0 0 2px var(--timeline-line);
}

.card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 14px;
  padding: 16px 18px;
  box-shadow: var(--shadow);
  transition: border-color 0.15s ease;
}

.card:hover {
  border-color: var(--accent);
}

.meta-row {
  display: flex;
  align-items: center;
  gap: 8px;
  flex-wrap: wrap;
  font-size: 0.8rem;
  color: var(--text-secondary);
  margin-bottom: 6px;
}

.badge {
  display: inline-block;
  padding: 2px 9px;
  border-radius: 999px;
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.02em;
  text-transform: uppercase;
  color: var(--accent-contrast);
  background: var(--badge-draft);
}

.badge.canon { background: var(--badge-canon); }
.badge.non-canon { background: var(--badge-noncanon); }

.category-pill {
  display: inline-block;
  padding: 2px 9px;
  border-radius: 999px;
  font-size: 0.72rem;
  font-weight: 600;
  border: 1px solid var(--border);
  color: var(--text-secondary);
}

.date {
  color: var(--text-secondary);
}

.card h2 {
  margin: 4px 0 6px;
  font-size: 1.2rem;
  line-height: 1.3;
}

.card h2 a { color: var(--text); }
.card h2 a:hover { color: var(--accent); text-decoration: none; }

.excerpt {
  color: var(--text-secondary);
  font-size: 0.95rem;
  margin: 0 0 10px;
}

.tags {
  display: flex;
  gap: 6px;
  flex-wrap: wrap;
  margin-bottom: 10px;
}

.tag {
  font-size: 0.72rem;
  color: var(--accent);
  background: color-mix(in srgb, var(--accent) 12%, transparent);
  padding: 2px 8px;
  border-radius: 999px;
}

.read-link {
  font-size: 0.88rem;
  font-weight: 600;
}

.empty-state {
  text-align: center;
  padding: 60px 20px;
  color: var(--text-secondary);
}

.empty-state h2 {
  color: var(--text);
  margin-bottom: 8px;
}

/* Story page */
.story-header {
  margin-bottom: 24px;
}

.back-link {
  display: inline-block;
  margin-bottom: 18px;
  font-size: 0.9rem;
  font-weight: 600;
}

.story-header h1 {
  font-size: 1.9rem;
  line-height: 1.25;
  margin: 6px 0 10px;
}

.story-body {
  font-family: Georgia, "Iowan Old Style", "Times New Roman", serif;
  font-size: 1.08rem;
  line-height: 1.75;
}

.story-body p { margin: 0 0 1.1em; }
.story-body h1, .story-body h2, .story-body h3 {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  margin-top: 1.6em;
}
.story-body blockquote {
  border-left: 3px solid var(--accent);
  margin: 1.2em 0;
  padding-left: 14px;
  color: var(--text-secondary);
}

footer.site-footer {
  max-width: 700px;
  margin: 0 auto;
  padding: 20px 16px 60px;
  color: var(--text-secondary);
  font-size: 0.8rem;
  text-align: center;
}
"""


BOARD_ENABLED = False


def page_shell(title: str, body: str, extra_head: str = "") -> str:
    board_link = (
        '<span style="margin-left:auto"><a href="{}board.html" '
        'style="color:var(--accent-contrast);opacity:.85;font-size:.85rem;font-weight:600">Board</a></span>'
        .format("" if title in (SITE_TITLE, "Editorial board") else "../")
    ) if BOARD_ENABLED else ""
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(SITE_TAGLINE)}">
<style>{BASE_CSS}</style>
{extra_head}
</head>
<body>
<div class="topbar">
  <a class="brand" href="index.html">{html.escape(SITE_TITLE)}</a>
  <span class="tagline">{html.escape(SITE_TAGLINE)}</span>
  {board_link}
</div>
{body}
<footer class="site-footer">{html.escape(SITE_TITLE)} — updated automatically as new stories are added.</footer>
</body>
</html>
"""


def badge_class(canon_status: str) -> str:
    s = (canon_status or "").lower()
    if s == "canon":
        return "canon"
    if s == "non-canon":
        return "non-canon"
    return ""


def render_index(stories) -> str:
    if not stories:
        body = """
<div class="wrap">
  <div class="empty-state">
    <h2>No stories yet</h2>
    <p>Check back soon — this page updates automatically as new stories are added to the repo.</p>
  </div>
</div>
"""
        return page_shell(SITE_TITLE, body)

    entries = []
    for s in stories:
        badge_cls = badge_class(s["canon_status"])
        tags_html = "".join(
            f'<span class="tag">{html.escape(t)}</span>' for t in s["tags"]
        )
        entries.append(f"""
  <div class="entry">
    <div class="card">
      <div class="meta-row">
        <span class="date">{html.escape(s["date_display"])}</span>
        <span class="category-pill">{html.escape(s["category"])}{" · " + html.escape(s["subtitle"]) if s["subtitle"] and s["subtitle"] != s["category"] else ""}</span>
        <span class="badge {badge_cls}">{html.escape(s["canon_status"])}</span>
      </div>
      <h2><a href="stories/{s['slug']}.html">{html.escape(s["title"])}</a></h2>
      <p class="excerpt">{html.escape(s["excerpt"])}</p>
      <div class="tags">{tags_html}</div>
      <a class="read-link" href="stories/{s['slug']}.html">Read the story →</a>
    </div>
  </div>
""")

    body = f"""
<div class="wrap">
  <div class="feed">
    {"".join(entries)}
  </div>
</div>
"""
    return page_shell(SITE_TITLE, body)


def render_story_page(s) -> str:
    badge_cls = badge_class(s["canon_status"])
    tags_html = "".join(
        f'<span class="tag">{html.escape(t)}</span>' for t in s["tags"]
    )
    body = f"""
<div class="wrap">
  <a class="back-link" href="../index.html">← Back to the timeline</a>
  <div class="story-header">
    <div class="meta-row">
      <span class="date">{html.escape(s["date_display"])}</span>
      <span class="category-pill">{html.escape(s["category"])}{" · " + html.escape(s["subtitle"]) if s["subtitle"] and s["subtitle"] != s["category"] else ""}</span>
      <span class="badge {badge_cls}">{html.escape(s["canon_status"])}</span>
    </div>
    <h1>{html.escape(s["title"])}</h1>
    <div class="tags">{tags_html}</div>
  </div>
  <div class="story-body">
    {s["body_html"]}
  </div>
  <p><a class="back-link" href="../index.html">← Back to the timeline</a></p>
</div>
"""
    return page_shell(s["title"], body)


# -------------------------------------------------------------------- main --

def build(repo_root: Path, out_dir: Path):
    stories_root = repo_root / "stories"
    stories = collect_stories(stories_root)

    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "stories").mkdir(parents=True, exist_ok=True)

    global BOARD_ENABLED
    BOARD_ENABLED = build_board.build_board(repo_root, out_dir)

    (out_dir / "index.html").write_text(render_index(stories), encoding="utf-8")

    if BOARD_ENABLED:
        (out_dir / "board.html").write_text(
            build_board.render_board_page(page_shell), encoding="utf-8")
        (out_dir / "robots.txt").write_text(
            "User-agent: *\nDisallow: /board.html\nDisallow: /board-data.json\n",
            encoding="utf-8")

    for s in stories:
        page = render_story_page(s)
        (out_dir / "stories" / f"{s['slug']}.html").write_text(page, encoding="utf-8")

    print(f"Built {len(stories)} story page(s) into {out_dir} "
          f"(publish: {PUBLISH_POLICY}, order: {ORDER_MODE})")
    for s in stories:
        print(f"  - {s['date_display']:>12}  [{s['category']}]  {s['title']}  ({s['source_path']})")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", default="_site", help="Output directory (default: _site)")
    parser.add_argument("--repo-root", default=".", help="Repo root (default: current directory)")
    parser.add_argument("--publish-policy", choices=["all", "approved"], default=None,
                        help="all: publish every story (default). "
                             "approved: withhold canon_status 'draft' and eval_status 'flagged'. "
                             "A story's own `publish:` frontmatter always wins.")
    parser.add_argument("--order", choices=["date", "reading"], default=None,
                        help="date: newest first by the date written (default). "
                             "reading: by each story's `order:` frontmatter, ascending.")
    args = parser.parse_args()

    global PUBLISH_POLICY, ORDER_MODE
    if args.publish_policy:
        PUBLISH_POLICY = args.publish_policy
    if args.order:
        ORDER_MODE = args.order

    repo_root = Path(args.repo_root).resolve()
    out_dir = Path(args.out).resolve()
    build(repo_root, out_dir)


if __name__ == "__main__":
    main()
