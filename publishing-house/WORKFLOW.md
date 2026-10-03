# Workflow: from slate entry to published story

This wraps the pipeline this repo already documents in `CLAUDE.md` and `stories/CLAUDE.md`. It does not replace it — it adds who does each step, and where the author's approval is required.

The author owns **ideas, structure, and final approval**. The Lead Editor runs everything else.

## Stages

| # | Stage | Owner | Output | Gate |
|---|-------|-------|--------|------|
| 0 | Audit and roadmap | lead-editor + specialists | `board/audit/`, roadmap | **G1** Author approves the roadmap |
| 1 | Slate agreement | development-editor | An arc's slate entries filled to drafting-ready shape | **G2** Author agrees the slate |
| 2 | Continuity pre-check | story-bible-keeper | Conflicts and gaps for this story | (feeds G3) |
| 3 | Worksheet + outline | **author**, supported by development-editor | Author's outline, pressure-tested against `outline-checklist.md`, with the story-shape block complete | **G3** Author confirms the outline is ready to draft |
| 4 | Draft | drafting-author | Draft in `stories/...` with full frontmatter | (internal) |
| 5 | Eval | anyone **except** the drafter | `eval-checklist.md` run, `eval_status` recorded | (internal) |
| 6 | Board of advisors | board-of-advisors | `<slug>.board-review.md` sidecar | (internal) |
| 7 | Revision | drafting-author | Revised draft | **G4** Author approves the story |
| 8 | Line pass | line-editor | `<slug>.line-review.md` markup sidecar | (internal) |
| 9 | Copy and proof | copy-proofreader | Corrections + queries | **G5** Author approves final text |
| 10 | Canon fold-back | story-bible-keeper | Canon Change Proposal for anything the story locks in | **G6** Author approves canon changes |
| 11 | Publish | author (production-formatter prepares) | Push to `main`; Pages redeploys | **G7** Author pushes |

## Who writes what (settled 2026-09-30, T-004)
The **author decides what happens and writes the outline**. `drafting-author` writes the **prose** from that outline. The author **approves** the finished story.

So the outline is the load-bearing artefact in this project, and `development-editor` does not author it. Its job at stage 3 is to take the author's outline and:
- run it through `writing-guide/outline-checklist.md` and report what fails,
- fill in or query the story-shape fields `stories/CLAUDE.md` requires (want, need, Point A, Point B, obstacle type, cost, `story_type`),
- flag canon it depends on that does not exist yet,
- say plainly if it is not yet a story — a mood or an image is not an A-to-B.

It proposes; the author decides. An outline reaches `drafting-author` only once the author says it is ready.

## How this maps onto the repo's own rules
- Stage 5 is `writing-guide/eval-checklist.md`, recorded in the story's `eval_status`. **The drafter does not run their own eval.**
- Stage 6 is the existing `.claude/agents/board-of-advisors.md`. It **flags, never corrects, never gatekeeps**. Its flags are presented alongside the draft; the author decides. Canon and consistency errors it catches get copied into the story's `<!-- eval notes -->`; craft and perspective flags stay in the sidecar only.
- A flagged story may still be filed as `canon_status: draft`. It must not move to `canon_status: canon` with an open flag on a canon-facing check.
- Stage 10 exists because `stories/CLAUDE.md` requires the relevant `story-bible/` file to be updated once a canon-locking story is finalised. That update is a canon change, so it is the author's call.

## Gates
Gates are reviewed as pull requests — see `publishing-house/REVIEW.md` for the two-file format and the review protocol.

A gate is a ticket in `awaiting_author`. The lead prepares a decision packet so approving takes minutes:
- What is being approved, in one sentence, with file paths.
- A short summary and the lead's recommendation.
- Numbered questions, each with a default.
- What happens next on approval.

The author replies `approve`, `approve with changes: ...`, or `reject: ...`. The lead records it in the ticket's Decision Log and in `board/DECISIONS.md`. **No agent passes a gate.**

## Rules of the house
1. **One writer per file.** A specialist writes only the files its ticket names.
2. **Canon changes are author decisions.** Facts a draft invents are `proposed` until approved.
3. **The eval is independent.** Never the drafter.
4. **Revision cap**: two draft-critique loops per story, then the lead escalates with a recommendation (revise, rewrite from outline, or shelve).
5. **WIP limits**: at most 3 tickets `in_progress` and at most 3 in `awaiting_author`, so the author is never flooded. The lead decides what he sees first.
6. **Everything published is public.** The repo and the reading site are both public, and `build_site.py` publishes every story file regardless of `canon_status` or `eval_status`. Treat "written" as "published" unless the story is deliberately kept out of `stories/`.

## Per-story ticket chain
Pitch/slate entry (G2) → continuity pre-check → worksheet + outline (G3) → draft → eval → board → revision (G4) → line pass → copy and proof (G5) → canon fold-back (G6) → publish (G7).
