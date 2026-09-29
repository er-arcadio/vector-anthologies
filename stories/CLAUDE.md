# CLAUDE.md — stories/

This is where actual prose lives. Currently empty — a `.gitkeep` placeholder is the only thing here so Git tracks the folder.

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

## The "story shape" block is required

Every story needs a protagonist moving from a starting point to a changed one, a want, and a real obstacle — not just a mood or an image. Point A and Point B are concrete states (a situation or condition, stated as a real before-and-after — e.g. "guarded, hiding the power" → "told his mother, first taste of trusting someone with it"), not a pair of abstract lessons or themes. Fill in the `<!-- story shape -->` block above from the `character-journey-worksheet.md` / `outline-checklist.md` pass you already ran before drafting (see "Before writing a story here"). This makes the want/need/obstacle/resolution visible and reviewable instead of something the outline stage privately assumed and the reader has to reverse-engineer. Keep it in the file — it's cheap context for the next person (or agent) who touches this story, and it's the first thing `eval-checklist.md` checks.

## `canon_status` matters

Not every short story needs to be treated as binding canon. Mark clearly whether a piece is meant to lock in new story-bible facts (in which case the relevant `story-bible/` file should be updated to match once the story is finalized) or is a non-canon "what if" / side piece.

## `eval_status` and the eval checklist

Before a story counts as done, run it against `../writing-guide/eval-checklist.md` — length, story shape, style-guide compliance, story-laws compliance, a check against `../story-bible/foreshadowing-map.md` and `../story-bible/plot-twist-inventory.md`, and a board-of-advisors pass (`../.claude/agents/board-of-advisors.md`, presented with the draft rather than acted on). Record the result in `eval_status`. A flagged story can still be filed as `canon_status: draft`, but shouldn't move to `canon_status: canon` (i.e. get folded back into `story-bible/`) with an open flag on a canon-facing check. If anything's flagged, add a short `<!-- eval notes -->` comment at the bottom of the story file itself — see the checklist for what to record.

## `date` is required

`date` is the real-world date the story was written (not in-story chronology — that's what the arc/character folder already encodes), in plain `YYYY-MM-DD` form. It drives the reading site's timeline (see below) — a story without one still publishes, but sorts to the bottom and shows "Date unknown" instead of a real date.

## Reading site

This repo publishes itself as a GitHub Pages site (a Reddit/Twitter/Tumblr-inspired timeline feed of every story, newest first, linking out to a full reading page per story). It rebuilds automatically from `scripts/build_site.py` via `.github/workflows/pages.yml` on every push to `main` that touches this folder — nothing needs to be done manually to publish a new story beyond writing the file with correct frontmatter and pushing it. See `scripts/build_site.py` if the site's look or behavior ever needs to change; it reads `title`, `tags`, `canon_status`, and `date` directly from each file's frontmatter, and infers the Vector/Anthology category and arc/character label from the file's path under this folder.
