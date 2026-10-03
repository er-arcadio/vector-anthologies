# The Board

All work is tracked as markdown under `board/`. The Kanban tab on the reading site renders it. **Only `lead-editor` creates tickets or changes a ticket's `status`.** Specialists append to the Work Log and may set `in_review` when finished.

## Files
```
board/
  PROJECT.md              charter: goals, scope, definition of success
  stories/US-NNN.md       user stories (outcomes)
  tickets/T-NNN.md        tickets (units of work)
  audit/                  audit reports
  DECISIONS.md            author decision log
```
IDs are sequential and never reused.

## Relationship to the repo's other backlogs
The board does not replace them. It is the single view over them:
- `story-bible/action-items-v5.1.md` — the narrative priority queue. Canonical for narrative priority.
- `story-bible/open-questions.md` — older unresolved decisions.
- `TODO.md` — tooling and process.
- `story-bible/plot-outline/era-1-overview.md` → "Open Gaps".

A ticket that comes from one of these **cites it** in its Inputs and does not fork it. When the author settles something, the lead updates the source file (with approval) as well as the ticket.

## Ticket format
```markdown
---
id: T-001
title: Short imperative title
story: US-001
epic: Foundation
status: ready          # backlog | ready | in_progress | in_review | awaiting_author | done
assignee: story-bible-keeper
priority: high         # high | medium | low
gate: none             # none | G1..G7
blocked_by:            # comma-separated ticket IDs, may be empty
estimate: S            # S | M | L
created: 2026-09-30
updated: 2026-09-30
---
## Goal
## Inputs
## Outputs
## Definition of done
- [ ] checkable
## Decision needed
(only when awaiting_author — numbered, each with a recommended default)
## Work log
## Decision log
```

## User story format
```markdown
---
id: US-001
title: Short title
epic: Foundation
status: backlog        # backlog | ready | in_progress | done
priority: high
---
**As** the author, **I want** ..., **so that** ...

## Acceptance criteria
- [ ] ...

## Tickets
T-001, T-002
```

## Columns
`backlog` → `ready` → `in_progress` → `in_review` → `awaiting_author` → `done`

- **ready** — inputs exist, blockers cleared, definition of done written.
- **in_review** — the lead is checking against the definition of done.
- **awaiting_author** — needs the author. Max 3.
- **done** — definition of done met and, if gated, approved.

## Frontmatter rules
Flat `key: value` lines only — no nesting, no multi-line values. Dates are `YYYY-MM-DD`. The board renderer parses these directly, so a nested or wrapped value will not display.
