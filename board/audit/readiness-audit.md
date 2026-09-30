---
title: "Readiness Audit — Can a Story Be Drafted Today?"
tags: [audit, development-edit, process, era-1]
audited: 2026-09-30
scope: read-only structural audit; no existing file was modified
---

# Readiness Audit — Vector Anthologies

Read-only development edit. Paths are relative to the repo root. "§" means a heading in the cited file; line numbers are given where a quote needs pinning down. Word counts are body text only (frontmatter and the trailing `<!-- eval notes -->` block excluded).

---

## Summary — the five findings that matter

1. **The pipeline breaks at the seam between `era-1-overview.md` and the outline pass, not at the start.** Root `CLAUDE.md` (§ Before outlining, step 2) says the overview supplies "that arc's starting point / want / obstacle / resolution shape." It does not. Each story entry holds only *Main character / Main problem / Obstacles / Resolution* (`era-1-overview.md` lines 10-15). No per-story want, need, Point A, Point B, obstacle type, cost, or `story_type` exists, and those are exactly the fields the required `<!-- story shape -->` block and `eval-checklist.md` §0 demand. The outline pass then has no template, no home and no approval state. For an Eli-POV story a writer can bridge this with `eli-reyes-journey-worksheet.md`'s per-phase table. For any other POV they invent it.
2. **Slate readiness is 14 draftable / 19 needs work / 5 blocked (38 stories).** Arc 1 and Arc 2 are the most ready. Arc 6 has zero draftable stories. Every blocked story traces to one of three things: Eli's mother (no name, no want), Eli's father (no interior), or the explicit `[GAP]` on "Eighteen."
3. **`the-name-first.md` should be rewritten from an outline, not revised, and it should not be the first story through the new pipeline.** The body is 2,004 words against a 3,000 floor. The board's structural finding (no live decision) is also baked into the overview's own framing (the overview says Eli "has just done" the killing). Beyond the five canon errors already logged, the draft contradicts Arc 2 canon on when Eli learned Shockwave's name and omits the Cory/Vinny transfer. Shockwave has no name anywhere in the bible, so the scene's hinge (saying the real name) has no input.
4. **Process holes are structural.** There is no "outline approved" state, no author-approval field, no revise/retire path for flagged stories, and no mechanism that says which story is next. The public site publishes flagged, author-rejected drafts. Reading order is impossible to control: the site sorts by written-date newest-first, and Arc 0 is supposed to be "placed first." The eval pass is run by the drafter and missed four canon errors that the board caught.
5. **Docs have drifted, and there are four backlogs, not two.** Examples: `writing-guide/CLAUDE.md` still states a 1,500-4,000 word target; `stories/CLAUDE.md` says the folder is "Currently empty"; three files cite an outline-checklist "Section 0" that does not exist. The only open item in `TODO.md` is a narrative task (the hero's-journey overlay) and is stale (it waits on Iris's want, which is settled). The backlog that actually gates drafting (agree the overview; name and characterize the mother and father) is in neither file.

**Recommended first action:** run an author-agreement pass on the *Arc 1 slate only*. Extend the overview's per-story template with the missing shape fields, fill them for the seven Arc 1 stories, and resolve the handful of Arc 1 decisions. Then mark Arc 1 "agreed" in the file. Then pilot-draft "Cleanup." Details in §6.

---

## 1. Can a story be drafted today?

**Short answer:** Yes for a small set of Eli-POV Arc 1-2 stories, *if* the author is willing to treat the draft overview as agreed. No for anything the process would call "ready": the process does not define what "ready" means, so nobody can currently certify it.

### The pipeline as documented

Root `CLAUDE.md` gives three lists, and `stories/CLAUDE.md` gives a fourth that orders them differently.

| Step | Source | Exists? | Verdict |
|---|---|---|---|
| 1. Fill a character-journey worksheet per POV/major character | Root `CLAUDE.md` § Before outlining, step 1; `stories/CLAUDE.md` § Before writing, item 3 | **Eli only** (`story-bible/characters/eli-reyes-journey-worksheet.md`). Iris has want/need/gap in prose (`characters/iris.md` § Her want and her need) but not in worksheet form. Vinny has a want, no stated need, no gap, no ending state (`characters/vinny-black.md`, "What Vinny wants"). Mother, father, physics teacher, Cory, Shockwave: nothing. | **Blocks every non-Eli POV story.** |
| 2. Read the story's entry in `era-1-overview.md` | Root § Before outlining, step 2 | Exists, 38 stories. Marked `status: draft — pending author agreement before treated as settled canon`. | **First gate.** See below. |
| 3. Run the event sequence through `outline-checklist.md` | Root step 3; `stories/CLAUDE.md` item 4 | Checklist exists. No event sequences exist anywhere; the overview has 4-field summaries, not sequences. | **Second gate.** |
| 4. Read `style-guide.md`, `story-laws.md` | Root § Before writing any prose, steps 1-2 | Both exist and are detailed. | Fine. |
| 5. Read relevant bible files; check `foreshadowing-map.md` and `plot-twist-inventory.md` | Root steps 3-4 | Exist. Thin for several characters (see below). | Fine for Eli/Vinny/Brick; thin for others. |
| 6. Draft | none | No instructions beyond style. | See §4. |
| 7. Run `eval-checklist.md`; record `eval_status` | Root § After writing a draft, step 1 | Exists and is thorough. | Fine, with the independence caveat in §4. |
| 8. Convene the board; present alongside the draft | Root step 2; `.claude/agents/board-of-advisors.md` | Exists; ran once (calibration). | Fine. |

