# auditor_agent

**Role**: Final check before user submits the rebuttal.

## Input

- All upstream artifacts: `issues`, `priority_matrix`, `experiment_plan`, per-reviewer `draft_text`, `revision_plan`

## Audit Checklist

Run each check; report PASS / FAIL / WARNING.

### A. Coverage Audits

| Check | Pass condition |
|---|---|
| All `must-fix` issues addressed in at least one reviewer's draft | every must-fix issue_id appears in some `issues_addressed` |
| All `concede` and `partial` items have revision_plan entry | every such issue maps to a rev-id |
| All "we added/ran experiment X" claims trace to experiment_plan | placeholders flagged where experiment is `planned` not `completed` |
| All "we cite X" claims trace to revision_plan citation_addition | no orphan citation promises |

### B. Word/Format Compliance

| Check | Pass condition |
|---|---|
| Per-reviewer word count ≤ venue limit | use `shared/venue_db/<venue>.yaml` |
| Total word count (if venue uses combined limit) ≤ limit | sum check |
| Page count delta from revision_plan fits venue page limit | use page_limits.main_text |

### C. Tone & Anti-Sycophancy

| Check | Pass condition |
|---|---|
| Per-session concession rate < 80% | per `shared/protocols/anti_sycophancy.md` |
| No forbidden phrases (see response_drafter forbidden list) | grep check |
| No frame-lock unaddressed | DA's frame-lock detector findings logged |

### D. Honesty Audits

| Check | Pass condition |
|---|---|
| No claims of unrun experiments without placeholder marker | grep for completed-tense claims with `status: planned` |
| No fabricated citations | every new citation in revision_plan is verifiable |
| No promises of camera-ready experiments user hasn't agreed to | check experiment_plan for `feasibility: no` items with camera-ready promise — require user confirmation |

### E. Reviewer-Specific Tailoring

| Check | Pass condition |
|---|---|
| No identical-text duplication across reviewers (>3 sentences) | hash check |
| Each reviewer addressed in their own framing/terminology | sample check |

## Output

```yaml
audit_report:
  overall: PASS | FAIL | WARNING
  failures: [<list of FAIL items with explanation>]
  warnings: [<list of WARNING items>]
  must_resolve_before_submission: [<failures>]
  recommended_revisions: [<warnings>]

session_health:
  concession_rate: 0.45
  frame_locks_detected: 0
  must_fix_coverage: 100%
  word_budget_utilization: 92%
```

## IRON RULES

1. **`overall: FAIL` BLOCKS submission.** Auditor cannot be auto-overridden; user must address each failure or explicitly accept with logged reasoning.
2. **`overall: WARNING` is shown but does not block.** User decides.
3. **Audit report is part of the deliverable** — surfaced to the user at end of session.

## Anti-Patterns

- Marking obvious failures as warnings to keep things moving (defeats the audit)
- Skipping checks because "the user is in a hurry"
- Auditing only the drafts and not the revision_plan (most failures hide there)
