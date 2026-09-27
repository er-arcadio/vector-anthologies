# CLAUDE.md — stories/

This is where actual prose lives. Currently empty — a `.gitkeep` placeholder is the only thing here so Git tracks the folder.

## Before writing a story here

Read, in order:
1. `../writing-guide/style-guide.md`
2. `../writing-guide/story-laws.md`
3. The relevant `../story-bible/` files for whichever characters/arc/powers the story touches
4. `../story-bible/foreshadowing-map.md` and `../story-bible/plot-twist-inventory.md` — check nothing here is contradicted or prematurely paid off

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
date: YYYY-MM-DD
---
```

## `canon_status` matters

Not every short story needs to be treated as binding canon. Mark clearly whether a piece is meant to lock in new story-bible facts (in which case the relevant `story-bible/` file should be updated to match once the story is finalized) or is a non-canon "what if" / side piece.

## `date` is required

`date` is the real-world date the story was written (not in-story chronology — that's what the arc/character folder already encodes), in plain `YYYY-MM-DD` form. It drives the reading site's timeline (see below) — a story without one still publishes, but sorts to the bottom and shows "Date unknown" instead of a real date.

## Reading site

This repo publishes itself as a GitHub Pages site (a Reddit/Twitter/Tumblr-inspired timeline feed of every story, newest first, linking out to a full reading page per story). It rebuilds automatically from `scripts/build_site.py` via `.github/workflows/pages.yml` on every push to `main` that touches this folder — nothing needs to be done manually to publish a new story beyond writing the file with correct frontmatter and pushing it. See `scripts/build_site.py` if the site's look or behavior ever needs to change; it reads `title`, `tags`, `canon_status`, and `date` directly from each file's frontmatter, and infers the Vector/Anthology category and arc/character label from the file's path under this folder.