Note the order inconsistency: root `CLAUDE.md` puts the outline reading *before* the style reading; `stories/CLAUDE.md` § Before writing a story here puts `style-guide.md` and `story-laws.md` as items 1-2 and the worksheet and checklist as items 3-4. Harmless but a sign nobody has walked this end to end.

### The first blocking point

**Step 1 fails first for any non-Eli POV.** For an Eli-POV story Step 1 passes and the first real block is **Step 2 → Step 3**. Three separate problems sit at that seam:

1. **The overview does not contain what the process says it contains.** Root `CLAUDE.md` § Before outlining, step 2: "read `era-1-overview.md` for that arc's starting point / want / obstacle / resolution shape." Actual fields (`era-1-overview.md` lines 10-15, § intro): "**Main character**... **Main problem**... **Obstacles**... **Resolution**." The only "Starting point" is era-level (§ Era-level frame, line 44). The story-shape block required by `stories/CLAUDE.md` § The "story shape" block is required needs **POV, Want, Need, Point A, Point B, Obstacle (external | interpersonal | internal), Resolution and its cost**. The overview supplies roughly POV, obstacle (untyped), and resolution. **The specific missing inputs are per-story Want, Need, concrete Point A / Point B, obstacle type, cost, and `story_type`.** `eval-checklist.md` §0 says a story lacking these "doesn't have a clear A-to-B yet — a flag, and usually a sign `outline-checklist.md` got skipped."
2. **The overview is unagreed and the repo has no way to agree it.** The `status:` line says pending author agreement. The only precedent for how that status is treated is the existing story: `the-name-first.md` eval notes, "REVISION PENDING": "needs a rewrite once story-bible/plot-outline/era-1-overview.md is agreed." A repo-wide search for approve / agreed / sign-off finds no mechanism. So a writer cannot tell whether "draft" means "safe to use for Arc 1" or "do not draft yet."
3. **The outline step has no output.** `outline-checklist.md` is a validator ("Each event on your outline should pass these checks") with no template, no location for the outline, and no reviewer. The only place its result is recorded is the story-shape block, which lives in the story file that does not exist yet. It also has no "Section 0": `character-journey-worksheet.md` line 8 and `README.md` (structure tree, `character-journey-worksheet.md` row) say the checklist "references this as its Section 0." The checklist's sections start at "1. Before You Sequence Anything."

### Where a writer has to invent, in the order they hit it

- Per-story want / need / A / B (above). Eli-POV can lean on the per-phase table (`eli-reyes-journey-worksheet.md` § Per-phase quick reference), which is one row per two arcs and too coarse to give a single story's want.
- Family specifics. `story-bible/00-story-identity.md` and `characters/eli-reyes.md` say "dark-skinned Latino-American," Jersey City. A repo-wide search for any specific heritage, language or church returns nothing. Mother and father are unnamed (`open-questions.md` § Decisions Still Needed: "Mother's first name: Not yet established"). The board's Renata Ocampo already flagged the consequence on the existing draft: "Nothing in this house is Dominican or Puerto Rican or Jersey City." Every Arc 1 story with the family in it will invent this.
- A word budget. Nothing tells the writer how to spend 3,000-5,000 words on a story whose overview entry is four bullet groups.

**Bottom line for Q1:** the first point where a writer is blocked is the missing per-story shape fields (plus the unrecorded agreement) at Step 2 → 3; for non-Eli POV it is the missing worksheet at Step 1.

---

## 2. Is `era-1-overview.md` actually draftable?

**Verdict:** It is a strong *premise-and-problem* slate and a weak *shape* slate. Most entries have a real protagonist, a real problem, and named obstacles. Almost none state a want, and none state a Point A / Point B. Where the protagonist is not Eli, the missing worksheet compounds it. It is draftable for a core set of Eli stories and not, as a whole.

Legend: **Y** = usable as written. **P** = implied or partial; a writer must infer. **N** = absent. "Want" is what the protagonist is trying to get *in this story*; the overview never labels one, so Y means unambiguous from the entry.

### Per-story table

