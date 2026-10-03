# CLAUDE.md — stories/

This is where actual prose lives. Currently one draft: `vector/arc-05/the-name-first.md` (flagged, pre-standards).

## Before writing a story here

Read, in order:
1. `../writing-guide/style-guide.md`
2. `../writing-guide/story-laws.md`
3. `../writing-guide/character-journey-worksheet.md` — check `../story-bible/characters/` for an already-filled instance (e.g. `eli-reyes-journey-worksheet.md`) before re-deriving a character's want/need from scratch
4. `../writing-guide/outline-checklist.md` — run the event sequence through it; this is where the story's A-to-B (starting point, want, obstacle, resolution) actually gets nailed down before drafting
5. The relevant `../story-bible/` files for whichever characters/arc/powers the story touches — for anything in Arcs 1–7, start with `../story-bible/plot-outline/era-1-overview.md`
6. `../story-bible/foreshadowing-map.md` and `../story-bible/plot-twist-inventory.md` — check nothing here is contradicted or prematurely paid off

## Filing convention

Suggested structure once stories exist — adjust as the anthology grows:

```
stories/
├── vector/                  main-series short stories, by arc
│   ├── arc-01/
│   ├── arc-02/
│   └── ...
└── anthology/                stories using the reference/ roster, once developed
    └── <character-name>/
```

Each story file should open with light frontmatter for lookup:

```markdown
---
title: "Story Title"
tags: [story, arc-X, character-name]
story_type: arc-advancing | single-beat
canon_status: draft | canon | non-canon
eval_status: unreviewed | passed | flagged
date: YYYY-MM-DD
---

<!-- story shape
POV: 
Want: 
Need: 
Point A (starting state): 
Point B (ending state): 
Obstacle (external | interpersonal | internal): 
Resolution and its cost: 
-->
```

## `story_type` — which kind of piece this is

Two forms, and every story declares one (full definitions in `../writing-guide/style-guide.md` → Length):

- **`arc-advancing`** — the default. Targets 3,000–5,000 words, needs a real A-to-B with a want and an obstacle, moves the arc it sits in. **These should outnumber single-beat pieces.**
- **`single-beat`** — no floor, typically 800–1,500 words. For beats whose power is compression and which longer treatment would ruin (Theo's death in two sentences, the diner scene, the arc where Vinny simply doesn't appear). Exempt from the A-to-B requirement, and exempt from the word floor, by definition.

Switch between them freely from piece to piece. The one thing not to do is reclassify a piece as `single-beat` *after* an arc-advancing draft came in short — that's a flag, not a category change.

## The "story shape" block is required

Required for `arc-advancing` stories; optional for `single-beat` pieces (where "Effect I'm going for:" is the one line worth recording instead).

An arc-advancing story needs a protagonist moving from a starting point to a changed one, a want, and a real obstacle — not just a mood or an image. Point A and Point B are concrete states (a situation or condition, stated as a real before-and-after — e.g. "guarded, hiding the power" → "told his mother, first taste of trusting someone with it"), not a pair of abstract lessons or themes. Fill in the `<!-- story shape -->` block above from the `character-journey-worksheet.md` / `outline-checklist.md` pass you already ran before drafting (see "Before writing a story here"). This makes the want/need/obstacle/resolution visible and reviewable instead of something the outline stage privately assumed and the reader has to reverse-engineer. Keep it in the file — it's cheap context for the next person (or agent) who touches this story, and it's the first thing `eval-checklist.md` checks.

## `publish` and `order` — controlling the public site

Two optional frontmatter fields control what reaches the reading site and in what order. Both were added because the generator previously published **every** file under `stories/` regardless of status.

```markdown
publish: false     # keep this story off the public site, whatever the policy
order: 3           # reading-order position, used when the site is built in reading order
```

**`publish`** — an explicit override that always wins. `publish: false` withholds a story even from an otherwise-publishing build; `publish: true` forces one through even when the build policy would withhold it. Omit the field for normal behaviour.

**The build policy** decides what happens to stories with no `publish` field:

| Policy | Behaviour |
|---|---|
| `all` (default) | Publish everything, as before. |
| `approved` | Withhold `canon_status: draft` and `eval_status: flagged`. |

Set it per build with `--publish-policy approved`, or with the `PUBLISH_POLICY` environment variable in `.github/workflows/pages.yml`. Every withheld story is named in the build log with the reason, so nothing disappears silently.

**`order`** — an integer. With `--order reading` (or `ORDER_MODE=reading`), the feed is sorted by `order` ascending so it can be read front to back; stories without an `order` fall to the end, newest first among themselves. The default remains `--order date`: newest first by the date written.

## `canon_status` matters

Not every short story needs to be treated as binding canon. Mark clearly whether a piece is meant to lock in new story-bible facts (in which case the relevant `story-bible/` file should be updated to match once the story is finalized) or is a non-canon "what if" / side piece.

## `eval_status` and the eval checklist

Before a story counts as done, run it against `../writing-guide/eval-checklist.md` — length, story shape, style-guide compliance, story-laws compliance, a check against `../story-bible/foreshadowing-map.md` and `../story-bible/plot-twist-inventory.md`, and a board-of-advisors pass (`../.claude/agents/board-of-advisors.md`, presented with the draft rather than acted on). Record the result in `eval_status`. A flagged story can still be filed as `canon_status: draft`, but shouldn't move to `canon_status: canon` (i.e. get folded back into `story-bible/`) with an open flag on a canon-facing check. If anything's flagged, add a short `<!-- eval notes -->` comment at the bottom of the story file itself — see the checklist for what to record.

## Board reviews live next to the story

A board-of-advisors report is saved as a sidecar beside the story it reviews: `<story-slug>.board-review.md` (e.g. `vector/arc-05/the-name-first.board-review.md`). That keeps the review versioned with the draft it's about and readable on GitHub without digging through chat history.

`scripts/build_site.py` skips any file ending in `-review.md`, so sidecars never publish to the reading site. Canon and consistency errors the board catches get copied into the story's own `<!-- eval notes -->` (those are objective fixes); craft, structure, and perspective flags stay in the sidecar only, because those are the author's call and shouldn't read as a to-do list.

## `date` is required

`date` is the real-world date the story was written (not in-story chronology — that's what the arc/character folder already encodes), in plain `YYYY-MM-DD` form. It drives the reading site's timeline (see below) — a story without one still publishes, but sorts to the bottom and shows "Date unknown" instead of a real date.

## Reading site

This repo publishes itself as a GitHub Pages site (a Reddit/Twitter/Tumblr-inspired timeline feed of every story, newest first, linking out to a full reading page per story). It rebuilds automatically from `scripts/build_site.py` via `.github/workflows/pages.yml` on every push to `main` that touches this folder — nothing needs to be done manually to publish a new story beyond writing the file with correct frontmatter and pushing it. See `scripts/build_site.py` if the site's look or behavior ever needs to change; it reads `title`, `tags`, `canon_status`, and `date` directly from each file's frontmatter, and infers the Vector/Anthology category and arc/character label from the file's path under this folder.
