# Canon and Continuity Audit

Prepared by: Story Bible Keeper (read-only continuity pass). Date of audit: 2026-09-30.
Scope: every file under `story-bible/` (characters, villains, power-system, plot-outline incl. `opening.md`, `era-1-overview.md`, top-level canon files, `foreshadowing-map.md`, `plot-twist-inventory.md`, `open-questions.md`, `action-items-v5.1.md`) plus `writing-guide/story-laws.md`. I also skimmed `CLAUDE.md` (root), `TODO.md`, and the existing draft `stories/vector/arc-05/the-name-first.md` only to check canon claims. I did not audit `reference/`, `themes/`, or the rest of `writing-guide/`. No file was modified except this report.

Citation format: `path` § heading (or the bullet's bold label where the file has no sub-headings). Quotes are verbatim.

---

## Summary

### Counts by severity

| Section | BLOCKER | SHOULD-FIX | NOTE |
|---|---|---|---|
| 1. Contradictions (C-items) | 4 | 14 | 12 |
| 2. Story-law violations (V-items) | 1 | 5 | 3 |
| 3. Gaps that block drafting (G-items) | 6 | 13 | 3 |
| 5. Foreshadowing / twist integrity (S/P-items) | 0 | 7 | 7 |
| **Total** | **11** | **39** | **25** |

(Section 4 is a reconciliation table and carries no severities of its own; Section 6 is proposals.)

### The three most important things

1. **The Maya-erasure / father / identity cluster is self-contradicting (C1, C2, G4).** Five canon files say the honest father-son moment survives only on *Eli's* side; `era-1-overview.md` says it survives only on the *father's* side in two separate places. On top of that, the bible disagrees on the order of erasure, admission and Eli's discovery, and never says who retains the identity reveal. Arc 6 ("The Civilian", "The Admission", "Colombia") and Arc 7 ("The Conversation") cannot be drafted coherently until this is one ledger.
2. **The Iris reveal rests on a premise the bible contradicts (C3, C4).** `arc-00.md` puts Eli and Iris in the same 24-kid *class* of sixth-graders, yet `iris.md` and `arc-06.md` stage "shared Jersey City origin, same field trip, opposite rooms" as a late-night discovery, and `iris.md` has Iris recognizing Eli from a "Group 1 list" (Eli is Group 2) "years before Colombia," when the identity reveal that made Vector = Eli happened only in 2020 and the list is "filed and forgotten until Arc 6." The twist "Iris knew first" needs a mechanism.
3. **The story-laws hard constraint on minds is broken in the outline, and the drafting-critical names/premises are missing (V1, G1, G2).** `era-1-overview.md` says Eli cannot move a mind "categorically, not yet," which contradicts the law that this is a categorical boundary, not a gap. Separately, the thesis story "The Name First" and "Shockwave, Contained" both hinge on Eli saying Shockwave's real name aloud, and no canon file contains it; the mother, father and physics teacher are also unnamed and the father has no job, faith or first name in canon, which every Arc 1 story needs.

---

## 1. Contradictions

### BLOCKER

**C1. BLOCKER. Whose memory does Maya's erasure remove? (Eli's or the father's)**
- Says father lost it, Eli kept it: `story-bible/villains/maya-vale.md` § "After the turn": "removes a moment between Eli and his father --- the most honest exchange they'd ever had during the chaos --- from his father's memory. Eli's remains." Same in `story-bible/plot-outline/arc-06.md` bullet **Maya's erasure**: "erased from his father's memory. Eli's remains."; `story-bible/plot-outline/arc-07.md` bullet **Father conversation**: "a previous breakthrough exists only on Eli's side. He starts over from behind."; `story-bible/foreshadowing-map.md` row "Maya's erasure --- collateral damage": "exists only on Eli's side"; `story-bible/plot-twist-inventory.md` row "Maya erased more than the identity reveal": "exists only on Eli's side."
- Says the opposite: `story-bible/plot-outline/era-1-overview.md` § Arc 6 / "The Admission" / Resolution: "Maya's erasure takes it from Eli's side of the ledger and leaves it only on his father's, so Eli starts over from behind in Arc 7"; and § Arc 7 / "The Conversation" / Obstacles: "The previous breakthrough exists only on his father's side of the ledger; Eli has to earn it twice."
- What conflicts: which man remembers. "Starts over from behind" only follows if the father forgot and Eli remembers, so the two era-1 sentences are wrong on their own logic as well as against five other files.

**C2. BLOCKER. Order of events and what Eli and his father know when.**
- `story-bible/plot-outline/arc-06.md` bullet order: identity reveal, mother killed, **Maya's erasure** ("Eli figures out what she did"), then **Grief** ("The father admits he suspected"), then origin investigation, then Colombia.
- `story-bible/plot-outline/era-1-overview.md` § "The Admission" puts the admission *first* ("He admits he suspected... Then Maya's erasure takes it...").
- `story-bible/plot-outline/arc-07.md` bullet **Father conversation** places the admission in Arc 7: "The father's admission of suspicion here."
- `story-bible/power-system/physical-consequences-and-canon.md` § "Return to New York": "He left believing his identity was public knowledge. He returns to find people don't recognize him --- Maya's erasure held." That contradicts `story-bible/plot-outline/arc-06.md` bullet **Maya's erasure** ("Eli figures out what she did," placed before the origin investigation and Colombia) and `era-1-overview.md` § "The Admission" (the erasure follows the admission, before Arc 7).
- `story-bible/characters/eli-reyes.md` § "Eli's Personal World" (His father): "Arc 6: Finds out everything simultaneously, including that his wife knew. The admission..." — if the reveal is erased from "enough minds that the story dissolves" (`01-world.md` / `maya-vale.md`), the father cannot be grieving *with* knowledge of Vector after the erasure.
- What conflicts: (a) admission in Arc 6 or Arc 7 or both; (b) whether the admission happens before or after the erasure; (c) whether Eli learns the erasure held before or after Colombia; (d) whether the father retains the identity reveal at all.

**C3. BLOCKER. Eli and Iris were in the same class, but the bible stages their shared origin as a discovery.**
- `story-bible/plot-outline/arc-00.md` § "The trip": "24 sixth-graders. Liberty Science Center, Jersey City... The class splits into two groups of 12." `story-bible/01-world.md` § "The Accident": "24 sixth-grade students... Splits into two groups of 12." Same doc, § "Eli, at eleven": Eli "does not notice Vinny. Peripheral impression at most" (i.e., a classmate).
- `story-bible/characters/iris.md` § "Colombia": "Late night conversation reveals shared Jersey City origin, same field trip, opposite rooms." Same in `arc-06.md` bullet **Iris**.
- What conflicts: nothing says the 24 came from different schools. As written, Iris, Eli, Vinny, Cory and the reporter were one class, so "shared origin" is not news, and Eli would also know at 16 that Cory/Brick was his classmate (`arc-01.md` "Cory was never a mystery"). Either the 24 are multiple schools/classes (edit `arc-00.md`/`01-world.md`), or the Iris beat changes. Cross-ref G13.

**C4. BLOCKER. How and when Iris "knew first."**
- `story-bible/characters/iris.md` bullet **What Iris knew and when**: "She recognized Eli's name from the Group 1 list years before Colombia --- had been watching Vector's story from the outside." Also § "Her want and her need": "Why she'd been watching Vector for years before they met."
- Conflicts with: (a) `arc-00.md` § "The trip": Eli is Group 2, so his name is not on a "Group 1 list"; (b) `era-1-overview.md` § "One Scheduling Decision": "The list of who was in which room gets filed and forgotten until Arc 6," and § "The List": "There's no paper trail by design" — so Iris cannot have had the list "years before"; (c) the identity reveal that connects Vector to Eli happens in Arc 6 (2020) and is erased (`01-world.md`, `arc-06.md`), and Colombia is 2021-2022 (`era-1-overview.md` chronology and "Colombia"), so at most ~1 year, not "years"; (d) `01-world.md` § "The Reporter": "Eli finds the reporter's name on the Group 1 list... the same list where he finds Iris" — i.e., Eli sees Iris's name *before* meeting her, while `era-1` § "The List" says "he doesn't know it yet," which is implausible if she introduces herself by name; (e) the erasure "held" (`physical-consequences-and-canon.md`), so how Iris kept the Vector = Eli knowledge is not stated.
- What conflicts: the twist "Iris knew first" (`plot-twist-inventory.md`) has no consistent mechanism (which list, what name, when, why the erasure spared her).

### SHOULD-FIX

**C5. SHOULD-FIX. Colombia chronology: is Iris there first or does she "arrive" late?**
- `story-bible/power-system/physical-consequences-and-canon.md` § "Field Sensing": Weeks 1-4 "This is when the first hookup with Iris happens"; Weeks 5-12 "The period of drift into friendship with Iris"; Weeks 13-24 "Iris arrives during this period. The second hookup, the real conversation, the field trip revelation."
- `story-bible/characters/iris.md` § "Colombia": "The retreat is Iris's established sanctuary --- she has been several times... Eli arrives independently." She is present from the first hookup.
- Conflict: Iris cannot both be present for weeks 1-12 and "arrive" in weeks 13-24. (Also `arc-06.md` "he starts going because Iris is going" reads as Iris-first.)

**C6. SHOULD-FIX. Voss is placed in Arc 6 and Arc 7.**
- `story-bible/plot-outline/arc-06.md` last bullet: "Voss: field perception across entire city. Every device found by electrochemical signature. Killed simultaneously."
- `story-bible/villains/bill-voss.md`: "Arc: 7 (early villain)"; `arc-07.md` "EARLY: BILL M. VOSS"; `era-1-overview.md` § Arc 7 "Voss"; `power-system/onset-timeline.md` table: "Arc 7 (2023)".
- Also stage-lock: `power-system/arc-by-arc-power-progression.md` Arc 6 has field sensing at Stage 2/Stage 1; city-scale field perception is Stage 3 only in Arc 7. Violates the Timeline-discipline law in `writing-guide/story-laws.md`.

**C7. SHOULD-FIX. Maya's "intel about Vinny" is in Arc 7 and in Arc 9.**
- `story-bible/villains/maya-vale.md`: "**Later encounter (Arc 9):** ... She tells him something about Vinny she read in the city's mind during Arc 6. A human detail that reframes the final confrontation." The file's tags are `[villain, arc-6, arc-9]` (no arc-7).
- `story-bible/plot-outline/arc-07.md` bullet **Maya encounter (1 of 2)**: the same intel drop in Arc 7; `plot-outline/arc-09.md`: "Maya encounter (2 of 2 --- the real reunion; distinct from the brief Arc 7 intel-drop beat". `open-questions.md` § Resolved says this is settled. `maya-vale.md` was never updated.
- Secondary: `open-questions.md` § Resolved calls the Arc 7 beat "mid-confrontation"; `arc-07.md` places it in the early (Voss) block and `era-1-overview.md` "Maya, Briefly" says "Eli is about to face Vinny." Also, "the final confrontation" in `maya-vale.md` is the Arc 7 fight, so an Arc 9 intel drop cannot "reframe" it.

**C8. SHOULD-FIX. How did the cult leader die?**
- Blood/biology: `story-bible/plot-outline/arc-03.md` (Vinny bullet): "The cult leader's blood transfer attempt kills him --- his body cannot integrate Vinny's cellular byproducts."; `power-system/physical-consequences-and-canon.md` § "Blood transfer mechanism": "The cult leader's immune system treated it as catastrophic invasion"; `era-1-overview.md` § "The Inventory": "dies trying to absorb Vinny's blood"; `foreshadowing-map.md` row "Cult leader's blood transfer death".
- Magic: `story-bible/characters/vinny-black.md` bullet **Two separate axes**: "the cult leader died trying to hold a fraction of it [the magic]"; `power-system/onset-timeline.md` § "Vinny: two separate axes": "the cult leader died trying to hold a fraction of what Vinny holds."
- Conflict: cellular byproducts of the *regeneration* (biology axis) versus channelling *magic* (learned axis). It matters because the "two axes" rule is the newest canon and the map/arc-03 version treats the regenerative axis as the dangerous, transferable one.

**C9. SHOULD-FIX. What makes Vinny "structurally the most powerful being": the healing or the magic?**
- Healing as the source: `story-bible/plot-twist-inventory.md` row "Vinny was always the more powerful one": "His self-healing is an integration mechanism. By Arc 7 he is structurally the most powerful being in the story." `foreshadowing-map.md` row "Vinny was always the more powerful one": "Integration mechanism, not passive healing." `characters/vinny-black.md` bullet **Power --- the reframe**; `writing-guide/story-laws.md` § Power system, 6th bullet ("Vinny's self-healing is an integration mechanism...").
- Magic as the source: `power-system/onset-timeline.md` § "Vinny: two separate axes": "What actually makes him the most powerful being in the story is the magic"; `story-laws.md` 7th bullet: "the healing is the vessel, not the source"; `vinny-black.md` bullet **Two separate axes**.
- Secondary: `story-laws.md` says Eli is "physically capable of crossing" the molecular-rewrite ceiling, yet Vinny is "structurally the most powerful being in the story" with no stated yardstick (most powerful *in use*? *in reach*?). The two claims are only reconcilable if "structurally" is defined.

**C10. SHOULD-FIX. Whose POV is the Science Center fight?**
- `story-bible/00-story-identity.md` § "Narrative Voice" (Present tense breaks): lists "the science center moment in the final fight" among the overwhelmingly alive memories where the narrator is "briefly losing control of his own distance."
- `plot-outline/arc-07.md`: "Shown from Vinny's perspective throughout"; `era-1-overview.md` § "The Science Center": "Vinny Black (POV throughout)".
- Conflict: Eli-narrated present-tense break versus Vinny-omniscient POV. (Also `arc-07.md` puts "Present tense break" inside the Vinny-POV scene.)

**C11. SHOULD-FIX. "Chaos magic cannot touch Stage 3" versus a fight where nearly everything Eli has is Stage 3 and still fails.**
- `story-bible/power-system/power-progression.md`: "Vinny's chaos magic disrupts Stage 1 and Stage 2. Cannot touch Stage 3... The punch in the final fight is the most Stage 3 thing Eli does in the entire story. No power. Just a fist."
- `power-system/arc-by-arc-power-progression.md` Arc 7 has Stage 3: field sensing, self-healing, body system control, plus everything carried from Arcs 3-6 (push/pull, lifts, shields, subatomic deconstruction, motion freeze, electricity, molecular state change). `arc-07.md` Phase 3: "Direct grip fails against chaos magic. Elements deployed --- each showing enormous capability bouncing off." `plot-twist-inventory.md`: Eli's attacks land and are absorbed.
- Conflict/underspecification: by the rule, Eli's Stage 3 kit should function undisrupted, so "the punch is the most Stage 3 thing" is not distinctive, and the fight's failures must come from Vinny's absorption, not disruption. The two mechanisms (disruption vs absorption) are not separated anywhere.

**C12. SHOULD-FIX. When does Maya start acting through Simone?**
- `story-bible/plot-outline/arc-04.md`: "Simone (Shifter) introduced under Maya's mind control."; `villains/simone.md`: "Arcs: 4 (under mind control), 5 (freed)... Used as Maya's first proxy."; `arc-05.md`: Simone freed in Arc 5 (2018).
- `story-bible/plot-outline/arc-06.md` bullet **Maya Vale**: "city-wide chaos, mind-controls civilians including Simone as first proxy" (2020). `power-system/onset-timeline.md`: Maya "First public appearance Arc 6 (2020)".
- Conflict: Simone was Maya's proxy and freed two years before Maya's Arc 6 debut; "first proxy" in Arc 6 contradicts her being freed in Arc 5. Also `era-1-overview.md` § "Simone, Unresolved": "The actual antagonist is invisible," so Eli does not know Maya exists in Arc 4 (see C13).

**C13. SHOULD-FIX. The electromagnetic helmet: Arc 4 "Maya countermeasure" or Arc 6?**
- `story-bible/suit-evolution.md` Arc 4: "The electromagnetic helmet built as a Maya countermeasure is the most technically sophisticated thing he's made."
- `plot-outline/arc-06.md`: "Eli comes out in electromagnetic helmet"; `arc-by-arc-power-progression.md` Arc 6 Stage 1: "psychic beam detection, electromagnetic neural shielding"; `suit-evolution.md` Arc 7: "Helmet gone except for electromagnetic shielding needs."
- Conflict: in Arc 4 Eli cannot know Maya (C12); shielding as a Stage 1 power only starts in Arc 6; and `suit-evolution.md` Arc 6 says "Less armor" (post-retreat), but the Maya fight (helmet) precedes the retreat.

**C14. SHOULD-FIX. When does the name "Vector" circulate publicly?**
- `story-bible/characters/eli-reyes.md` bullet **Hero name**: "Begins circulating publicly in Arc 2."
- `story-bible/suit-evolution.md` Arc 3: "Vector starts being photographed. The name begins circulating publicly."

**C15. SHOULD-FIX. When does Eli start to look younger?**
- `characters/eli-reyes.md` **Age**: "Looks 2-3 years younger from Arc 6 onward due to body control slowing aging."
- `power-system/abilities-environmental-effects.md`, row Body System Control / Self-Healing: "Aging slowing becomes notable by Arc 7." `arc-by-arc-power-progression.md`: body system control is Stage 1 in Arc 6, Stage 3 only in Arc 7.

**C16. SHOULD-FIX. `arc-by-arc-power-progression.md` contradicts itself in Arc 6 and drops abilities.**
- Arc 6: "Stage 2: matter creation, field sensing. Stage 1: field sensing, self-healing, ..." — field sensing is listed at Stage 2 and Stage 1 in the same arc.
- Arc 7 keeps matter creation at Stage 2 (no graduation), element bending vanishes after Arc 4, "targeted motion freeze" (Arc 4 Stage 1) has no Stage 2/3 step, and flight (`abilities-environmental-effects.md` row Flight; "crude flight" Arc 1 in `arc-01.md`) is never tracked again though `arc-06.md` has "Meteor... first time in space by choice." Because story-laws makes stages arc-locked, writers will guess.

**C17. SHOULD-FIX. The onset rule contradicts its own table, and "nearly last" is wrong.**
- `story-bible/power-system/onset-timeline.md` § The rule: "Onset latency scales with the power's ceiling"; § Timeline note: "Once latency passes roughly five years you're in tier-broken territory."
- Table: Bill Voss (High, INFORMATION, not BROKEN) and the Bio-Control Kid (High) at ~5.5 yrs, later than Eli (BROKEN, ~4.5) and Twitch (BROKEN, ~5); Simone (Mid-high) ties Eli at ~4.5; Vinny (Low-mid) ties Shockwave (Mid) at ~3.5. `arc-00.md` § "Aftermath": "the tier-broken powers last of all" — but the two last-tied are not tier-broken.
- `story-bible/01-world.md` § "The delay": "Eli, at 16, is nearly last." Per the table four of twelve arrive after him, and one ties.

**C18. SHOULD-FIX. Residency: timing and pipeline.**
- `story-bible/eli-character-arc.md` Phase 3 (Arcs 4-5, Age 22): "Surgical residency as both processing and avoidance simultaneously."; `arc-05.md` Aftermath: "Surgical residency begins."; `era-1-overview.md` § Arc 6 "Residency": "Eli Reyes — 2019"; `arc-06.md` opens with the residency.
- `characters/eli-reyes.md` **Education & Career**: "Physics major... Enters surgical residency after graduation." Graduation is May 2018 (`era-1-overview.md` chronology, Arc 5 "Graduation"); residency requires a medical degree; no canon file accounts for one. Residency also spans Colombia (4-6 months) and 2020-2023 with no leave stated.

### NOTE

- **C19. NOTE.** Confidence timing: `characters/eli-reyes.md` **After first fight**: "Natural confidence emerges rapidly. Talking louder, downward tonality, piercing eye contact" (Arc 1, Nov 2012) vs `arc-03.md`: "speaking louder... Irish goodbye personality established" (Arc 3) vs `eli-reyes.md` "Visibly more muscular and physically confident from Arc 3 onward." Also `open-questions.md` "Recommended Writing Order" #4 puts "friends who accept the Irish goodbye" in the Arc 1 normal world.
- **C20. NOTE.** `characters/eli-reyes.md` "Mind and voice as a teenager (Arcs 1-4, roughly ages 16-21)": Arc 4 is age 21-22 (`era-1-overview.md` chronology: "21→22"), not 21.
- **C21. NOTE.** `story-bible/01-world.md` § "Society's Response": "Arc 4 (Age 22): Twitch first full appearance. Shifter." Twitch is speed; Simone is the Shifter (`villains/twitch.md`, `villains/simone.md`).
- **C22. NOTE.** Vinny's regeneration onset is 2011 (`onset-timeline.md` table, `vinny-black.md`) but `era-1-overview.md` § "Relief" is "2012" and "Vinny discovers he heals." Reconcilable as discovery lag; not stated.
- **C23. NOTE.** `characters/vinny-black.md` bullet **Arc** lists "cult massacre (Arc 3) → first appearance vs Eli, loses (Arc 2)": the arrows run out of chronological order.
- **C24. NOTE.** `arc-05.md`: "Earthquake rescue (Arc 5 or early 6)" vs `foreshadowing-map.md` / `era-1-overview.md` (Arc 5, 11/2018).
- **C25. NOTE.** `moral-framework.md` § "Era 2": "Open: whether the planet's culture has *no* moral framework at all, or a different, unfamiliar one" vs `arc-08.md` first bullet ("the planet has no equivalent") and `action-items-v5.1.md` item 3 ("the planet lacks Earth's ambient moral framework"). "No equivalent" and "none" are not the same; the phrasing invites a writer to pick "none."
- **C26. NOTE.** `story-bible/suit-evolution.md`: the six-step ladder "Absurd → Earnest → Impressive → Iconic → Simplified → Symbolic" is mapped onto seven arcs, and the Arc 6 line says "This version becomes iconic" although "Iconic" precedes "Simplified" in the ladder; Arc 5 has no suit description at all (only "Was partly about anonymity").
- **C27. NOTE.** `action-items-v5.1.md` closes with "Story Bible v5.0 | Confidential" though titled v5.1. `open-questions.md` § "Recommended Writing Order" is stale against `arc-00.md`/`era-1-overview.md`: #5 lists "field trip day, Ouroboros ring" as Vinny's "Arc 1 scenes" though these moved to Arc 0; #3 places the mother conversation with the first manifestation, while `era-1-overview.md` puts it in Oct 2012 after the refusal; and `era-1-overview.md` § "This is a map, not a queue" says "Writing starts at Arc 1" and "write in whatever order you're actually excited about."
- **C28. NOTE.** Ages of Group 2 villains are never stated. All twelve are Eli's classmates (±1 yr), so Shockwave in Arc 2 (2013) is ~17-18 and Tide in 2016 ~20, yet `era-1-overview.md` § "Shockwave, Contained" says "A man is taking blocks apart" and the story draft gives him "a job."
- **C29. NOTE.** Jean Grey homage: `00-story-identity.md` assigns it to "Eli's early involuntary emotional surge"; `arc-07.md` Phase 5 assigns "Jean Grey homage" to Vinny reaching into the well. Not a contradiction if intended, but no file says it is deliberate double use.
- **C30. NOTE.** `plot-outline/CLAUDE.md` says the outline is "one file per arc (`opening.md`, `arc-01.md` … `arc-09.md`)" and omits `arc-00.md`; `opening.md` and the "The Opening" section of `era-1-overview.md` overlap (see S/P section for the substantive difference).

---

## 2. Story-law violations

**V1. BLOCKER. Eli "cannot move a mind... not yet."**
- Law: `writing-guide/story-laws.md` § Power system, 2nd bullet: "This isn't a gap he might one day close through comprehension — it's a categorical boundary of what the power *is*."
- Violation: `story-bible/plot-outline/era-1-overview.md` § Arc 6 / "Maya" / Obstacles: "Eli cannot move a mind — categorically, not yet (see `story-laws.md`)." "Not yet" implies a future capability, the exact thing the law forbids, and the line cites the law it contradicts. Any Maya story drafted from this will inherit the error.

**V2. SHOULD-FIX. Confirming the ring's origin.**
- Law: `story-laws.md` § Ambiguous threads: "The origin of Vinny's Ouroboros ring (never confirmed — implication only)."
- Violation: `story-bible/plot-twist-inventory.md` row title "The Ouroboros ring was placed" asserts placement as a fact in the heading (the body says "Never confirmed"). Also `foreshadowing-map.md` row "Ouroboros ring": "The implication is available" is fine; only the inventory heading confirms.

**V3. SHOULD-FIX. Calling Vinny invincible or unkillable.**
- Law: `story-laws.md` § Power system, 6th bullet: "Avoid flatly calling him 'invincible'... true invincibility (literally unkillable) hasn't been decided."
- Violations: `story-bible/characters/vinny-black.md` **Appearance**: "his self-healing making him effectively unkillable in a fight"; `story-bible/characters/eli-reyes.md` bullet **How the world reads him**: "invincible-reading via his healing." These are not prose, but they are the source a writer copies from. They also feed the exact conflation `story-laws.md` 7th bullet warns against (healing as the source of power).
- Also the law is internally in tension: 6th bullet credits the healing with making him "structurally the most powerful"; 7th bullet says the healing "never reaches BROKEN tier." See C9.

**V4. SHOULD-FIX. Moral labels on characters in the canon files.**
- Law: `story-laws.md` § Characterization: "No character is narrated as objectively good or evil... present competing philosophies, not verdicts."
- Instances that instruct narration with a verdict: `villains/joel-mara.md` "Good/neutral"; `villains/maya-vale.md` "turns good"; `villains/simone.md` "Good at her core"; `villains/tide.md` "Not evil --- cornered by registration pressure. Victim of inadequate policy."; `villains/brick.md` "**Always a bully.**" (partially behavioral). `00-story-identity.md` Core Themes and `eli-character-arc.md` Phase 5 ("Fighting evil because it's right") are fine only if kept as Eli's read. Fix is to relabel as Eli's read or as observable behaviour.

**V5. SHOULD-FIX. Confronting the moral framework in Era 1.**
- Law: `story-laws.md` § Timeline discipline: "Earth-set material (Arcs 1–7) must treat it as ambient, unexplained texture — never confronted, argued for, or rationalized on the page."
- Risk: `moral-framework.md` defines the framework partly as "presence/gratitude/non-attachment as practiced disciplines," while `arc-06.md` makes meditation the retreat's "bread-and-butter" ("Slowly understands its significance"), `eli-character-arc.md` Phase 4 makes "First successful meditation" the defining moment, and `foreshadowing-map.md` row "Colombia retreat" makes the retreat structurally central. Nothing says the Colombia practice is *not* the framework. If it is, Arc 6 confronts it early; if it isn't, the boundary is unstated.

**V6. SHOULD-FIX. "Never write it as something he can't do."**
- Law: `story-laws.md` 3rd Power bullet (the playing-god ceiling is "a standing refusal, not a limitation").
- Tension: `villains/shockwave.md` Arc 5 labels restructuring "**First glimpse of playing god ceiling:** He could have restructured rather than destroyed"; `plot-outline/arc-05.md`: "the knowledge of what he could have done instead came one fight too late"; `plot-outline/arc-09.md`: "Arc 5 he chose death because he didn't yet know another way." That is a knowledge failure (consistent with knowledge-dependency), not a refusal, yet it is labelled as the playing-god ceiling. Either restructuring is *not* the ceiling (then relabel), or the Arc 5 failure reads as "couldn't" (law breach).

**V7. NOTE. Vinny's single "Joker crack."**
- Law: `story-laws.md` § Character consistency: "exactly one 'Joker crack'... a laugh that arrives wrong."
- `characters/vinny-black.md` **Psychological register**: "A laugh that arrives in wrong moments" (plural), and `arc-04.md` horror note suggests "a laugh that sounds almost right" in Arc 4 as an option. No file assigns the one crack to one scene.

**V8. NOTE. Vinny as tempter.**
- Law: `story-laws.md`: "Vinny needling, testing, or delighting in how close he gets is in-bounds and expected." `arc-07.md` calls the science-center exchange "the only real dialogue," and no arc file gives Vinny a needling beat with Eli in Arcs 2-6 (Arc 2 is a silent fight, Arc 5 has no Vinny-Eli contact on the page). See G15.

**V9. NOTE. Body System Control and "his own emotion."**
- Law: `story-laws.md` 2nd Power bullet: no ability "to touch emotion or belief, his own or anyone else's."
- `abilities-environmental-effects.md` "Body System Control... Direct regulation of autonomic nervous system" and `power-progression.md` "Emotion is now fuel not interference" sit close to that line. Not a violation as written, but no file states that self-regulation of physiology stops short of emotion.

---

## 3. Gaps that block drafting

Ordered by how soon they bite. "Next story" is read as Arc 1 / the Opening rewrite because `era-1-overview.md` § "This is a map, not a queue" says "Writing starts at Arc 1" and `CLAUDE.md` flags `the-name-first.md` for rewrite.

**G1. BLOCKER. Names the current slate cannot proceed without.**
- Shockwave's real name — `story-bible/villains/shockwave.md` has none. "The Name First" (`era-1-overview.md` § Opening; `arc-05.md`: "He says Shockwave's real name. One sentence.") and `opening.md` ("I knew his name") both require it. The Arc 2 story "Shockwave, Contained" needs it as well ("Eli has to find him"). The existing draft dodges it ("I know his name").
- Eli's mother's first name — `characters/eli-reyes.md` "Name TBD"; `open-questions.md`; `action-items-v5.1.md` item 4.1. She appears in "Sixteen", "One Step at a Time", "The Verdict", "The Civilian" (`era-1-overview.md`).
- Eli's father: no first name, occupation, faith, or origin in any canon file, though he is on the page in Arc 1, 5, 6, 7 (`eli-reyes.md` describes only his function). The draft already invents "his father's shop" and a "parish priest"; canon says nothing on either. Home/family specifics (siblings or none, faith, national origin of a "Latino-American" family) belong in `characters/eli-reyes.md`.
- Physics teacher name (`characters/physics-teacher.md` "TBD"), reporter (`01-world.md` unnamed; `action-items-v5.1.md` 4.4), cult leader, Vinny's mother, and every Group 2 villain except Cory, Marcus Webb, Maya Vale, Joel Mara, Bill Voss, Simone, Danny Reeves (Twitch, Shockwave, the Bio-Control Kid, the cult) have no real names. Only the first two bullets are drafting-blocking; the rest are SHOULD-FIX.

**G2. BLOCKER (for that story). "Eighteen" (Arc 2).**
- `era-1-overview.md` § Arc 2 "Eighteen": "**[GAP]** — ... what earns it was never specified." `arc-02.md` closes on "18th birthday as arc's closing beat --- earned rather than given" with no content. The candidate ("no longer needs the man's verdict") is a suggestion, not canon. Also listed only in era-1 Open Gaps #4, in neither queue (Section 4).

**G3. SHOULD-FIX. The "Eli tells his mother" scene has no slot, and when she knows is ambiguous.**
- `arc-01.md` § "The arrival": "He tells his mother. The relief of being known." `eli-reyes-journey-worksheet.md` per-phase table (Phase 1 resolution): "Tells his mother." But `era-1-overview.md` Arc 1 has no story for it; "Sixteen" ends with her "catches his eye... says nothing," and "One Step at a Time" says "She finds out what he's been sitting on" (`arc-01.md`: that he can do something about Brick and decided not to). Whether she knew from March, from the telling, or from the refusal is unspecified.

**G4. BLOCKER. Identity-knowledge ledger and the mother's killer (blocks "The Civilian", "The Admission", "The Conversation", Colombia).**
- No file states, after the erasure, who remembers Eli = Vector: father, friends, the physics teacher, the reporter (`01-world.md`: "The reporter's notes survive Maya's erasure"), Iris, the killer, the police. See C1, C2, C4.
- `arc-06.md`: mother "killed by random civilian who saw the news"; `era-1-overview.md` "The Civilian": "Not mind-controlled. Not part of any plan." Nothing says who the killer is, whether the erasure reaches him, whether he is caught, or what Eli does. This is the sharpest possible test of the law `story-laws.md`: "He will not kill an unpowered person, whatever they believe about him" (a "live, tested restraint") — and the bible has no scene that tests it (see G16). `eli-reyes.md` says only that some religious characters read Vector as the devil; nothing links the killer to that.

**G5. BLOCKER (for "The List"). Paper trail becomes public: mechanism unspecified.**
- `era-1-overview.md` § "The List": "**[GAP]** the mechanics of how the paper trail becomes public aren't specified." Also unspecified: reporter–Eli contact (`01-world.md` says "should not be adversarial"; no arc file has the scene), and the reporter's beats between the Arc 2 byline and Arc 6 that `01-world.md` promises (hearing question, investigative piece); none appears in `arc-02.md`-`arc-05.md` or the era-1 slate. The erasure's effect on the national reckoning (is it erased too?) is not stated.

**G6. SHOULD-FIX (BLOCKER for Colombia/Iris stories, via C3/C4). `characters/iris.md` (`status:` flag).**
- Frontmatter: "want/need settled; still needs her Arcs 3–5 offscreen activity and one independent scene per arc from Arc 6."
- Concretely unresolved: (1) the vocation: `iris.md` "**[GAP]** the specific vocation — documentarian, oral historian, translator, nurse — is still open"; (2) what she does in Arcs 3-5 (the file says "she's building the project, and it isn't going well in the way that matters," but names no event, place, or person); (3) independent scenes for Arcs 6, 7, 8 and 9: only Arc 6 has any (`era-1-overview.md` "Colombia," "Iris's side of this story"); Arc 8 (Eli gone for years) is the obvious slot and is empty; (4) the Arc 7 "time conversation" (`iris.md`) has no scene in `arc-07.md` or `era-1-overview.md`; (5) how she funds retreats, her father's name/status, how she knew Vector = Eli (C4); (6) Arc 0 "One Scheduling Decision" needs Iris and the reporter at 11 (`arc-00.md`: "Whether either gets on-page presence in Arc 0... is open").
- Depends on it: the Colombia story, the twist "Iris knew first," `action-items-v5.1.md` item 1, the reporter link (item 4.4), and Arc 9's reunion.

**G7. BLOCKER (for any Arc 8 story). `plot-outline/arc-08.md` (`status: least developed`).**
- Unresolved (`action-items-v5.1.md` item 3 and `open-questions.md`): planet physics; culture (none vs a competing framework, C25); who the supers are and their powers; why they come from "a similar field trip accident" (does this imply a parallel Earth, and how does that square with "planet"/"alternate reality" in `arc-07.md` and "home reality" in `arc-09.md`?); duration ("years" in `arc-09.md`) and Eli's age; language; what he builds ("clear new beginning"); who "the girl from the other world" is (`open-questions.md`); how the return works given the knowledge-dependency law. Also the Earth-chapter ending ("Nail the Earth-chapter ending," item 3) is largely answered by `arc-07.md` Phase 5, so item 3's first bullet is stale (Section 4).
- Depends on it: Arc 9, the playing-god ladder (item 2), Iris's independent scenes (G6), and the "Colombia → Arc 8" callback in `foreshadowing-map.md`.

**G8. BLOCKER (for any Arc 9 story). `plot-outline/arc-09.md`.**
- The final battle has no antagonist, stakes, or place ("Eli's full integrated power at scale"); `arc-09.md` says "Eli's world in bad shape" with no account of what happened in his years away; whether Vinny appears is an open decision that `story-laws.md` says not to resolve; "the killing threshold" situation is undefined; Joel and Simone's roles are one line each.

**G9. SHOULD-FIX. Vinny's track between Arc 5 and Arc 7 has no beats, but later canon depends on it.**
- `arc-06.md` has no Vinny content; `vinny-black.md` says "devil's influence accelerates (Arc 6)"; `maya-vale.md` says Maya "read [something about Vinny] in the city's mind during Arc 6." So Vinny must be in the city and identifiable in Arc 6, and there is no seed.
- `arc-05.md` "Vinny second appearance: stone destroyed," `vinny-black.md` "short-term time travel, chaos magic, stone destroyed (Arc 5)": none appears in the `era-1-overview.md` Arc 5 slate; who destroys the stone, what Vinny and Eli do at "the fight," and Vinny's motive for moving Brick's strength to Shockwave are unstated.
- Also unplaced: the ring moving from necklace to finger (`vinny-black.md`), the "one Joker crack" (V7), the science-center line (`open-questions.md`), and the cult brand (`open-questions.md`).

**G10. SHOULD-FIX. `suit-evolution.md` (`status:` flag): which suit, which color, when.**
- Open per the file: "the exact arc where each transition happens, and what in-story event motivates each one." Concretely: only two data points exist (Arc 1 drab; Arc 7 resolved, "tentatively"). A writer of any Arc 2-6 story cannot pick a color state or trigger; Arc 5 has no suit description; the helmet timeline conflicts (C13); and `story-laws.md` requires the suit to reflect "his relationship to vulnerability at that point in time." Depends on: Arc 2 (Earnest), Arc 3, Arc 5 (anonymity), Arc 6 (post-retreat iconic) stories, and `foreshadowing-map.md` row "The suit."

**G11. SHOULD-FIX. `plot-outline/era-1-overview.md` (`status: draft`): dependency risk.**
- Everything in it is "pending author agreement," yet the root `CLAUDE.md` tells writers to start there for Arcs 1-7. Its chronology is "invented scaffolding" (§ Placeholder chronology), while `onset-timeline.md` (all onset dates), the story draft ("a Tuesday in March"), and every age in the bible are computed from it; "Eli born March 1996" appears only there. If any date moves, the onset table cascades.
- Its internal errors (C1 x2, V1) show why it should not be treated as canon yet. It also omits stories for beats present in the arc files: Simone freed / Brick's death / Shockwave transformation (Arc 5), Joel Mara persuasion (Arc 6), the meteor (Arc 6/7), the Iris time conversation (Arc 7), Vinny's Arc 6, and the physics-teacher Arc 5 conversation.

**G12. SHOULD-FIX. Brick's containment and the facility.**
- `arc-01.md` "Brick, resolved" says how he loses but not what happens to him; yet he "dies in his cell in Arc 5" (`brick.md`, `arc-05.md`). `01-world.md` puts an "Inadequate containment facility" in Arc 2. How a Hulk-tier Brick was held for six years in a facility Eli calls inadequate (`era-1-overview.md` "Shockwave, Contained") is unexplained, as is who runs it. `open-questions.md` "Government recurring characters" is the related open item.

**G13. SHOULD-FIX. Group 2 schooling, ages and acquaintance.**
- Which of the twelve Eli knew as classmates, and whether he recognizes Cory, Vinny, Shockwave, etc. as former classmates in Arcs 1-5, is unstated (C3, C28). `01-world.md` delays the pattern until "Arc 6: Eli pieces this together," which requires him not to notice the connection for four years.

**G14. SHOULD-FIX. Playing-god ladder (`action-items-v5.1.md` item 2).**
- Present: Arc 5 (`shockwave.md`), Arc 6 (`arc-06.md`: "could rewrite the accident's effects at a cellular level. Won't."), Arc 9 (`arc-09.md`). Absent: any rung in Arcs 2, 3, 4, 7 or 8; no instance where "restraint visibly cost him something" is designed.

**G15. SHOULD-FIX. Tempter beats.**
- `story-laws.md` says the Eli/Vinny dynamic is Batman/Joker with Vinny "pushing for the moment Eli breaks." The bible has Eli-Vinny contact in Arc 2, (unclear) Arc 5, and Arc 7 only. Arcs 3-4 have Vinny explicitly absent or omniscient-only.

**G16. SHOULD-FIX. The religious "devil" reading is never seeded.**
- `story-laws.md` § Power system (4th bullet) and `characters/eli-reyes.md` treat it as "a real, standing public perception," but no arc file (`arc-01.md`-`arc-09.md`) or era-1 story contains a scene where it appears or is tested.

**G17. SHOULD-FIX. Moral framework has no lexicon.**
- `moral-framework.md` (`status: shape decided, name and specific text still open`) requires it to be visible as "a phrase used in passing... small worn symbols or gestures" in Era 1 without explanation, but supplies none. Every writer will invent phrases and symbols, and each invention becomes accidental canon. A short shared lexicon (three phrases, two gestures, one symbol) is needed before Arc 1 drafting.

**G18. SHOULD-FIX. Vinny's magic system and the Arc 7 exile.**
- The bible uses "time magic" (`arc-07.md`), "chaos magic" (`power-progression.md`), and "chaotic dimensional magic" (`arc-07.md`) for what may be one thing; only time-jump rules are given. The step that sends Eli to another planet in an "alternate reality" is not seeded in any earlier arc (map row "Twitch's time dilation" covers time only).

**G19. SHOULD-FIX. What the world knows when Eli disappears (Arc 7 to Arc 9).**
- Arc 7 ends with Eli alone on another planet; `arc-09.md` returns him "after years away" to a "world in bad shape." Nothing says what his father, Iris, the public, the government, or the (erased) history believes happened to him; Iris's Arc 8 life is the obvious place to show it (G6).

**G20. NOTE. Flight and space.** `arc-06.md` "Meteor... first time in space by choice" and the Arc 7 moon phase need flight, shielding and life-support logic; the abilities table lists Flight, but `arc-by-arc-power-progression.md` never tracks it after Arc 1 (C16).

**G21. NOTE. Per-villain wants.** `action-items-v5.1.md` 4.7 covers this; Tide's open thread is intentionally open (`era-1-overview.md` § Open Gaps #7).

**G22. NOTE. `story-bible/characters/physics-teacher.md`** has no Arc 1 scene despite the map claiming "Nothing is perfect" is planted then, and no statement of whether he knows Eli is Vector at the Arc 5 "oblique conversation" (`arc-05.md`).

---

## 4. Open-questions vs action-items reconciliation

Key: **OQ** = `story-bible/open-questions.md`; **AI** = `story-bible/action-items-v5.1.md`; **Still open?** is my judgement after reading the whole bible. Per `story-bible/CLAUDE.md`, AI is "more current," but three of the OQ items below are drafting-blocking and sit low in AI.

| # | Item | Appears in | Still open? / answered where | Do the queues disagree on priority? |
|---|---|---|---|---|
| 1 | Physics teacher's name | OQ "Decisions Still Needed"; OQ Writing Order #6; AI 4.5; `characters/physics-teacher.md` ("TBD") | Open. Not answered anywhere. | Yes. OQ wants it by writing the scene (early); AI ranks him 5th of 8 in a QUEUED-ongoing item that is last of four. |
| 2 | Mother's first name and her own want | OQ "Mother's first name"; AI 4.1 ("most urgent by a distance"); `eli-reyes.md` ("Name TBD") | Open. Her function is fully specified (`arc-01.md`, `eli-reyes.md`); name and want are not. | Yes. AI calls it "most urgent" but inside item 4 (4th of 4, QUEUED); OQ lists it unranked. She is in at least four Arc 1-6 stories ("Sixteen", "One Step at a Time", "The Verdict", "The Civilian"), so she blocks more drafting than AI items 1-3. |
| 3 | Father's full arc / what he wants for himself | OQ "Father's full character arc"; AI 4.2 | Partly answered: arc direction in `eli-reyes.md` § "Eli's Personal World" (His father) and `era-1-overview.md` "The Verdict/The Admission/The Conversation." Open: his own want, name, job, faith. | Mild. OQ says "direction established"; AI treats it as a full want-need job. |
| 4 | Sol's exit line | OQ; `era-1-overview.md` Open Gaps #5 ("deliberately deferred"); not in AI | Open by design (arrives in the writing). Not a blocker. | AI omits it (fine). |
| 5 | Science center dialogue | OQ; `arc-07.md` ("the only real dialogue"); `foreshadowing-map.md` row "Vinny sees Eli as rival brother" | Shape given by OQ ("acknowledgment of shared loss..."); content open. Note `arc-07.md` horror note says "Do not explain what was said," which OQ's "shape" partly does. | AI omits it. |
| 6 | Vinny's cult brand | OQ; `vinny-black.md`, `arc-02.md` (brand referenced, undefined) | Open. | AI omits it. |
| 7 | Simone after Arc 5 | OQ; `villains/simone.md` ("Eli knows where she goes and respects it"); AI 4.7 | Open (where and what life). | AI lumps it into the roster item. |
| 8 | Government recurring characters | OQ; `01-world.md` (hearings, registration) | Open. Related to Brick/facility gap G12. | AI omits it. |
| 9 | Arc 8 planet specifics (physics, supers) | OQ; AI 3; `arc-08.md` (`status: least developed`); `moral-framework.md` Era 2 | Open. Partly answered: moral lesson, mentor arc, "physics humbles" (`arc-08.md`). | AI ranks it 3rd (heaviest lift, last on purpose); OQ unranked. No conflict. |
| 10 | The girl from the other world | OQ; `arc-08.md` (Eli "stays loyal"); `arc-09.md` ("introduced --- handled as adult, normal") | Open (who/power). Answered: he does not cross the loyalty line (`arc-08.md`). Note `arc-09.md` implies she comes to Earth. | AI omits her (item 3 "supers as real characters" covers her implicitly). |
| 11 | Vinny's whereabouts after Arc 7 | OQ ("Decisions Still Needed"); `story-laws.md` § Ambiguous threads ("Vinny's whereabouts and fate after his Arc 7 disappearance"); `arc-09.md` ("Vinny's legacy") | Deliberately open by law. | **Yes, in status:** OQ frames it as a decision to make; `story-laws.md` says do not resolve. Only the narrow "does he appear in Arc 9?" is a real decision. |
| 12 | Devil's endgame | OQ; `story-laws.md` § Ambiguous threads ("purely atmospheric — never face-to-face") | Deliberately open by law. | **Yes, same conflict as #11.** |
| 13 | Maya encounter timing | OQ § Resolved; `arc-07.md`; `arc-09.md` | Answered in OQ, but `villains/maya-vale.md` was not updated (C7); "mid-confrontation" wording conflicts with `arc-07.md`. | Not a priority conflict; a stale-file issue. AI 4.3 lists Maya's want as open. |
| 14 | Recommended writing order | OQ; `era-1-overview.md` § "This is a map, not a queue" | Superseded: `era-1-overview.md` says start at Arc 1 in any order; OQ list predates the Arc 0 split (C27). | **Yes.** OQ puts Arc 6 planning last (#8) while AI item 1 (Iris, Arc 6) is first. Different bases (writing vs development), but not stated. |
| 15 | Format decision | OQ | Answered (novel first, `00-story-identity.md` § Format). | No. |
| 16 | Iris independent want | AI 1; `iris.md`; `era-1-overview.md` Open Gaps #1 | Want/need/goal DONE; vocation still open (`iris.md` [GAP]); offscreen Arcs 3-5 and per-arc scenes open. | AI 1 is "IN PROGRESS," but its first sub-bullet is DONE; `era-1-overview.md` strikes the whole gap. OQ omits Iris entirely. |
| 17 | Iris offscreen Arcs 3-5 | AI 1 bullet 2; `iris.md` `status:` | Open (see G6). | -- |
| 18 | One Iris scene per arc from Arc 6 | AI 1 bullet 3; `iris.md` `status:` | Open; only Arc 6 has a slot. | -- |
| 19 | Playing-god escalation ladder | AI 2 | Open; rungs exist only at Arcs 5, 6, 9 (G14). | AI 2 is second; `arc-09.md` already sets part of the "final-arc test." |
| 20 | Earth-chapter ending | AI 3 bullet 1 | Largely answered: `arc-07.md` Phase 5, `era-1-overview.md` "The Science Center," `eli-character-arc.md` Phase 5. | AI treats it as open; stale. |
| 21 | Planet world logic | AI 3 bullet 2 | Open. | -- |
| 22 | Arc 8 unique lesson | AI 3 bullet 3; `moral-framework.md` | Shape answered; "none vs competing framework" open (C25). | AI says "Shape now settled"; `moral-framework.md` agrees. |
| 23 | Arc 8 supers as real characters | AI 3 bullet 4; OQ #9 | Open. | -- |
| 24 | Arc 8 clear new beginning | AI 3 bullet 5 | Open. | -- |
| 25 | Secondary wants: Maya | AI 4.3 | Partly answered: condition and shame motive in `maya-vale.md`; her want beyond function open. | OQ's "Resolved" Maya item is about timing only. |
| 26 | Secondary wants: reporter (and name) | AI 4.4; `01-world.md` | Open; unnamed. | OQ omits the reporter. |
| 27 | Secondary wants: Vinny's mother | AI 4.6; `arc-03.md` (careless-and-true line) | Open; unnamed. | OQ omits. |
| 28 | Secondary wants: villains | AI 4.7 | Partly answered per villain (Shockwave, Tide, Simone, Joel). Most lack a want beyond "be stopped." | -- |
| 29 | Secondary wants: Jade and Sol | AI 4.8 | Open. | -- |
| 30 | **Not in either queue** | -- | (a) "Eighteen" (`era-1-overview.md` #4); (b) how the paper trail becomes public (`era-1-overview.md` #6); (c) Brick's relation to the accident (`brick.md`, `arc-00.md`, `onset-timeline.md` Open, `era-1-overview.md` #2); (d) suit color transitions (`suit-evolution.md`); (e) moral-framework name/text (`moral-framework.md`); (f) Iris vocation; (g) Shockwave's real name; (h) erasure/identity ledger (C1-C4, G4); (i) residency pipeline (C18); (j) Vinny Arc 5-6 gap (G9); (k) killer of Eli's mother (G4). | The two queues collectively omit the items that block Arc 1-6 drafting most. |

Summary of disagreements: (1) the drafting-blocking names (mother, physics teacher) are last-priority in AI but early-priority in OQ's writing order; (2) OQ and `story-laws.md` disagree on whether Vinny's fate and the devil are decisions or deliberately closed; (3) AI item 3's first bullet is answered elsewhere; (4) AI 1 is marked IN PROGRESS but has a completed first sub-bullet; (5) OQ's "Recommended Writing Order" has not been updated since the Arc 0 split.

---

## 5. Foreshadowing and twist integrity

### Seeded, no home or no payoff

- **S1. SHOULD-FIX. "Father always suspected"** (`foreshadowing-map.md` "Arc 3/4 (invisible)" → Arc 6; `plot-twist-inventory.md` "3/4 (invisible) → 6"). `arc-03.md`, `arc-04.md` and the Arc 3-4 era-1 stories contain no father beat; his first on-page appearance is Arc 5 ("The Verdict"). Also `eli-reyes.md` says the father noticed "the sudden confidence, the deepened absence" after the first fight, i.e., Arc 1-3.
- **S2. SHOULD-FIX. "Nothing is perfect"** (map: planted Arc 1, pays "All arcs, final statement... in the Vinny ending"). `arc-01.md` and era-1 Arc 1 contain no physics-teacher scene; `arc-07.md` and era-1 Arc 7 contain none either. The first place the line is used in any outline is Arc 5 ("Physics teacher's oblique conversation"). Both the plant and the payoff lack a beat.
- **S3. SHOULD-FIX. "Vinny sees Eli as rival brother"** (map: Arc 2 → Arc 7 science center). `arc-02.md` and era-1 Arc 2 ("Not a Priority", "Preparation, Not Talent") show the "preparation vs talent" reframe but not the rival-brother framing; it lives only in `vinny-black.md` § "What Vinny wants."
- **S4. SHOULD-FIX. Reporter thread** (map: byline Arc 2/3 → Arc 6; `01-world.md`: returns "periodically" and "notes survive Maya's erasure... remains live into later arcs"). No arc file gives the periodic beats, the Eli-reporter contact, or any payoff after Arc 6.
- **S5. SHOULD-FIX. Iris's time perception** (map: planted Arc 6, pays Arc 7). `story-bible/characters/iris.md` bullet **The time conversation (Arc 7)** puts the conversation itself in Arc 7, so the map's Arc 6 plant has no source; `arc-07.md` and era-1 Arc 7 have no Iris scene; and the mechanism is unclear: `power-system/abilities-environmental-effects.md` row Motion Freeze defines it as "Reducing kinetic energy of matter toward zero," `power-system/power-progression.md` says Eli "manipulates the gravitational and inertial conditions that time responds to," and `iris.md` says the conversation changes "what he's always been doing when he freezes motion" as the last piece of Arc 7 gravitational-field mastery (Stage 1 in `arc-by-arc-power-progression.md`).
- **S6. SHOULD-FIX. "Twitch's time dilation → Arc 7"** (map). `vinny-black.md` says Vinny uses "short-term time travel" in Arc 5, `arc-04.md` says "Foreshadowing Vinny's time magic complete" in Arc 4, and no outline places time travel on the page in Arc 5. The first payoff is unplaced; the last (Arc 7) is fine.
- **S7. NOTE.** Orphaned phrase: the map row "Cult leader's blood transfer death" refers to "the 'mostly' in Shockwave's survival is the partial rejection scaled up"; no file describes Shockwave surviving the transfer partially.
- **S8. NOTE.** Ring gesture: `vinny-black.md` says its absence "if it ever disappears, is the loudest signal"; no arc says whether it is absent at the Arc 7 disappearance.
- **S9. NOTE.** Seeds absent from the map: Simone under Maya (Arc 4 → Arc 6), the meteor → moon fight (`arc-06.md`), Joel Mara and Simone reappearing "on the right side" (Arc 6/4 → Arc 9), Danny Reeves and the Bio-Control Kid (Arc 6 mention only, by design).
- **S10. NOTE.** Twist inventory omits: the mother's-death subversion (no villain), Voss sounding like Eli's father, and the Arc 5 Shockwave help-seeking reveal.
- **S11. NOTE.** Tide's facility and Eli's romantic pattern are intentionally unresolved (`era-1-overview.md` Open Gaps #7); no scheduled payoff, by design.

### Paid off (or stated) before it is seeded

- **P1. SHOULD-FIX. The Arc 1 earthquake.** `foreshadowing-map.md`: "Never stated --- available through juxtaposition with Arc 5 earthquake rescue." `plot-twist-inventory.md`: "Never stated." `01-world.md`: "On reread it is understood..." But `era-1-overview.md` § "The Name First" states it outright as a reason for the rewind: "The tremor during that birthday dinner... was the power's first motion. It's the same force that turned a man to fog six years later," and in reading order the Opening comes before Arc 1 (`00-story-identity.md` § Opening; `opening.md`). The existing draft `stories/vector/arc-05/the-name-first.md` also says "a tremor that nobody will connect to anything for years." So the twist is delivered before the seed is planted, by the piece that is supposed to come first. (The earthquake rescue callback in `arc-05.md` still pays off, but as confirmation, not surprise.)
- **P2. NOTE.** Voss's city-wide sensing is placed in Arc 6 (`arc-06.md`) before its Stage 3 level in Arc 7 (C6).
- **P3. NOTE (draft vs bible, out of audit scope).** `opening.md`: "I'd known it since the first time we fought"; the draft says "I looked it up two years ago." Not a bible conflict, but the draft contradicts the outline.

### Checked and consistent

Ouroboros ring (Arc 0 → all arcs; hand gesture from Arc 2), Theo's tracking (Arc 2/3 → Arc 5), physics teacher in paper trail (Arc 0 → Arc 6), Group 1/Group 2 split, Colombia → Arc 8, the suit Arc 1 → Arc 7, and "Maya erased more than the identity reveal" (direction of memory: the map and inventory agree with each other and with four other files; only `era-1-overview.md` disagrees, C1).

---

## 6. Canon change proposals for the author

None of these are applied. Each names what it would touch. Decisions are yours.

**Erasure and identity**
1. **Fix the direction of Maya's erasure to "father forgets, Eli remembers."** Touches `era-1-overview.md` ("The Admission" Resolution, "The Conversation" Obstacles). Five files already agree; two lines are the outlier. (C1)
2. **Write one identity-knowledge ledger and sequence.** Proposal: reveal, mother killed, admission (with father knowing), erasure (father loses reveal and admission; Eli keeps both), Eli discovers the erasure held only on return. Then admission #2 in Arc 7 is a genuine restart. Touches `arc-06.md` (reorder bullets), `arc-07.md` bullet Father conversation, `eli-reyes.md` (His father), `physical-consequences-and-canon.md` (Return), `maya-vale.md`, and add a ledger table to `maya-vale.md` naming who retains what (father, friends, physics teacher, reporter, Iris, killer). (C2, G4)
3. **Decide the mother's killer:** who, whether caught, and whether the story tests the "no killing unpowered people" law here. Touches `arc-06.md`, `era-1-overview.md` "The Civilian," `eli-reyes.md` (the religious devil-reading), `story-laws.md` (only if the test becomes a cited example). (G4, G16)

**Iris**
4. **Resolve the class premise.** Options: (a) the 24 come from several schools/classes (edit `arc-00.md`, `01-world.md` "24 sixth-grade students... Splits into two groups of 12"); (b) keep one class and make Iris and Eli near-strangers who remember each other only faintly, changing the Colombia beat from "shared origin revealed" to "shared origin *named*." Touches `arc-00.md`, `01-world.md`, `iris.md`, `arc-06.md`, `era-1-overview.md` "Colombia." (C3, G13)
5. **Give "Iris knew first" a mechanism.** Proposal: Iris knew *Eli Reyes* from the class roster, and learned Vector = Eli from the 2020 reveal; the erasure missed her because she was outside the city's mind-reach or abroad. Rename the list "Group 1 list" to "the roster" throughout. Touches `iris.md`, `arc-06.md`, `01-world.md` (Reporter), `foreshadowing-map.md`, `plot-twist-inventory.md`. (C4)
6. **Reconcile Colombia chronology:** Iris present weeks 1-24; reword "Iris arrives" to "Iris becomes central." Touches `physical-consequences-and-canon.md`. (C5)
7. **Pick Iris's vocation and the Arcs 3-5 activity** (one concrete project, one place, one person). Put an Arc 8 Iris scene in the slate to cover Eli's disappearance. Touches `iris.md`, `era-1-overview.md`, `action-items-v5.1.md` item 1. (G6, G19)

**Villains and powers**
8. **Close Brick:** adopt "Group 2 kid with earliest onset." Evidence the bible already contains but does not cite: `onset-timeline.md` lists exactly twelve people, matching the twelve Group 2 children in `arc-00.md`; Brick is one of the twelve. Then reword `story-laws.md` ("with the exception of Brick") and `villains/CLAUDE.md` to "Brick's fight is the exception to the origin question, not the exposure." Touches `brick.md` (status), `arc-00.md`, `onset-timeline.md` Open, `era-1-overview.md` #2.
9. **Unify the cult leader's death** (proposal: he died absorbing Vinny's *blood*, which carries the regenerative byproducts; magic was not the killer) or adopt the magic version and edit `arc-03.md`, `physical-consequences-and-canon.md`, `era-1-overview.md`, `foreshadowing-map.md`. (C8)
10. **Update the "Vinny is most powerful" language** in `plot-twist-inventory.md`, `foreshadowing-map.md`, `vinny-black.md` § "Power --- the reframe," and `story-laws.md` 6th bullet to match the vessel/source model, and define "structurally most powerful" relative to Eli's unused ceiling (for instance, "most powerful in exercised capacity"). (C9, V3)
11. **Remove "unkillable/invincible" wording** from `vinny-black.md` and `eli-reyes.md`; reword the twist-inventory heading "The Ouroboros ring was placed" to a neutral title (e.g., "The Ouroboros ring appears"). (V2, V3)
12. **Delete "not yet" from `era-1-overview.md` "Maya"** and cite the law without qualification. (V1)
13. **Specify the chaos-vs-Stage-3 rule:** "chaos disrupts Stages 1-2; Stage 3 abilities function but are absorbed by Vinny." Touches `power-progression.md`, `arc-07.md` Phases 3-5, `plot-twist-inventory.md`. (C11)
14. **Place Voss in Arc 7 only;** delete his bullet from `arc-06.md`. (C6)
15. **Update `maya-vale.md`** to Arc 7 intel drop plus Arc 9 reunion; change "mid-confrontation" in `open-questions.md` to "just before the confrontation." (C7)
16. **Decide when Maya first acts:** either Maya is active but unseen from 2017/18 (then edit `onset-timeline.md` first appearance and `arc-06.md` "Simone as first proxy") or Simone's Arc 4 control is by someone else. Touches `arc-04.md`, `simone.md`, `arc-06.md`, `suit-evolution.md`. (C12, C13)
17. **Fix the onset table or the rule:** re-tier Voss and the Bio-Control Kid as BROKEN-adjacent, or state that INFORMATION/mind-adjacent powers are exempt; change "nearly last" in `01-world.md` to "in the last third." (C17)
18. **Clean `arc-by-arc-power-progression.md`** (Arc 6 duplicate, missing flight/element bending). Add a one-line note that self-regulation of physiology stops short of emotion. (C16, V9)

**Structure, timeline, and other files**
19. **Settle the name-circulation arc** (`eli-reyes.md` Arc 2 vs `suit-evolution.md` Arc 3) and the aging start (Arc 6 vs Arc 7). (C14, C15)
20. **Decide the medical pipeline:** e.g., a fast-track that runs 2018-2019 offscreen, or reframe "residency" as a clinical fellowship, and stop `eli-character-arc.md` Phase 3 from carrying residency into Arcs 4-5. Touches `eli-reyes.md`, `arc-05.md`, `arc-06.md`, `eli-character-arc.md`. (C18)
21. **Assign the Science Center POV:** either update `00-story-identity.md` to remove it from Eli's present-tense breaks, or change `arc-07.md`/`era-1-overview.md` to allow a POV hand-off. (C10)
22. **Clarify the Colombia practice vs the moral framework** with one sentence in `moral-framework.md` (e.g., "the retreat teaches attention, not the ethic; the ethic remains unnarrated"). Add the lexicon (G17). (V5, G17)
23. **Relabel Arc 5 "First glimpse of playing god ceiling"** in `shockwave.md` (e.g., "first glimpse of what restructuring is") unless restructuring is meant to be the ceiling. (V6)
24. **Reframe the two queues.** In `open-questions.md`, mark "Vinny's whereabouts" and "devil's endgame" as "deliberately open (`story-laws.md`)," keeping only "does Vinny appear in Arc 9?" as a decision; refresh "Recommended Writing Order" against `arc-00.md`/`era-1-overview.md`. In `action-items-v5.1.md`, add a drafting-blockers item ahead of item 1 or 2: names (Shockwave, mother, father), "Eighteen," identity ledger, killer, paper-trail mechanism; and mark item 3's first bullet answered. (Section 4)
25. **Add missing slate stories** to `era-1-overview.md`: Eli tells his mother (G3); Arc 5 setup (Brick's death, Simone freed, Shockwave transformed); Joel Mara; Vinny's Arc 6; the Iris time conversation; the physics teacher in Arc 1. (G3, G9, G11, S2, S5)
26. **Fill the map:** add the Simone → Maya seed, the meteor → moon seed, Joel/Simone → Arc 9; correct the Iris time conversation plant/payoff arcs; decide whether the Opening states the birthday tremor's cause (P1). Touches `foreshadowing-map.md`, `plot-twist-inventory.md`, `era-1-overview.md` § Opening. (S5, S9, P1)
27. **Fix small text errors:** `01-world.md` "Shifter" (C21), `action-items-v5.1.md` footer version (C27), `plot-outline/CLAUDE.md` file list (C30), `eli-reyes.md` age band (C20).

### Unverifiable or not checked

- I could not verify whether the reference roster in `reference/` has any collision with Vector beyond the Twitch/Blink rename (out of scope).
- I did not read `writing-guide/style-guide.md`, `eval-checklist.md`, or `themes/`; any conflict they hold with the bible is not reported.
- The claim in C3 that the 24 are "one class" is my reading of "the class splits into two groups of 12" in `arc-00.md`; if the intent was several classes, C3/G13 shrink to a wording fix.
- Root `CLAUDE.md` says `stories/` is "Currently empty" while `stories/vector/arc-05/the-name-first.md` exists (out of scope, noted only).
