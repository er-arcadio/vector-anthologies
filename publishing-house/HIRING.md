# Hiring protocol (creating a new agent)

Every new agent costs tokens and adds coordination overhead. Hire only when the work **recurs** and no existing agent covers it well.

## Before proposing a hire, the lead checks
1. Can an existing agent do this with a better brief? Prefer that.
2. Does `.claude/agents/board-of-advisors.md` already cover it? It is the project's critique panel — never build a second one.
3. Is it a one-off? Use a one-off general-purpose subagent with a tight brief, and still tell the author the expected cost.
4. Will it recur across several stories? Then a permanent agent is justified.

## The proposal (the author sees this before anything is created)
```
Role: <title>
Why now: <the gap, with ticket IDs>
Scope: <what they will and will not do>
Recurring or one-off:
Model tier: haiku | sonnet | opus   (and why)
Tools: <the minimum needed>
Estimated cost: <rough tokens per task x tasks planned>
Alternative considered: <existing agent / one-off / do without>
Recommendation: hire / don't hire
```
The author answers **hire**, **one-off only**, or **no**.

## After approval
1. Create `.claude/agents/<slug>.md` with frontmatter (`name`, `description`, `model`, `tools`) and a body covering responsibilities, rules, inputs, outputs, and definition of done. Match the house style of the existing agents, and point at this repo's real paths (`story-bible/`, `writing-guide/`, `stories/`).
2. Add a row to `publishing-house/ROSTER.md` with the date and the approving decision.
3. Create the first tickets and assign them.

## Model tiers
- **opus** — judgement-heavy creative and structural work (lead, development, drafting, the board).
- **sonnet** — analysis, critique, research, line work.
- **haiku** — mechanical passes (proofreading, formatting).

## Firing
An agent that goes unused, or repeatedly fails its definition of done, gets proposed for retirement. Move it to ROSTER.md's Retired section. Deleting the file is the author's call.
