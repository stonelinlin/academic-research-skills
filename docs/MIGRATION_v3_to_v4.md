# Migration: v3.3 → v4.0

v4.0 is a **BREAKING release**. This guide maps the old structure to the new one.

## TL;DR

- 4 large skills (`deep-research` / `academic-paper` / `academic-paper-reviewer` / `academic-pipeline`) → **10 atomic skills + 1 optional meta-skill**
- 24 explicit modes → **0 explicit modes** (sub-modes auto-detected from inputs)
- General academic (HEI default) → **AI/ML specialized** (NeurIPS/ICLR default)
- 547-line SKILL.md → **≤200-line SKILL.md per atomic skill** (CI enforced post-migration)
- 7-10 mandatory checkpoints → **3 mandatory in `research-pipeline` (optional skill)**

## Skill Mapping

| v3.3 skill / mode | v4.0 atomic skill | Notes |
|---|---|---|
| `deep-research full` | `lit-scout` (comprehensive) + `idea-forge` + `method-architect` | Split by intent |
| `deep-research quick` | `lit-scout` (quick) | Just literature |
| `deep-research lit-review` | `lit-scout` (standard or comprehensive) | Direct mapping |
| `deep-research fact-check` | `integrity-check` | Promoted to first-class skill |
| `deep-research socratic` | shared/agents/socratic_mentor invoked by `idea-forge` / `lit-scout` | No longer a mode |
| `deep-research systematic-review` | `lit-scout` (comprehensive) + `integrity-check` | Composition |
| `deep-research paper-review` | `paper-reviewer` (mode: full) | Direct mapping |
| `academic-paper full` | `paper-writer` + `figure-smith` + `venue-formatter` | Split by deliverable |
| `academic-paper plan` | `paper-writer` (outline mode) | Auto-detected |
| `academic-paper outline` | `paper-writer` (outline mode) | Same |
| `academic-paper revision` | `paper-writer` (revise mode) | Auto-detected from `existing_draft` |
| `academic-paper revision-coach` | `paper-writer` (polish mode) + Socratic | Auto-detected |
| `academic-paper abstract` | `paper-writer` with `section: abstract` | Just an input |
| `academic-paper lit-review` | `lit-scout` + `paper-writer` | Composition |
| `academic-paper format-convert` | `venue-formatter` | Direct mapping |
| `academic-paper citation-check` | `integrity-check` | Promoted |
| `academic-paper disclosure` | `venue-formatter` (disclosure block) | Folded in |
| `academic-paper-reviewer full` | `paper-reviewer` (mode: full) | Direct |
| `academic-paper-reviewer quick` | `paper-reviewer` (mode: quick) | Direct |
| `academic-paper-reviewer methodology-focus` | `paper-reviewer` (mode: methodology-focus) | Direct |
| `academic-paper-reviewer re-review` | `paper-reviewer` (mode: re-review) | Direct |
| `academic-paper-reviewer socratic-guided` | `paper-reviewer` invoking shared/socratic | Direct |
| `academic-paper-reviewer calibration` | `paper-reviewer` (mode: calibration) | Direct |
| `academic-pipeline` (full) | `research-pipeline` | Demoted to optional meta-skill |

## New in v4.0 (no v3.3 equivalent)

| Skill | Why new |
|---|---|
| `idea-forge` | Idea generation was buried in `deep-research` socratic mode; now first-class |
| `related-positioning` | Positioning was implicit in `paper-writer` lit-review; now explicit + threat-model |
| `rebuttal-coach` | Rebuttal handling was missing entirely from v3.3 |

## Data / Output Mapping

