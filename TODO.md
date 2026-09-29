# TODO

Cross-cutting backlog for tooling and process work — not narrative development. For the active story/canon priority queue, see `story-bible/action-items-v5.1.md` instead.

## Done

- ~~Build an eval harness for drafts.~~ Built as `writing-guide/eval-checklist.md`: a manual (human/agent) checklist run once per finished draft, covering length, style-guide compliance, story-laws compliance, and a canon cross-check against the foreshadowing map and twist inventory. Results are recorded in the story's own `eval_status` frontmatter field plus an inline `<!-- eval notes -->` comment if anything's flagged (see `stories/CLAUDE.md`). Flags don't block filing a draft, but a story can't move to `canon_status: canon` with an open flag in the canon-facing sections.

## Open

- **Overlay the hero's journey framework onto the character arcs.** Map the standard stages (call, refusal, mentor, threshold, trials, abyss, transformation, return) onto Eli's journey across Arcs 0–9, onto Vinny's parallel journey as its inversion, and — once she has a want (`story-bible/characters/iris.md`) — potentially onto Iris's. Arc 1 already has an explicit refusal-of-the-call and a mentor turn (his mother), so the framework is partly latent in the material; the task is to check the whole span for stages that are missing, out of order, or accidentally doubled, rather than to force the structure where it doesn't fit. Probably lives as a new file in `writing-guide/` or alongside `story-bible/eli-character-arc.md`.
