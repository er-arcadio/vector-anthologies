# CLAUDE.md — Vector Anthologies

This file orients an agent (or collaborator) working in this repo. Read this first. Each subfolder has its own `CLAUDE.md` with folder-specific guidance — read the relevant one(s) before writing or editing anything in that folder.

## What this repo is

Development and canon repo for the *Vector* series (primary story) and a secondary anthology roster (future, separate continuity — see `reference/`). The goal is a structure any agent can search and cite accurately without re-reading one giant document.

## Before outlining a new arc or story

1. Read `writing-guide/character-journey-worksheet.md` and fill one out per POV/major character.
2. Read `writing-guide/outline-checklist.md` and run the event sequence through it before handing anything off to be drafted as prose.

## Before writing any prose

1. Read `writing-guide/style-guide.md` — tone, voice, and prose rules. Non-negotiable.
2. Read `writing-guide/story-laws.md` — hard canon constraints that must never be contradicted.
3. Read the relevant `story-bible/` files for the character/arc/power involved. Treat `story-bible/` as source of truth; never invent canon that isn't there without flagging it as new.
4. Check `story-bible/foreshadowing-map.md` and `story-bible/plot-twist-inventory.md` — do not accidentally pay off, contradict, or prematurely reveal a seeded thread.
5. New short stories go in `stories/`, never in `story-bible/`. `story-bible/` is canon reference, not prose.

## Folder map

- `story-bible/` — Eli/Vector's canon: world, moral framework, characters, villains, power system, arc-by-arc outline, foreshadowing, open questions, active action items.
- `reference/superhero-reference-book/` — a **separate, not-yet-connected** hero roster for future anthology entries. Do not treat as Vector canon unless a story explicitly crosses over.
- `writing-guide/` — outlining tools (checklist + character worksheet), style guide, story laws, and the reader-preference research behind the style guide's prose defaults. Read before outlining and before writing.
- `themes/` — thematic source material (life-lessons content) that might surface across the anthology; not decided yet how or where. See its `CLAUDE.md` — it's distinct from `story-bible/moral-framework.md`, which is in-world canon.
- `stories/` — actual short story drafts live here. Currently empty; see its `CLAUDE.md` for naming/filing conventions, including the required `date` frontmatter field.
- `scripts/build_site.py` — generates the GitHub Pages reading site (a timeline feed of everything in `stories/`) from each story's frontmatter. Deployed automatically by `.github/workflows/pages.yml` on every push to `main`. Update this if the site's look or behavior needs to change; no need to touch it just to publish a new story.
- `TODO.md` — cross-cutting backlog for tooling/process work (e.g. an eval harness for checking drafts against the writing guide). Separate from `story-bible/action-items-v5.1.md`, which is the narrative-development queue.

## Key naming note

The *Vector* villain formerly called "Blink" is now **Twitch** (`story-bible/villains/twitch.md`) to avoid collision with the reference-roster hero **Blink** (`reference/superhero-reference-book/06-blink.md`). These are two unrelated characters — do not merge them.

## Status flags worth knowing about

Files with unresolved development needs carry a `status:` line in their frontmatter. As of this writing: `story-bible/characters/iris.md`, `story-bible/plot-outline/arc-08.md`, `story-bible/action-items-v5.1.md` (active priority queue), and two files in the reference roster. Check `story-bible/action-items-v5.1.md` for the current priority order before assuming a thread is settled.