| Story | Protagonist | Want | Obstacle | A-to-B | Verdict | Note |
|---|---|---|---|---|---|---|
| **Opening / Arc 5** The Name First | Y (Eli) | P | P | P | needs work | Entry frames the story as aftermath ("has just done"); `arc-05.md` § The Killing frames a live decision. See §3. |
| **Arc 0** Group Two | P (Eli named; story is about a room) | N | P | N (by design) | needs work | Deferred by design ("Write this arc later, place it first," `arc-00.md`). Single-beat. |
| Arc 0 One Scheduling Decision | Y (Iris) | N | P | N (by design) | needs work | Deferred; single-beat. |
| Arc 0 The Door | Y (teacher) | N | P | N (by design) | needs work | Deferred; teacher unnamed (`physics-teacher.md`: Name TBD). |
| Arc 0 What Vinny Found | Y | Y (to be seen) | Y | Y | draftable | Deferred, but the entry is complete. |
| **Arc 1** Sixteen | Y | N | P | N ("nothing is recognized") | needs work | Effectively a single-beat or mood. Must be written not to duplicate the compressed birthday in The Name First (overview line 70). |
| Cleanup | Y | Y (make the room look normal before parents wake) | Y | Y | **draftable** | Best-shaped story in the slate. Phase 1 defining moment. |
| How Strong Cory Got | P (Cory, omniscient) | N | P | Y | needs work | A system story with no want for its subject; Gap #2 (Brick's relation to the accident) sits directly under it. |
| The Refusal | Y | Y (stay out) | Y (his own good reasons) | Y | **draftable** | Contains a real choice. |
| One Step at a Time | Y (mother) | P (function only) | Y | Y | **blocked** | Mother unnamed and has no want or worksheet. `action-items-v5.1.md` item 4: "**1. Eli's mother.** The most urgent by a distance... If she's only a function, her death is only a plot event. She also still needs a name." Item 4 note: build the character "*before* writing them, not after." |
| Footing | Y | Y | Y | Y | **draftable** | Cost is not stated in the entry; add it in the shape block. |
| Relief (Vinny) | Y | P | Y | Y | draftable | No Vinny worksheet, but `vinny-black.md` is rich. |
| **Arc 2** Shockwave, Contained | Y | Y | Y | Y | needs work | Shockwave has no name, no backstory scenes (`arc-02.md`: "audience knows who he was before seeing what he's become"), and no defined facility. Sets up the Arc 5 hinge. |
| Not a Priority | Y | Y | P (he's winning) | Y | draftable | Cult brand is an open decision (`open-questions.md`); trivial invention. |
| Preparation, Not Talent | Y (Vinny) | Y | Y | Y | draftable | |
| Eighteen | Y | N | N | N | **blocked** | Explicit `[GAP]`: "the arc is supposed to close on an 18th birthday that reads as 'earned rather than given,' but what earns it was never specified." Overview Open Gap #4. |
| **Arc 3** Four Seconds | Y | Y | Y | Y | draftable | Jade has no want (`action-items` item 4.8); acceptable for Eli-POV. |
| Tide | Y | Y | Y | Y | needs work | `villains/tide.md` is two bullets. `arc-03.md` demands "two simultaneous problems, scale demonstration, must be written to full dramatic potential"; neither is defined. |
| The Blackout | Y | Y (fix it) | Y | P | needs work | The failure is that he *misses the people*, but the human cost is "diffuse, statistical." A story about not noticing needs concrete people for the reader to notice. |
| The Inventory (Vinny) | Y | P | Y | Y | needs work | Four stories in one (cult leader's death, mother's verdict, massacre, Theo). Over budget for 5,000 words. |
| **Arc 4** Twitch | Y | Y | Y | P | needs work | Overview: "comparatively routine." No character stake for Eli beyond competence; `story-laws`/`style-guide` § Fight writing requires stakes "traceable to character." `villains/twitch.md` is two bullets. |
| Sol | Y | Y | Y | Y | draftable | Exit line is deliberately deferred to the writing (`open-questions.md`); fine. |
| Simone, Unresolved | Y | Y | Y | P (non-resolution is the change) | draftable | Deliberate break from the one-villain-per-arc pattern. |
| Three Weeks (Vinny) | Y (Theo/Vinny) | N (by design) | N (by design) | N (by design) | draftable | Single-beat. Decide whether Vinny appears: `arc-04.md` gives him "one scene"; the overview and `style-guide.md` § Length say he "simply doesn't appear." |
| **Arc 5** Theo | Y | N (by design) | N (by design) | N | needs work | The resolution is "Two sentences." A two-sentence beat cannot be a story file (single-beat range is "typically 800-1,500 words"). Fold into The Diner or a Vinny omnibus. |
| The Diner | Y | N (by design) | N | N | draftable | Single-beat; effect is clear ("The person he could have been is fully visible in the watching and never stated"). |
| The Name First | see above | | | | needs work | |
| The Verdict | Y | P | Y | P | needs work | The story *is* the father's speech, and its content is undefined. Father unnamed; interior is undefined (`action-items` item 4.2). |
| Earthquake | Y | Y | Y | P | draftable | Contrast piece. Its payoff (the Arc 1 tremor) only works once "Sixteen" exists. |
| **Arc 6** Residency | Y | N | N ("Nothing is wrong") | N | needs work | Mood by the overview's own admission: "No resolution, by design." Needs a concrete patient or case to dramatize. |
| Maya | Y | P | Y | Y | needs work | Too big for one story (helmet fights and mind-control in `arc-06.md`, extended confrontation, identity reveal, erasure). Maya has no want (`action-items` item 4.3). |
| The Civilian | Y | N | N | N | **blocked** | "The prose does not pause" (a few sentences). Depends wholly on the mother having been made real first. |
| The Admission | Y (father POV) | P | Y | Y | **blocked** | POV character is the father; no worksheet, no interior (`action-items` item 4.2). No style rule exists for a father-POV voice. |
| The List | Y | Y | Y | Y | needs work | Gap #6: "how the paper trail becomes public aren't specified." Teacher unnamed. |
| Colombia | Y | Y | Y | Y | needs work | Novella-scale (4-6 months, four to five beats in `arc-06.md`). Iris's vocation is open (`iris.md` [GAP]). Needs splitting. |
| **Arc 7** Voss | Y | Y | Y | Y | draftable | Hinge (Voss's argument "that sounds eerily like Eli's father") depends on the father's voice already existing in prose. Sequence it late. |
| The Conversation | Y | Y | Y | Y | **blocked** | Father again. "Eli has to earn it twice" needs the first breakthrough to exist. |
| The Science Center | Y (Vinny POV) | Y | Y | Y | needs work | Five-phase set piece across four locations and the moon. Vinny's key line undecided (`open-questions.md`). No voice rule for "POV throughout" Vinny (`arc-07.md`) versus the omniscient rule. |
| Maya, Briefly | Y | Y | Y | P | needs work | The "one human detail about Vinny" that reframes the final fight is undecided. |

**Totals:** 14 draftable, 19 needs work, 5 blocked (38 unique stories; The Name First appears twice in the overview but is one story).

### Per-arc rollup

| Arc | Stories | Draftable | Needs work | Blocked | Read |
|---|---|---|---|---|---|
| 0 (deferred by design) | 4 | 1 | 3 | 0 | Not a priority; correct. |
| 1 | 7 | 4 | 2 | 1 | **Best arc to start.** Cleanup, The Refusal, Footing, Relief. |
| 2 | 4 | 2 | 1 | 1 | Second-best. Shockwave's name and backstory are the gap. |
| 3 | 4 | 1 | 3 | 0 | Premises are good; supporting files are thin. |
| 4 | 4 | 3 | 1 | 0 | Surprisingly ready; three of four are short or deliberately open. |
| 5 | 5 | 2 | 3 | 0 | Centerpiece is the least ready story; the two short Vinny pieces are ready. |
| 6 | 6 | 0 | 4 | 2 | **Not ready.** Emotional peak, and it rests on the mother and father. |
| 7 | 4 | 1 | 2 | 1 | Blocked by the father and by undecided key lines. |

### Slate-level problems the table does not show

- **Overview omits beats that `arcNN.md` and the bible require.** Not in the slate at all: Eli telling his mother (`arc-01.md` § The arrival: "**He tells his mother.** The relief of being known"; `eli-reyes-journey-worksheet.md` Phase 1: "Tells his mother"); Cory's death and the transfer to Shockwave, Simone freed, Vinny's stone-destroyed appearance and the physics teacher's "oblique conversation" (all in `arc-05.md`); the electromagnetic-helmet fights, Joel Mara, the meteor (`arc-06.md`); Iris's Arc 7 "time conversation" (`iris.md`) and the Arc 7 moon fight as a discrete story.
- **Seeds with no host story.** `foreshadowing-map.md` places "Nothing is perfect" and "Comprehension ceiling stated as rule" in Arc 1, "Vinny sees Eli as rival brother" in Arc 2, and "Reporter byline" in Arc 2/3. No slate entry for those arcs contains the physics teacher, the rival-brother framing, or the reporter. The recommended writing order (`open-questions.md` § Recommended Writing Order, items 4 and 6) wants a physics-teacher first encounter; the slate has none.
- **`story_type` is never assigned.** `style-guide.md` § Length says several of these beats "are designed this way on purpose" as single-beat, and requires each story to declare a type. My read is roughly eight single-beat pieces (Theo, Diner, Three Weeks, Civilian, Group Two, One Scheduling Decision, The Door, probably Sixteen), which keeps arc-advancing in the majority. But the single-beat range does not fit the slate's own examples: "Theo" is two sentences and "The Civilian" is "a few sentences."
- **Voice coverage gap.** `style-guide.md` § Narrative voice defines two voices: Eli first-person (retrospective, present tense) and an omniscient grandmother. Slate entries with the mother, the father, Cory or the teacher as main character, and "Vinny (POV throughout)" in The Science Center, have no voice rule.

---

## 3. The existing draft: `the-name-first.md`

### Facts

- Frontmatter: `story_type: arc-advancing`, `canon_status: draft`, `eval_status: flagged`, `date: 2026-09-27`.
- **Length: 2,004 words** (body only). Style guide target for arc-advancing is 3,000-5,000 (`style-guide.md` § Length; `eval-checklist.md` §0). That is about 1,000 words (33%) under the floor, with no rationale recorded. The eval notes' own "~2,000 (within 1,500-4,000 band)" cites the retired band. The notes then reverse it under REVISION PENDING: "conceived as a full story and came in short, which is exactly the case the label isn't allowed to paper over."
- No `<!-- story shape -->` block.
- The piece is filed under `arc-05/` but is a diptych: Arc 1 birthday (about 580 words) plus Arc 5 killing and aftermath.
- It is live on the public site. `scripts/build_site.py` (lines 50, 129-133) skips only `CLAUDE.md` and `*-review.md`; it does not read `eval_status` and shows `canon_status` only as a badge.

### What the board actually flagged (`the-name-first.board-review.md`)

The board itself says its run was a "calibration — first run of the board, on a draft already slated for rewrite," so treat it as partly a test of the board.

Structural, five of eight advisors:
- **The killing has no decision in it** (June Okada): "By 'There is a version of this where I get close enough,' it's settled." The thesis "arrives as a report, four seconds late by the story's own admission." "You can't dramatize a road not taken that the character didn't know was there."
- **The birthday has no want and no obstacle** (June): "does the second panel mean anything different without the first? I don't think it does."
- **No sixteen-year-old** (Marcus Feld): "There is no sixteen-year-old in that scene." Fun, which the guide says gets "disproportionate page-time," gets "zero."
- **Emotional shorthand** (Yvonne Baptiste): the piece "announces its own restraint and then grades it."
- **Shockwave has a biography and no body**; withholding his name "works against the beat canon says the scene is built on."

Perspective:
- Unplaced family, Spanish absent, father "translated" (Renata Ocampo). Mother as function, the third-floor woman as a demonstration (Alice Nkemdirim). The narrator "converted grief into a competency" (Tomás Ruiz). Belief thinly rendered (Deacon Warner).

Canon / research (copied to the story's eval notes):
1. Arc-lock: "field sensing" belongs to Arc 6 (`power-system/arc-by-arc-power-progression.md`).
2. Research anchor: "fear has no readable electromagnetic signature."
3. Physics: deconstruction at that mass releases heat and an EM pulse (`power-system/abilities-environmental-effects.md`), yet nobody on the block registers it.
4. The eval notes contradict the prose: they say the tremor seed was "left unstated," but the prose says "I didn't know yet what six-forty was. I know now."
5. Clinical: a progressive tremor would get a referral or imaging, not a stress pamphlet.

### Additional problems the eval and board did not record

I verified these against canon.

- **Shockwave chronology contradicts Arc 2.** Draft line 40: "I looked it up two years ago, back when he was still a guy with a job and a shaking hand and a doctor." Canon: `opening.md` has Eli say "I knew his name. I'd known it since the first time we fought." `power-system/onset-timeline.md` gives Shockwave onset 2011, first public appearance Arc 2 (2013). `era-1-overview.md` "Shockwave, Contained" (11/2013) has Eli identify and contain him, with the doctor failure "which Eli only learns later." The draft has a stranger Eli half-knows; canon has a man Eli already failed once ("his first real moral debt"). That debt is the emotional engine the draft is missing.
- **The cause of the crisis is missing.** `arc-05.md` and `villains/brick.md` § Death: Vinny extracts Cory's strength and transfers it to Shockwave, producing the yellow transformation. `foreshadowing-map.md` (cult leader's blood transfer, Arc 3 to Arc 5) says "the 'mostly' in Shockwave's survival is the partial rejection scaled up." The draft has no Vinny, no transfer, no containment failure.
- **Shockwave has no name in the bible.** `villains/shockwave.md` gives none; `era-1-overview.md` § The Name First says he "said the man's real name out loud first." The scene's hinge requires an input that does not exist.
- **The playing-god ceiling reads as ignorance, not refusal.** Draft: "I don't know if it would have worked... the knowledge of the drawer arrived about four seconds after I needed it." `story-laws.md` § Power system: "Never write this as something he *can't* do — it must always read as something he *won't*." `shockwave.md` calls this the "First glimpse of playing god ceiling." The overview and the worksheet ("drilled tool rather than the untested, humane one") make the four-second lag intentional, so the draft may be right, but this is an unresolved tension between two laws and the author should decide it explicitly.
- **Dialogue pattern.** The birthday exchange runs one line, one narration beat, one line, one narration beat. That is the *Bluebird, Bluebird* pattern `fiction-style-profile.md` and `eval-checklist.md` §1 call "the single most common failure mode." The eval notes did not mention it.
- **Tone ratio.** The 30% visceral-action lane is essentially absent; the fight is summarized in reflection.
- **Moral-framework boundary.** The overview's thesis ("is killing still wrong when it was right?") sits close to `moral-framework.md`'s rule that Era 1 material must never argue the framework on the page. Not a violation, but the rewrite should stay on personal ethics.
- **Overview versus arc file.** `era-1-overview.md` line 57 frames the story as aftermath ("has just done"). `arc-05.md` § The Killing says "The not-instantaneous is in the decision... Eli lives in the moment of choosing long enough to fully own it." The draft follows the overview and gets flagged for it. The author has to pick one before the rewrite.

### What would have to change to pass `eval-checklist.md`

| Section | Now | Needed |
|---|---|---|
| §0 Length and shape | 2,004 words, no rationale; no shape block | 3,000-5,000 words or a recorded rationale (the author has already said no relabel); shape block filled from an outline (POV, Want, Need, Point A, Point B, Obstacle type, Cost). Author's own instruction: "the outline pass should happen first, not be reverse-engineered." |
| §1 Style | Young-Eli voice fails; dialogue interruption; no visceral lane; tone ratio; restraint off-page | Sixteen-year-old attention on the page (fun, fixation, dread-vs-anxiety); sustained dialogue in the kitchen scene; the fight and the restraint given real page time |
| §2 Story laws | Arc-lock breach (field sensing); ceiling framing unresolved | Replace sensing with an Arc 5 ability (proximity sensing is listed at Stage 2 in Arc 3; confirm it persists); decide "won't" versus "didn't think of it" on the page |
| §3 Canon | Shockwave chronology and cause wrong; seed stated outright; EM/heat physics; no Vinny/Cory link | Align with Arc 2 (name known since 2013); state the transfer or leave it off-page deliberately; do not state the 6:40 tremor connection (or change the foreshadowing map); give the deconstruction a physical signature |
| §4 Board | Done (sidecar exists) | Re-run after rewrite; the sidecar covers the old draft only |
| §5 Final call | `flagged` | Reaches `passed` only when §2 and §3 flags close |

### Recommendation: **rewrite from an outline. Do not revise. Do not draft it first.**

Reasoning:
1. **Revision cannot fix the shape.** The defects are not sentence-level. The board's convergent finding (five of eight advisors, and the room's phrase "a very well-written aftermath of the story it means to be") is that the draft has no decision and no sixteen-year-old. Adding 1,000 words to a piece without a decision produces a longer aftermath. The author reached the same conclusion: "needs a rewrite once story-bible/plot-outline/era-1-overview.md is agreed."
2. **The piece is the era's thesis (overview line 50) and the Arc 5 centerpiece, and it leans on stories that do not exist.** It needs the Arc 2 containment (the moral debt), "Sixteen" (so the birthday isn't duplicated: overview line 70), a named Shockwave, and ideally "Earthquake" for the juxtaposition. Writing it first inverts the dependency the bible is built on.
3. **Shelving outright wastes real assets.** Keep as reference for the rewrite: the killing panel images (held-breath quiet, sirens for a fire already out, hands that don't shake), the father line "the smoke was the actual subject and I was incidental to it" (Tomás: the most accurate thing in the draft), and "warm in a way that had nothing to do with the candles" (Marcus: pitched exactly right, "which tells me the register is available").
4. **Immediate housekeeping (no rewrite needed):** the file is public. Take it off the feed (for example `canon_status: non-canon` plus a publish filter, or move it out of `stories/`) so an unapproved draft is not the site's only story.

Precondition decisions for the rewrite outline: Shockwave's name and the Arc 2 backstory; whether the killing is a dramatized decision or a reported aftermath; whether the 6:40 tremor is stated; what Eli *wants* in the scene.

---

## 4. Pipeline gaps in the process itself

### 4.1 Is there a defined step between "outline approved" and "draft exists"?

**No, and "outline approved" does not exist as a state.**
- Root `CLAUDE.md` § Before outlining step 3: "run the event sequence through it before handing anything off to be drafted as prose." There is no receiver, format, or approval for that "handoff."
- `outline-checklist.md` §9 speaks of "handing an event off to be drafted as a scene." Same gap.
- The outline has no artifact. The only place it lands is the story-shape block, which sits inside the not-yet-existing story file.
- Nothing addresses scene-level planning or spending a 3,000-5,000 word budget.
- **Whose pen is it?** Root `CLAUDE.md` addresses an agent ("Before writing any prose"; "Treat `story-bible/` as source of truth"). `eval-checklist.md` lines 11-14 say the repo "has exactly one author whose voice is the thing being protected." The board agent says "The author is developing his own voice... Never rewrite his prose." The Name First evidently was agent-drafted (eval notes: "Fixed: Shockwave's color was drafted as..."). The docs never say who drafts, which decides everything downstream.
- **What is the short story *for*?** `style-guide.md` § Length: short stories are "separate from the eventual novel-length prose the story-bible arcs are outlined for." `open-questions.md` § Format Decision: "Confirmed: Novel first. Complete prose before any adaptation." The relationship between the 38-story slate and the novel is undefined, which affects what "done" means.

### 4.2 Who decides a story is done?

- The checklist decides `eval_status`. The author decides everything else ("Never act on its flags unilaterally; the author decides what to take," root `CLAUDE.md` § After writing a draft, step 2). But there is **no field for author approval**. `eval_status` is `unreviewed | passed | flagged`; `canon_status` is `draft | canon | non-canon` (`stories/CLAUDE.md` frontmatter).
- The Name First's author rejection was recorded as an ad-hoc comment ("REVISION PENDING... Author reviewed this draft and did not approve it") with `eval_status` left at `flagged`. So `flagged` currently means both "objective canon error" and "the author didn't like it."
- `eval-checklist.md` §5 says `passed` is "clean, or only Section 0/1 flags left as accepted exceptions," and `flagged` is "Section 2 or 3 issue found." A Section 4 (board) outcome maps to neither.
- Nothing says who flips `canon_status` to `canon`, or checks the "silent fork" condition in §3 (bible file updated).
- "Run once per draft" (`eval-checklist.md`, intro) says nothing about a re-run after revision.

### 4.3 What happens to a flagged story?

- `eval-checklist.md` intro and `stories/CLAUDE.md` § `eval_status`: it can be filed as `canon_status: draft`, "shouldn't move to `canon_status: canon`." That is all.
- No revise loop, no re-eval trigger, no shelving or retirement, no archive. Version history is git only.
- **The public site publishes it anyway** (see §3 Facts). Every flagged or unapproved draft goes live with a "draft" badge. The HTML comment carrying the eval notes passes through Python-Markdown into the page source.

### 4.4 Is there anything that tells the author which story to write next?

**No.** Four sources point in different directions:
- `era-1-overview.md` § This is a map, not a queue: "Writing starts at Arc 1... write in whatever order you're actually excited about."
- `open-questions.md` § Recommended Writing Order: eight items, predating the slate. Items 1, 2 and 7 all describe The Name First (item 7 says "Write it last of the early material," item 1 says start with it). Item 1 conflicts with "Writing starts at Arc 1."
- `action-items-v5.1.md` header: "*Sequenced for reading pleasure and payoff, not writing ease.*" It sequences bible development (Iris, playing-god ladder, Arc 8), not stories. Its item 4 note refers to "the character whose story is next in the queue" — a queue the overview says does not exist.
- `arc-00.md`: "Drafting starts at Arc 1."
- There is no per-story status column (not started / outlined / drafted / flagged / passed / canon), so nobody can see what has been done.

### 4.5 Is the ordering of stories across arcs decided anywhere?

- **Writing order:** not decided (above).
- **Reading order:** effectively decided *wrong* by the tooling. `build_site.py` sorts by `date`, newest first. `stories/CLAUDE.md` § `date` is required: "the real-world date the story was written (not in-story chronology)." There is no order or sequence field in the frontmatter. So "Arc 0... **place it first**" (`arc-00.md`, `era-1-overview.md` § This is a map) cannot be implemented: a later-written Arc 0 will sit at the top of a newest-first feed, and the whole feed reads in reverse writing order. This matters because the bible's twist architecture depends on order (`plot-twist-inventory.md`: the Arc 1 tremor is recontextualized by the Arc 5 rescue; `foreshadowing-map.md`: "inevitable in retrospect").
- The Opening is designed as the first thing a reader meets (`opening.md`), yet it is the story with the worst standing.

### 4.6 Other holes worth naming

- **The eval is run by the drafter, and it showed.** Notes dated 2026-09-27 claimed Section 2/3 were clean; the board (2026-09-28) then caught four canon/research errors plus a contradiction inside the notes themselves. The board agent is not scoped to catch them: its calibration list (`.claude/agents/board-of-advisors.md` § Before you read the draft) omits `arc-by-arc-power-progression.md`, `foreshadowing-map.md`, `era-1-overview.md` and `abilities-environmental-effects.md`. It caught them anyway because Dr. Raghunathan's lens overlaps. Do not rely on that.
- **Seeds are paid off before they are planted.** The draft cites "nothing is perfect" as internalized (the map plants it in Arc 1) and pays off the Arc 1 tremor inside a story that is also the plant. There is no rule for keeping plants ahead of payoffs in writing order.
- **Doc drift (each one contradicts another file):**
  - `writing-guide/CLAUDE.md` line 6: "short-story length target (1,500-4,000 words)". Everywhere else: 3,000-5,000 (arc-advancing).
  - `stories/CLAUDE.md` line 3: "Currently empty"; root `CLAUDE.md` § Folder map: "Currently empty." The folder contains a story and its board review (both cited elsewhere in the same files).
  - "Section 0" of `outline-checklist.md` (cited in `character-journey-worksheet.md` and `README.md`) does not exist.
  - Root `CLAUDE.md` says the overview is for "Arcs 1-7" and gives a starting point / want per arc; it covers Arcs 0-7 and gives neither.
  - `story-bible/villains/maya-vale.md` § "Later encounter (Arc 9)" describes the Arc 7 encounter; `open-questions.md` § Resolved separates them.
  - `action-items-v5.1.md`: Item 1 is `[STATUS: IN PROGRESS]` while item 4 says "Iris (item 1) is now done and is the template." Footer still says "Story Bible v5.0."
- **Voice coverage:** no rule for non-Eli, non-Vinny POV (mother, father, teacher, Cory) or for close-POV Vinny, though four slate stories require them.

---

## 5. The two backlogs

### Are they consistent?

On charter, yes. `TODO.md` (line 3): "tooling and process work — not narrative development." Root `CLAUDE.md` § Folder map, `README.md` last line of the structure tree, and `action-items-v5.1.md` all say narrative goes to action-items. In practice, no:

1. **There are at least four backlogs, not two.**
   - `TODO.md` (tooling).
   - `story-bible/action-items-v5.1.md` (narrative priorities).
   - `story-bible/open-questions.md` § Decisions Still Needed (11 items, called "original unresolved items").
   - `era-1-overview.md` § Open Gaps Needing a Decision (7 items). It calls itself "distinct from `../open-questions.md` and `../action-items-v5.1.md`, which remain the canonical backlogs."
   - Plus scattered `status:` flags and story-level "REVISION PENDING."
   - Overlap is real: Sol's line is in `open-questions.md` and Overview Gap #5; Brick's accident relation is in `brick.md`, `onset-timeline.md`, `arc-00.md`, the overview and `story-laws.md`; the mother's name is in `open-questions.md` and `action-items` item 4 but not in the overview even though the overview's "One Step at a Time" depends on it.
2. **The gate is in neither.** No backlog item says "agree `era-1-overview.md`," "assign `story_type`," or "name the mother."
3. **`action-items` priority order does not follow the critical path.** Item 1 (Iris) mostly concerns Arc 6+ scenes, the least ready arc. Items 2 and 3 concern the Arc 9 climax and Arc 8 redevelopment, none of which the first prose will touch. The urgent character work (mother #1, father #2; "the most urgent by a distance") is buried as sub-priorities of item 4, `[QUEUED, ongoing]`.
4. **Status inconsistency inside `action-items`** (Iris IN PROGRESS versus "now done"; see §4.6).

### Is anything in one that belongs in the other?

- Nothing in `action-items` belongs in `TODO.md`; every item is narrative.
- The reverse is not true (next).
- `TODO.md` is missing everything that is actually tooling or process, all of which this audit found: a publish filter for `eval_status`/`canon_status`, a `sequence` (reading order) field, a per-story status tracker, the doc-drift fixes, an outline template, an approval state, and board-agent scope (add `foreshadowing-map`, `era-1-overview`, power-progression to its reading list). Its "Done" section holds the eval checklist; its "Open" section holds one narrative item.

### Is the "hero's journey overlay" a narrative task?

**Yes. It is a narrative-structure analysis and belongs in `action-items` (or should be dropped).**
- The text of the task: "check the whole span for stages that are missing, out of order, or accidentally doubled" across Eli's and Vinny's arcs and possibly Iris's, and "Probably lives as a new file in `writing-guide/` or alongside `story-bible/eli-character-arc.md`." Its deliverable is a story-bible file about story structure; there is no tooling in it.
- **It is partly stale.** It waits on Iris having a want ("once she has a want (`story-bible/characters/iris.md`)"). `iris.md` § Her want and her need — settled says the want is settled, and `action-items` item 1 marks it DONE.
- **It partly duplicates existing work.** `story-bible/eli-character-arc.md` is already a five-phase Campbell-tagged arc (Containment to Integration), and `eli-reyes-journey-worksheet.md` § Per-phase quick reference maps local want and obstacle onto it. The listed stages (call, refusal, mentor, threshold, trials, abyss, transformation, return) are an eight-step paraphrase, not a standard model.
- **Priority:** it is a check on the whole Era 1 slate. It becomes more useful *after* the overview is agreed (it audits the slate for missing or doubled stages), and it would also surface the missing "tells his mother" beat noted in §2. Move it to `action-items` below the gate work in §6.

---

## 6. What I would do first

### The single highest-leverage action

**Run an author-agreement pass on the Arc 1 slate only, in `era-1-overview.md`, and make the entries carry the shape fields.**

Why this one: it is the only action that removes the first blocker (§1) *and* creates the missing outline artifact *and* records agreement, and it is small (seven stories). Concretely:
1. Extend the per-story template with: `story_type`, Want, Need, Point A, Point B, obstacle type (external/interpersonal/internal), cost, and status (not started / outlined / drafted / flagged / passed / canon). Fill for Sixteen, Cleanup, How Strong Cory Got, The Refusal, One Step at a Time, Footing, Relief.
2. Decide the four Arc 1 open items: Sixteen as single-beat or arc-advancing; where "Eli tells his mother" lives in the slate; the family's heritage and the mother's and father's names (or a deliberate decision to leave them as "Mom" and "Dad" on the page); Brick's relation to the accident (Gap #2).
3. Set Arc 1 to "agreed" in the file, with a date. After that, "draft, pending author agreement" has a meaning.

### The five that follow

1. **Pilot-draft "Cleanup" through the full pipeline.** It has the cleanest shape in the slate (a concrete want, a clock, an external and internal obstacle, a Phase 1 defining moment) and needs almost no unwritten inputs. Have someone other than the drafter run the eval, then the board. This is the first real test of the process, so record every place it creaks.
2. **Name and characterize the mother** (worksheet plus a want of her own, per `action-items` item 4.1). She gates "One Step at a Time," "The Civilian," and "The Verdict," and she is the emotional load-bearing wall of Arcs 1-6. Do the father (item 4.2) right behind her; he gates The Admission, The Conversation and Voss's hinge.
3. **Take `the-name-first.md` off the public feed and mark it superseded**, then defer its rewrite until Shockwave has a name and Arc 2 backstory ("Shockwave, Contained" outlined) and the author has picked between the overview's aftermath framing and `arc-05.md`'s live-decision framing.
4. **Patch the process in one sitting.** Fix the drift list in §4.6; add an `author_status` or `approved` field and a `sequence` field to the frontmatter spec; make `build_site.py` honor them; give the outline a home (a `## Outline` section in the overview or an `outlines/` folder); scope the board agent to read the foreshadowing map, overview and power progression; and move the hero's-journey overlay from `TODO.md` to `action-items`.
5. **Draft the ready Vinny pair as a proof of the omniscient voice**, "What Vinny Found" and "Preparation, Not Talent," or "The Diner" folded with "Theo." They have wants, clear effects and no dependency on the unwritten mother and father, and they exercise the second voice the style guide defines but no story has yet used.

What I would *not* do first: touch Arc 6, write "The Name First," or work the `action-items` list top-down. All three are the highest-stakes work and the least supported by inputs that exist today.