| v3.3 artifact | v4.0 artifact | Location |
|---|---|---|
| `intake_brief.yaml` | Per-skill intake (`idea-forge.intake`, `lit-scout.intake`, etc.) | Per-skill state |
| `RQ_brief.yaml` | `idea-forge` Idea Card + `method-architect` hypothesis | Various |
| `annotated_bibliography.yaml` | `lit-scout` output (same name) | `lit-scout` |
| `material_passport.yaml` | `integrity-check` Material Passport | `integrity-check` |
| `integrity_audit.yaml` | `integrity-check` audit_report | `integrity-check` |
| `paper_draft.tex` | `paper-writer` section drafts → `venue-formatter` compile | Sequential |
| `review_report.yaml` | `paper-reviewer` reports | `paper-reviewer` |
| `rebuttal.md` | `rebuttal-coach` per-reviewer drafts | `rebuttal-coach` |

## Domain Changes

| v3.3 | v4.0 |
|---|---|
| Domain default: HEI (higher education) | Domain default: AI/ML |
| Paper structures: IMRaD, case-study, policy-brief, theoretical, systematic-review | Paper structures: Method-Experiments-RelatedWork-Discussion, position, benchmark |
| Bilingual EN-ZH abstracts mandatory | Bilingual abstracts optional (English default for AI venues) |
| Citation styles: APA, MLA, Chicago, IEEE | Citation styles: ACM, IEEE, neurips/iclr/icml-bibtex (others available but uncommon) |
| Default venues: vague | Default venues: NeurIPS, ICLR (configurable per `shared/venue_db/`) |

## What Got Deleted

| Removed | Why |
|---|---|
| `MODE_REGISTRY.md` | No more explicit modes |
| `POSITIONING.md` (skill positioning) | Folded into README + COMMAND_INDEX |
| `docs/ARCHITECTURE.md` (full pipeline arch) | Pipeline is optional now; arch in `research-pipeline/SKILL.md` |
| Most "case study" / "policy brief" templates | Out of AI/ML scope |
| HEI-specific examples and vocab | Out of AI/ML scope |
| `socratic_mentor_agent.md` (×2 copies in deep-research and academic-paper) | Consolidated to `shared/agents/socratic_mentor.md` |
| `devils_advocate_agent.md` (×2 copies) | Consolidated to `shared/agents/devils_advocate.md` |

## Backward Compatibility (6-month window)

Until 2026-10:
- v3.3 top-level skills (`deep-research`, `academic-paper`, `academic-paper-reviewer`, `academic-pipeline`) remain as **read-only references**. Their agent files are still pointed to by v4.0 atomic skills (e.g., `lit-scout` references `deep-research/agents/bibliography_agent.md`).
- v3.3 trigger phrases like "deep research" or "academic paper" will route to the closest v4.0 atomic skill with a one-line migration notice.
- After 2026-10, v3.3 directories will be moved to `legacy/` and triggers removed.

## Migration Steps for Active Users

If you have ongoing v3.3 sessions:

1. **In-flight pipeline**: Complete current stage; resume v4.0 from corresponding atomic skill (use the table above)
2. **Custom modes you relied on**: Open issue if your mode isn't covered; we'll add explicit override or sub-mode
3. **State files in v3.3 format**: One-time conversion script: `scripts/migrate_v3_state_to_v4.py` (TODO — not shipped in initial v4.0; coming in v4.0.1)

## Why the Change

User feedback in research design phase identified four pain points:

1. Entry complexity (24 modes × 4 skills was hard to navigate)
2. Verbose docs (547-line SKILL.mds buried critical rules)
3. Tedious checkpoints (7-10 confirmations per pipeline run)
4. Lack of AI/ML specialization (HEI defaults didn't match user's domain)

v4.0 addresses all four:

| Pain | Fix |
|---|---|
| Entry complexity | 10 atomic skills, no modes; natural-language triggers |
| Verbose docs | ≤200 lines per SKILL.md (CI-enforced post-migration) |
| Tedious checkpoints | Atomic skills have 0 checkpoints; meta-skill has 3 |
| Domain mismatch | AI/ML venue_db; AI/ML structures; default venues NeurIPS/ICLR |

## Questions / Issues

Open an issue with `migration` label.
