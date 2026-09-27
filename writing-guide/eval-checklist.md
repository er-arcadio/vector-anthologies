---
title: "Draft Eval Checklist"
tags: [writing-guide, eval, checklist, quality-gate]
---

# Draft Eval Checklist

A quality gate, not a style opinion. Run this against a finished draft in
`stories/` before treating it as done — after `outline-checklist.md` has
already done its job at the outline stage, this is the equivalent pass on
actual prose. Manual (human or agent), run once per draft. Not automated,
and not meant to be: the checks below are judgment calls a script can't
reliably make, and this repo has exactly one author whose voice is the
thing being protected, not a team that needs a bot to enforce a house
style.

**This gate flags, it doesn't block.** A draft can be filed with open
flags — see `eval_status` below. But a story can't move from
`canon_status: draft` to `canon_status: canon` (i.e. its facts get folded
back into `story-bible/`) with unresolved flags in Sections 2 or 3 — those
are the sections that protect continuity for everything written after it.

Record the outcome in the story's own frontmatter (`eval_status:
unreviewed | passed | flagged` — see `stories/CLAUDE.md`) and, if anything
is flagged, leave a short `<!-- eval notes -->` HTML comment block at the
bottom of the story file itself: what was flagged, and whether it was
fixed, accepted as an intentional exception, or left for later. Keep the
record with the story, not in a separate report file — it's one author,
one file per decision.

---

## 0. Length and Shape

- [ ] Word count falls in the **3,000–5,000 word** band (`style-guide.md`
  → Length). If it's outside the band, that's not an automatic fail, but
  it's not a silent pass either: **write the rationale into the eval
  notes** — why this piece earned more room, or why it said everything it
  needed to say short. A story under the floor with no rationale recorded
  is a flag, not an exception.
- [ ] The `<!-- story shape -->` block (`stories/CLAUDE.md`) is filled in:
  POV, want, need, point A, point B, obstacle (external / interpersonal /
  internal), and what the resolution costs. If any field is vague or
  can't be answered from the actual text, the story doesn't have a clear
  A-to-B yet — that's a flag, and it usually means `outline-checklist.md`
  got skipped rather than run.

## 1. Style Guide Compliance (`style-guide.md`)

- [ ] **Tone blend** reads roughly 60% grounded drama / 30% visceral
  action / 10% horror-hum — not a genre switch, a ratio. A story doesn't
  need all three in equal measure, but if it's 90% one lane, ask whether
  that's the story's actual center of gravity or a default.
- [ ] **Narrative voice:** present tense is the default register. Any
  past-tense passage has a real in-scene reason (the narrator stepping
  back into explicit reflection, or telling a story within the story) —
  not a scheduled "big moment" that could just as easily be present tense.
- [ ] **Present-tense break:** if a past-tense passage exists, its most
  overwhelming beat snaps back to present tense. A past-tense passage that
  never breaks is a flag.
- [ ] **Dialogue — sparse AND sustained, not either/or.** This is the
  single most common failure mode to check for explicitly: read any
  dialogue-heavy scene and count how often narration interrupts between
  lines. If narration steps in on *nearly every line*, that's a violation
  of the sustained-exchange default even if each individual line is
  appropriately terse — the two axes (line length, interruption frequency)
  are independent and both need to pass.
- [ ] **Horror register** stays a background hum: planted without
  follow-up explanation in the same scene, absence over performed grief,
  no ambiguous thread over-confirmed. If a wrong detail gets explained
  immediately, or a loss gets a full mourning scene, flag it.
- [ ] **Fight writing** (if applicable): every ability used visibly
  affects its environment (cross-check
  `story-bible/power-system/abilities-environmental-effects.md`); the
  fight's stakes trace to character, not just spectacle; restraint gets
  real page time, not just the escalation.
- [ ] **Research anchor** (if a power/consequence is on the page): does it
  trace to something real, or is it flavor text standing in for a
  mechanism? Check against
  `story-bible/power-system/physical-consequences-and-canon.md`.
- [ ] **Young Eli's voice** (if the story is set in Arcs 1–4, ages
  16–21): does his in-scene interiority actually read like a teenager's —
  cause-and-effect minded, fixated on what he already cares about, low
  emotional vocabulary — rather than the older narrator's retrospective
  polish leaking into the character being depicted? Check the dread-vs-
  anxiety distinction specifically: is dread showing up where he hasn't
  yet connected an obligation to responsibility, and anxiety where he
  has? See `style-guide.md` (Narrative Voice) and
  `story-bible/characters/eli-reyes-journey-worksheet.md`.

## 2. Story Laws Compliance (`story-laws.md`) — hard constraints

- [ ] **No moral framing.** Villain or hero, judgment comes from POV only.
  Outside a POV filter (omniscient register), competing philosophies are
  presented, not verdicts.
- [ ] **Power system:** knowledge-dependency rule intact (no power Eli
  hasn't earned via comprehension); playing-god ceiling written as a
  standing refusal, never an inability; precision/surgical use preserved
  for top-tier abilities (no sloppy portrayal that would contradict
  "ethics and physics are the same thing").
- [ ] **Vinny (if present):** self-healing shown as integration, not
  passive defense; empathy decline is trackable and specific, not a
  personality flip; at most the one allowed "Joker crack" exists anywhere
  in the whole story — check this isn't the story that spends it, unless
  it's meant to be.
- [ ] **Eli's growth engine:** does the climax turn on out-fighting
  someone, or on choosing something harder than winning? If it's the
  former, the story's actual engine (per `story-laws.md`) is missing.
- [ ] **Suit check** (if Eli is suited and the story is arc-placed):
  matches `story-bible/suit-evolution.md` for that arc.
- [ ] **Timeline discipline:** ages, power stage (Think/Know/Feel-Become —
  check `story-bible/power-system/arc-by-arc-power-progression.md`), and
  relationship status all match the arc the story is set in. No borrowed
  later-arc capability or relationship beat.
- [ ] **Moral framework era-lock:** if Earth-set (Arcs 1–7), the world's
  moral/spiritual framework stays ambient and unconfronted — no
  arguing-for or rationalizing it on the page. That confrontation is
  reserved for Arc 8.
- [ ] **Reference-roster boundary:** no uncredited crossover between
  `story-bible/` characters and `reference/superhero-reference-book/`
  characters.
- [ ] **Ambiguous threads:** Ouroboros ring origin, the devil's
  endgame/identity, Vinny's post-Arc-7 fate — none confirmed, explained,
  or closed.

## 3. Canon Cross-Check

- [ ] Checked against `story-bible/foreshadowing-map.md` — does this
  story pay off a seed early, contradict one, or accidentally plant
  something that collides with an existing entry?
- [ ] Checked against `story-bible/plot-twist-inventory.md` — same
  question for twists specifically: does this story spoil, undercut, or
  duplicate a listed reveal?
- [ ] Checked against the relevant `story-bible/characters/`,
  `story-bible/villains/`, and `story-bible/plot-outline/arc-0N.md` files
  for the arc/characters involved — no invented canon that isn't flagged
  as new.
- [ ] If `canon_status: canon` (or heading there): the relevant
  `story-bible/` file(s) have actually been updated to match what the
  story establishes. A canon story that hasn't been folded back is a
  silent fork waiting to contradict something later.

## 4. Final Call

- [ ] Set `eval_status` in the story's frontmatter: `passed` (clean, or
  only Section 0/1 flags left as accepted exceptions), `flagged`
  (Section 2 or 3 issue found — needs a decision before this can be
  `canon_status: canon`), or leave `unreviewed` if this pass hasn't
  happened yet.
- [ ] If anything is flagged, add the `<!-- eval notes -->` comment block
  at the bottom of the story file per the instructions above.
