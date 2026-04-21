# Integrity Protocol (consolidated reference)

**Status**: v4.0 — Index of canonical protocol files under `shared/references/` (v4 copies; do not link into `archive/v3/` from v4 skills).

## Scope

Citation, claim, data, and reproducibility verification. Used by `ai-integrity-check` skill (primary consumer) and invoked optionally by `ai-paper-reviewer` and `ai-rebuttal-coach`.

## Component References

| Concern | Authoritative Reference | Owned by |
|---|---|---|
| 5-phase citation/claim verification | [`../references/integrity_review_protocol.md`](../references/integrity_review_protocol.md) | ai-integrity-check |
| 7-mode AI research failure checklist | [`../references/ai_research_failure_modes.md`](../references/ai_research_failure_modes.md) | ai-integrity-check + ai-paper-reviewer |
| Claim extraction & source tracing | [`../references/claim_verification_protocol.md`](../references/claim_verification_protocol.md) | ai-integrity-check |
| Plagiarism / self-plagiarism / AI-text detection | [`../references/plagiarism_detection_protocol.md`](../references/plagiarism_detection_protocol.md) | ai-integrity-check |
| Semantic Scholar API verification | [`../references/semantic_scholar_api_protocol.md`](../references/semantic_scholar_api_protocol.md) | ai-lit-scout + ai-integrity-check |
| Anti-leakage (knowledge isolation) | [`../references/anti_leakage_protocol.md`](../references/anti_leakage_protocol.md) | ai-paper-writer |
| VLM figure verification | [`../references/vlm_figure_verification.md`](../references/vlm_figure_verification.md) | ai-figure-smith |
| Reproducibility audit | [`../references/reproducibility_audit.md`](../references/reproducibility_audit.md) | ai-integrity-check |
| Material Passport schema | [`shared/handoff_schemas.md`](../handoff_schemas.md) Schema 9 | ai-integrity-check |
| Repro lock | [`shared/artifact_reproducibility_pattern.md`](../artifact_reproducibility_pattern.md) | ai-integrity-check |

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

Unlike v3, where integrity ran only inside the pipeline at Stage 2.5/4.5, v4.0 lets users invoke `ai-integrity-check` directly:

```
"Check citations in this paper"
"Verify the claims in §4"
"Run failure mode checklist on my draft"
```

The skill auto-detects scope (whole paper, single section, single claim list) and chooses the right mode.
