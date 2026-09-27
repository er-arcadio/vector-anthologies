# Vector Anthologies

Story development repo for the *Vector* series and the broader anthology roster. Content is split into small, single-topic Markdown files (rather than one long document) so it's easy to look up, link, and search — each file covers one character, one arc, or one system.

**Start with `CLAUDE.md`** at the repo root — it's the main navigation guide for anyone (human or agent) working in this repo. Every folder below also has its own `CLAUDE.md` with folder-specific guidance.

## Structure

```
CLAUDE.md                       Start here — repo-wide navigation guide

story-bible/                    Eli/Vector's story — the primary series (canon reference, not prose)
├── CLAUDE.md
├── 00-story-identity.md        Logline, themes, tone, narrative voice
├── 01-world.md                 Setting, the accident, society's response
├── moral-framework.md          The world's moral/spiritual framework — ambient on Earth, confronted on the Arc 8 planet
├── characters/                 Eli, Iris, the physics teacher, Vinny
│   └── CLAUDE.md
├── villains/                   One file per villain (Brick, Shockwave, Twitch, Tide, Simone, Maya Vale, Bill Voss, Joel Mara)
│   └── CLAUDE.md
├── power-system/               Power rules, progression, abilities table
│   └── CLAUDE.md
├── eli-character-arc.md        Five-phase character arc
├── suit-evolution.md
├── plot-outline/               One file per arc (opening + arcs 1–9)
│   └── CLAUDE.md
├── foreshadowing-map.md
├── plot-twist-inventory.md
├── open-questions.md           Original unresolved decisions
└── action-items-v5.1.md        Active development priorities (Iris, playing-god ceiling, Arc 8)

reference/
├── CLAUDE.md
└── superhero-reference-book/   Separate hero roster for future anthology entries
    ├── CLAUDE.md
    ├── roster-overview.md      Core criteria + status snapshot
    ├── 01-warewolf.md … 07-chicle.md
    └── power-convergence-guide.md   Power-tier calibration reference (domains, ceilings)

writing-guide/                  Read before outlining or drafting any story
├── CLAUDE.md
├── outline-checklist.md            Checklist for sequencing events before any scene is written
├── character-journey-worksheet.md  Per-character template, filled out before outlining (outline-checklist.md's Section 0)
├── style-guide.md                  Tone, voice, prose technique — the drafting-ready version to follow
├── story-laws.md                   Hard canon constraints — not preferences
└── fiction-style-profile.md        Where style-guide.md's prose-preference rules come from (real books ranked against each other) — still preference rules, just in research form rather than drafting-ready

themes/                          Thematic source material (life-lessons content), not yet tied to a specific story
├── CLAUDE.md
├── lessons-for-young-men.md            General-audience life lessons
└── lessons-for-young-men-adult.md      Same source, 18+ material (content_rating: adult)

stories/                        Actual short story drafts (currently empty)
└── CLAUDE.md                   Filing conventions, frontmatter, canon_status

TODO.md                         Tooling/process backlog only (e.g. an eval harness) — narrative
                                 todos stay in story-bible/action-items-v5.1.md, not here
```

## Notes

- **For agents/Claude:** every folder has a `CLAUDE.md`. Read the root one first, then the folder-specific one for whatever you're working on — especially `writing-guide/` before drafting any prose.

- **Naming:** the *Vector* villain formerly called "Blink" (super speed, Arcs 3–4) has been renamed **Twitch** to avoid collision with the separate reference-roster hero **Blink** (teleportation, hummingbird totem — not yet part of the main story).
- **Frontmatter:** every file has YAML frontmatter (`title`, `tags`, and where relevant `status`/`related`) for quick lookup and filtering.
- **Status flags:** files with an open development need carry a `status:` line — currently `characters/iris.md`, `plot-outline/arc-08.md`, and `reference/superhero-reference-book/05-vampire-doctor.md` and `06-blink.md`.
- **Source:** migrated from *Vector Story Bible v5.1* and *Superhero Reference Book*. Treat this repo as the source of truth going forward; update files directly rather than the original docs.
