# Integrity Protocol (consolidated reference)

**Status**: v4.0 — Index pointing to existing v3.3 integrity infrastructure (which is solid). No content duplication.

## Scope

Citation, claim, data, and reproducibility verification. Used by `integrity-check` skill (primary consumer) and invoked optionally by `paper-reviewer` and `rebuttal-coach`.

## Component References

| Concern | Authoritative Reference | Owned by |
|---|---|---|
| 5-phase citation/claim verification | [`archive/v3/academic-pipeline/references/integrity_review_protocol.md`](../../archive/v3/academic-pipeline/references/integrity_review_protocol.md) | integrity-check |
| 7-mode AI research failure checklist | [`archive/v3/academic-pipeline/references/ai_research_failure_modes.md`](../../archive/v3/academic-pipeline/references/ai_research_failure_modes.md) | integrity-check + paper-reviewer |
| Claim extraction & source tracing | [`archive/v3/academic-pipeline/references/claim_verification_protocol.md`](../../archive/v3/academic-pipeline/references/claim_verification_protocol.md) | integrity-check |
| Plagiarism / self-plagiarism / AI-text detection | [`archive/v3/academic-pipeline/references/plagiarism_detection_protocol.md`](../../archive/v3/academic-pipeline/references/plagiarism_detection_protocol.md) | integrity-check |
| Semantic Scholar API verification | [`archive/v3/deep-research/references/semantic_scholar_api_protocol.md`](../../archive/v3/deep-research/references/semantic_scholar_api_protocol.md) | lit-scout + integrity-check |
| Anti-leakage (knowledge isolation) | [`archive/v3/academic-paper/references/anti_leakage_protocol.md`](../../archive/v3/academic-paper/references/anti_leakage_protocol.md) | paper-writer |
| VLM figure verification | [`archive/v3/academic-paper/references/vlm_figure_verification.md`](../../archive/v3/academic-paper/references/vlm_figure_verification.md) | figure-smith |
| Reproducibility audit | [`archive/v3/academic-pipeline/references/reproducibility_audit.md`](../../archive/v3/academic-pipeline/references/reproducibility_audit.md) | integrity-check |
| Material Passport schema | [`shared/handoff_schemas.md`](../handoff_schemas.md) Schema 9 | integrity-check |
| Repro lock | [`shared/artifact_reproducibility_pattern.md`](../artifact_reproducibility_pattern.md) | integrity-check |

## Two Modes

| Mode | When | Coverage | Behavior on FAIL |
|---|---|---|---|
| `pre-review` | Before sending paper to reviewers | 30% sample of claims (min 10) | Block: fix and re-verify, max 3 rounds |
| `final-check` | After all revisions, before submission | 100% of claims | Block (zero tolerance) |

## Block-on-Suspect Rule

If ANY of the 7 failure modes is `SUSPECTED`, or Modes 1/3/5/6 are `INSUFFICIENT EVIDENCE`, the protocol BLOCKS. There is no `--no-block` escape hatch. User override requires:

1. Explicit reasoning written by the user
2. Logged in `outputs/integrity_override_log.md`
3. Surfaced again at submission time

## v4.0 Atomic Invocation

Unlike v3, where integrity ran only inside the pipeline at Stage 2.5/4.5, v4.0 lets users invoke `integrity-check` directly:

```
"Check citations in this paper"
"Verify the claims in §4"
"Run failure mode checklist on my draft"
```

The skill auto-detects scope (whole paper, single section, single claim list) and chooses the right mode.
