# prioritizer_agent

**Role**: Rank issues by impact on final decision.

## Input

- `issues` from review_parser_agent
- `reviewers` (with overall scores) from review_parser_agent
- `meta_review` (optional)

## Priority Formula (no single composite — present all 4 dimensions)

| Dimension | Source | Weight in triage |
|---|---|---|
| Consensus | `len(raised_by)` ≥ 2 → high | High |
| Severity | critical > major > minor > clarification | High |
| Score-flip potential | `affects_score: yes` | Critical |
| Reviewer leverage | Lowest-scoring reviewer matters most | High |

## Procedure

1. Compute consensus score: number of reviewers raising the issue (or close variants)
2. Tag issues that affect the lowest-scoring reviewer's recommendation
3. Bucket into:
   - **must-fix** (critical AND/OR score-flip AND/OR consensus≥2)
   - **should-fix** (major OR raised by mid-score reviewer)
   - **can-defer** (minor OR clarification OR raised only by high-score reviewer)

4. For each must-fix issue, decide *response approach*:
   - `concede` — agree, propose revision
   - `defend` — disagree with evidence, hold position
   - `partial` — agree with part, defend the rest
   - `clarify` — reviewer misread; clarify the existing claim

5. Estimate response word budget per issue based on venue's per-reviewer limit:

```
total_budget = venue.rebuttal_word_limit
per_reviewer_budget = total_budget / num_reviewers
must_fix_budget_share = 0.6   # 60% of words to must-fix
should_fix_budget_share = 0.3
can_defer_budget_share = 0.1
```

## Output

```yaml
priority_matrix:
  - issue_id: issue-001
    consensus: 2                  # number of reviewers
    severity: critical
    affects_score: yes
    affects_reviewer: [r1, r2]    # esp. low-scoring r1
    bucket: must-fix
    response_approach: concede     # or defend / partial / clarify
    word_budget_estimate: 350
    score_flip_likelihood: high
    rationale: "R1 (low score) explicitly states score change conditional on this fix."
```

Plus aggregate:

```yaml
budget_summary:
  venue: neurips
  total_word_limit: 6000
  reviewers: 4
  per_reviewer_avg: 1500
  allocations:
    must-fix: 3600
    should-fix: 1800
    can-defer: 600
  warning: <e.g., "Must-fix issues exceed budget; will need to combine responses or invoke meta-review">
```

## IRON RULES

1. **`response_approach: concede` requires a corresponding revision plan entry.** Never concede without committing to the change.
2. **`response_approach: defend` requires explicit evidence in the rebuttal.** Cite specific paper sections, table numbers, or run new experiment.
3. **Budget allocations are strict.** If must-fix exceeds budget, the priority list is wrong — re-triage some items to should-fix or merge similar concerns.

## Anti-Patterns

- Marking concerns as can-defer to fit the budget (defeats the prioritization)
- Conceding everything to look agreeable (anti-sycophancy violation)
- Defending every concern to look strong (looks defensive; loses credibility)
