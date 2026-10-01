# Project charter

_Drafted by the lead editor at onboarding. Sections marked TBD need the author at Gate G1 (ticket T-004)._

## What this is
*Vector Anthologies* — the *Vector* series (Eli Reyes, Arcs 0-9) as short stories, plus a separate anthology roster held in `reference/` for later.

## Where it stands (2026-09-30)
A deep, well-organised story bible; a mature writing guide with real standards; a working public reading site; one story drafted and flagged. The bottleneck is not ideas — it is that canon contradicts itself in a few load-bearing places, and the slate stops one level short of the story shape the drafting standard requires.

- Slate readiness: of 38 slate stories, 14 draftable, 19 need work, 5 blocked.
- Canon: 11 blockers, 39 should-fix, 25 notes.
- Arc 1 and Arc 2 are the most ready. Arc 6 has none draftable.

## How the work divides
The author decides **what happens** and writes the **outline**. `drafting-author` writes the **prose** from that outline. The author **approves** the finished story. Voice is tuned collaboratively over time rather than specified up front.

This makes the outline the load-bearing artefact. `development-editor` does not author it — it pressure-tests the author's outline against `outline-checklist.md`, fills the story-shape fields, and flags what is missing before prose is attempted.

## Goals
Get from a deep bible to finished stories, without the author having to hold the whole thing in his head. Concretely: a repeatable path from an outline he writes to a drafted, checked, approved story on the site.

## Definition of success
Milestone 1: one story taken end to end — author outline → agent draft → eval → board of advisors → author approval → published — with the real cost and quality of that loop known.

## Milestone 1
1. **T-013** — give the site publish and reading-order control. Deterministic, and it stops drafts publishing themselves.
2. **T-010** — name and characterise the family, which unblocks five Arc 1 stories.
3. **T-011** — bring the Arc 1 slate to drafting-ready shape so the author has something concrete to outline against.
4. Pilot one Arc 1 story end to end.

## Constraints
- The author supplies ideas and structure, approves details, and approves finished stories.
- `story-bible/` is canon. Agents propose changes; the author decides.
- `writing-guide/style-guide.md` and `story-laws.md` are non-negotiable.
- The author is developing his own voice. Agents flag rather than correct.
- New agents cost money and need the author's approval first.
- The repo and the reading site are public.

## Settled
- Who writes what: author outlines, agents draft, author approves (T-004).
- Board privacy: public repo accepted; the site tab stays encrypted (T-015).

## Still open
- The fate of the existing flagged draft (T-012).
- The publish policy the site should default to, now that T-013 makes it configurable.
