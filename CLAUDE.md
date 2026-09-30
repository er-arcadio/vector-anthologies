# CLAUDE.md — Vector Anthologies

This file orients an agent (or collaborator) working in this repo. Read this first. Each subfolder has its own `CLAUDE.md` with folder-specific guidance — read the relevant one(s) before writing or editing anything in that folder.

## How work is run

This project is run by an editorial team of agents. **Start every session as `lead-editor`** (`.claude/agents/lead-editor.md`) — it is the only agent the author talks to, it owns the board in `board/`, and it delegates to the specialists.

- `publishing-house/WORKFLOW.md` — the stages from slate entry to published story, and where the author's approval is required. It wraps the pipeline described below; it does not replace it.
- `publishing-house/BOARD.md` — ticket and user-story conventions. All work is a ticket in `board/`.
- `publishing-house/HIRING.md` — creating a new agent costs tokens and needs the author's approval first.
- `publishing-house/ROSTER.md` — who is on the team, and the bench.
- `board/audit/` — the standing audits. Start with the most recent `AUDIT-*.md`.

`story-bible/` is canon and agents never change it; canon changes are proposed to the author. `.claude/agents/board-of-advisors.md` is the project's critique panel — convene it, never duplicate it.

## What this repo is

Development and canon repo for the *Vector* series (primary story) and a secondary anthology roster (future, separate continuity — see `reference/`). The goal is a structure any agent can search and cite accurately without re-reading one giant document.

## Before outlining a new arc or story

1. Read `writing-guide/character-journey-worksheet.md` and fill one out per POV/major character — check `story-bible/characters/` first for an already-filled instance (e.g. `eli-reyes-journey-worksheet.md`) rather than re-deriving want/need from scratch.
2. For anything set in Arcs 1–7, read `story-bible/plot-outline/era-1-overview.md` for that arc's starting point / want / obstacle / resolution shape (currently draft, pending author agreement — check its "Open Gaps" section).
3. Read `writing-guide/outline-checklist.md` and run the event sequence through it before handing anything off to be drafted as prose. Every story needs an actual point A, point B, want, and obstacle — not just a mood or an image.

## Before writing any prose

1. Read `writing-guide/style-guide.md` — tone, voice, and prose rules (including the 3,000–5,000 word short-story length target). Non-negotiable.
2. Read `writing-guide/story-laws.md` — hard canon constraints that must never be contradicted.
3. Read the relevant `story-bible/` files for the character/arc/power involved. Treat `story-bible/` as source of truth; never invent canon that isn't there without flagging it as new.
4. Check `story-bible/foreshadowing-map.md` and `story-bible/plot-twist-inventory.md` — do not accidentally pay off, contradict, or prematurely reveal a seeded thread.
5. New short stories go in `stories/`, never in `story-bible/`. `story-bible/` is canon reference, not prose.

## After writing a draft

1. Run it against `writing-guide/eval-checklist.md` before treating it as done, and record the result in the story's `eval_status` frontmatter (see `stories/CLAUDE.md`).
2. **Convene the board of advisors** (`.claude/agents/board-of-advisors.md`) and present its read *alongside* the draft whenever handing a draft to the author for review. The board flags — it doesn't correct or gatekeep. Its purpose is to surface what a diverse room of readers would notice that the author might not, so he's choosing deliberately rather than by default. Never act on its flags unilaterally; the author decides what to take.

## Folder map

- `story-bible/` — Eli/Vector's canon: world, moral framework, characters, villains, power system, arc-by-arc outline, foreshadowing, open questions, active action items.
- `reference/superhero-reference-book/` — a **separate, not-yet-connected** hero roster for future anthology entries. Do not treat as Vector canon unless a story explicitly crosses over.
- `writing-guide/` — outlining tools (checklist + character worksheet), style guide, story laws, and the reader-preference research behind the style guide's prose defaults. Read before outlining and before writing.
- `themes/` — thematic source material (life-lessons content) that might surface across the anthology; not decided yet how or where. See its `CLAUDE.md` — it's distinct from `story-bible/moral-framework.md`, which is in-world canon.
- `stories/` — actual short story drafts live here. Currently empty; see its `CLAUDE.md` for naming/filing conventions, including the required `date` frontmatter field.
- `scripts/build_site.py` — generates the GitHub Pages reading site (a timeline feed of everything in `stories/`) from each story's frontmatter. Deployed automatically by `.github/workflows/pages.yml` on every push to `main`. Update this if the site's look or behavior needs to change; no need to touch it just to publish a new story.
- `TODO.md` — cross-cutting backlog for tooling/process work. Separate from `story-bible/action-items-v5.1.md`, which is the narrative-development queue. The eval harness for checking drafts against the writing guide is built — see `writing-guide/eval-checklist.md`.

## Key naming note

The *Vector* villain formerly called "Blink" is now **Twitch** (`story-bible/villains/twitch.md`) to avoid collision with the reference-roster hero **Blink** (`reference/superhero-reference-book/06-blink.md`). These are two unrelated characters — do not merge them.

## Status flags worth knowing about

Files with unresolved development needs carry a `status:` line in their frontmatter. As of this writing: `story-bible/characters/iris.md`, `story-bible/plot-outline/arc-08.md`, `story-bible/plot-outline/era-1-overview.md` (draft, pending author agreement — see its "Open Gaps" section), `story-bible/suit-evolution.md` (color-arc concept settled, exact arc-by-arc transitions open), and `reference/superhero-reference-book/05-vampire-doctor.md` and `06-blink.md`. `story-bible/action-items-v5.1.md` doesn't carry a `status:` field itself but *is* the active priority queue — check it for the current priority order before assuming a thread is settled.

`stories/vector/arc-05/the-name-first.md` is currently `eval_status: flagged` / `canon_status: draft` — written before the current style-guide and length standards, not yet approved, pending revision once the Era 1 outline above is agreed.
