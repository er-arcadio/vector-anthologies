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
---
```

## `canon_status` matters

Not every short story needs to be treated as binding canon. Mark clearly whether a piece is meant to lock in new story-bible facts (in which case the relevant `story-bible/` file should be updated to match once the story is finalized) or is a non-canon "what if" / side piece.
