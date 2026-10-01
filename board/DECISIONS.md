# Author decision log

One row per decision. The lead appends here whenever the author approves, rejects, or chooses.

| Date | Ticket | Decision | Notes |
|------|--------|----------|-------|
| 2026-09-30 | T-004 | **Author owns the outline; agents draft the prose.** The author decides what happens and writes the outline. `drafting-author` writes the prose from it. The author approves the finished story. Voice is fine-tuned together over time. | `development-editor` supports and pressure-tests the author's outline rather than authoring it. |
| 2026-09-30 | T-015 | **Board privacy: accept the public repo.** The encrypted site tab keeps the board off the reading site; `board/*.md` stays readable on GitHub like the rest of the project. | Revisit if the board starts carrying unpublished plot. |
| 2026-09-30 | T-004 | **First work: the site, then Arc 1.** Fix publish and reading-order control first because it is deterministic, then unblock Arc 1. | T-013 before T-010 / T-011. |
| 2026-09-30 | — | **Landing: branch + PR**, with a local preview so the author can read the whole thing before it merges. | Branch `editorial-team`. |
