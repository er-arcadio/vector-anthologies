# How the author reviews a proposal

Proposals get long, because the reasoning behind a recommendation is worth recording. But the author should never have to read a long document to make a decision. This is how that is squared.

## Every proposal ships as two files

| File | What it is | Who reads it |
|---|---|---|
| `T-NNN-decisions.md` | One block per decision. Options, a recommendation, the cost, and an **Author's call** line. Nothing else. | The author, always |
| `T-NNN-proposal.md` | The reasoning, evidence, quotes and filled worksheets behind those recommendations. | Only when a recommendation looks wrong and he wants to see why |

The decisions file must stand alone. If the author has to open the proposal to understand what he is choosing between, the decisions file has failed and the lead sends it back.

## Every proposal ships as a pull request

A proposal is never dropped into chat as a wall of text. The lead opens a PR containing both files, and the author reviews it on GitHub:

- Comment on any line in **Files changed** to push back, ask a question, or pick something other than the recommendation.
- Or fill in the **Author's call** line inline.
- Or approve the PR to accept every recommendation as written.

The lead reads the review comments back, applies the decisions, replies to each thread, and pushes the result to the same PR. The author re-reviews only what changed.

This gives the project a durable, line-anchored record of why canon is what it is — in the same place as the change itself, rather than scattered through a chat log.

## Rules for the lead

1. **Mark the load-bearing decisions.** Use ★ for the ones that change what gets written. Everything else is taste and must be deferrable without blocking work.
2. **State the cost of each decision**, including what it forces elsewhere. A decision that quietly requires rewriting an existing draft must say so.
3. **Never bundle a canon addition into a detail question.** If a decision adds something the bible does not currently contain, say so and route it as its own Canon Change Proposal.
4. **Silence is consent, so say that out loud.** Anything the author does not address is treated as accepting the recommendation. He needs to know that is the rule.
5. **Report what the ticket did not achieve.** If a proposal unblocks less than the ticket was scoped to, that goes in the decisions file, not buried in the proposal.
6. **One PR per ticket.** Do not mix a proposal with tooling changes — review comments become unreadable when the diff contains both.

## Applying the decisions

Once the author has decided:
1. Record each decision in `board/DECISIONS.md` with the date and the ticket.
2. Apply the canon changes to `story-bible/` — this is the one moment agents write to canon, and only for decisions the author explicitly made.
3. Reply to each review thread saying what was done.
4. Move the ticket to `done` and open whatever the decisions unblocked.
