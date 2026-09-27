# TODO

Cross-cutting backlog for tooling and process work — not narrative development. For the active story/canon priority queue, see `story-bible/action-items-v5.1.md` instead.

## Open

- **Build an eval harness for drafts.** A repeatable way to check a new or edited story in `stories/` against `writing-guide/` (style guide, story laws) and relevant `story-bible/` canon before it's considered done — a quality gate, not just a style opinion.
  - Should catch, at minimum: dialogue scenes broken up by narration beats on nearly every line (violates the sustained-dialogue default in `style-guide.md`); tense misuse (present tense should be the default, past tense only when a character is reflecting back or telling a story); contradictions with `story-bible/foreshadowing-map.md` or `story-bible/plot-twist-inventory.md` (paying off, contradicting, or prematurely revealing a seeded thread); canon conflicts with character/villain/power-system files.
  - Open questions to resolve when scoping this: automated (e.g. an LLM-graded rubric run against each draft) vs. a checklist a human/agent runs manually before filing a story as done; where results should live (inline PR comments, a report file per story, a status field in frontmatter); whether it blocks filing a story or just flags issues for review.
