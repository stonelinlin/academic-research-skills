# ai-research-skills (formerly academic-research-skills)

**v4.0.0** — Atomic skills for AI/ML research. Trigger any skill in natural language; skills compose but don't require it.

> Renaming note: the project was previously `academic-research-skills` (general academic). v4.0 specializes for AI/ML and renames to `ai-research-skills`. The old top-level directory may still exist during the 6-month migration window — see [`docs/MIGRATION_v3_to_v4.md`](docs/MIGRATION_v3_to_v4.md).

## What This Is

10 atomic skills, each does one thing well, each callable on its own:

| Skill | What it does | Typical trigger |
|---|---|---|
| [`idea-forge`](idea-forge/) | Generate + score AI/ML research ideas | "give me ideas on X" |
| [`lit-scout`](lit-scout/) | Find + verify literature | "find papers on X" |
| [`related-positioning`](related-positioning/) | Differentiate vs existing work | "position my work vs A, B, C" |
| [`method-architect`](method-architect/) | Design experiments | "design experiment for X" |
| [`paper-writer`](paper-writer/) | Draft sections | "write the intro" |
| [`figure-smith`](figure-smith/) | Plot results, design figures | "plot accuracy vs X" |
| [`integrity-check`](integrity-check/) | Verify citations, claims, reproducibility | "check citations" |
| [`paper-reviewer`](paper-reviewer/) | Multi-perspective peer review | "review my paper" |
| [`rebuttal-coach`](rebuttal-coach/) | Author response to reviewers | "write rebuttal" |
| [`venue-formatter`](venue-formatter/) | Compile to NeurIPS/ICLR/etc. | "format for NeurIPS" |
| `research-pipeline` (meta, optional) | Orchestrate the full workflow | "full pipeline" |

## Install

Skills live as Markdown files. Two install paths:

### Cursor / Claude Code (skill auto-discovery)

```bash
# clone into your skills directory
git clone <this-repo> ~/.cursor/skills/ai-research-skills
# or
git clone <this-repo> ~/.claude/skills/ai-research-skills
```

Skills auto-trigger from natural-language phrases (each skill's `description` lists triggers).

### Manual

Open the skill's `SKILL.md` in your assistant's context when you want to use it.

## Quick Start

### "I have an interest area, no specific idea yet"

```
"Give me ideas on long-context LLM evaluation. 8 H100s for 2 months."
```
→ `idea-forge` produces ranked Idea Cards

### "I have a research question, need to know what's been done"

```
"Find recent papers on long-context LLM evaluation since 2024."
```
→ `lit-scout` produces verified annotated bibliography

### "I have a draft, want to know how it compares to known work"

```
"Position my work vs RULER, LongBench v2, NIAH-multi."
```
→ `related-positioning` produces differentiation matrix + Related Work draft

### "I have results, need to write up the paper"

```
"Draft the Method section for the long-context similarity paper, NeurIPS style."
```
→ `paper-writer` produces section draft

### "I have a draft, want pre-submission audit"

```
"Check citations and run the 7-mode failure checklist."
```
→ `integrity-check` produces verification report (BLOCK on issues)

### "I want to know what reviewers will say"

```
"Run a NeurIPS-style review on my paper."
```
→ `paper-reviewer` produces 5 reviewer reports + meta-review

### "Reviews came back, need to respond"

```
"Help me rebut these ICLR reviews. [paste]"
```
→ `rebuttal-coach` produces priority matrix + per-reviewer drafts within word budget

### "Final compile and submission package"

```
"Format for NeurIPS submission. Include reproducibility checklist."
```
→ `venue-formatter` produces compiled PDF + checklist + disclosure

## Skill Composition

Skills hand off via `.ars-state/`. Common chains:

```
idea-forge → lit-scout → related-positioning → method-architect →
paper-writer → figure-smith → integrity-check → paper-reviewer →
venue-formatter
```

Each handoff is OPTIONAL — the user can stop, skip, or restart at any point.

For users who want enforced orchestration with checkpoints, see [`research-pipeline`](research-pipeline/).

## Supported Venues

`shared/venue_db/` ships YAML knowledge bases for:

- **NeurIPS** — main ML venue
- **ICLR** — OpenReview, multi-round rebuttal
- **ICML** — formal ML
- **ACL / EMNLP** — NLP, mandatory limitations + ethics
- **CVPR** — computer vision, 1-page rebuttal
- **AAAI** — broader AI
- **arXiv** — preprint

Each YAML has page limits, template URL, review format, disclosure policy, reproducibility checklist URL, broader-impact requirements.

## Design Principles

1. **Atomic over orchestrated** — every skill works on its own
2. **Natural language triggers** — no slash commands, no mode flags
3. **Block on integrity violations** — fabricated citations, unsupported claims, plagiarism
4. **Anti-sycophancy** — adversarial agents don't capitulate without ≥4/5 evidence
5. **Venue-aware** — page limits, disclosure, reproducibility from `shared/venue_db/`
6. **AI/ML specialized** — not a general academic toolkit; assumes AI venue conventions

## Documentation

- [`docs/COMMAND_INDEX.md`](docs/COMMAND_INDEX.md) — natural-language triggers per skill
- [`docs/AI_VENUE_GUIDE.md`](docs/AI_VENUE_GUIDE.md) — what each AI/ML venue expects
- [`docs/MIGRATION_v3_to_v4.md`](docs/MIGRATION_v3_to_v4.md) — moving from v3.3 to v4.0
- [`CHANGELOG.md`](CHANGELOG.md) — version history
- [`shared/`](shared/) — common agents, protocols, venue knowledge

## Status

- **Current**: v4.0.0 (2026-04) — BREAKING release
- **Deprecated** (kept until 2026-10): `academic-paper`, `academic-paper-reviewer`, `academic-pipeline`, `deep-research` as top-level skills (their agents remain as references for atomic skills above)

## License

See `LICENSE`.
