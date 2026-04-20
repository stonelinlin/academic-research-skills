# Concession Protocol — When to Agree vs Hold Position

Inherits from `shared/protocols/anti_sycophancy.md`. This file is rebuttal-specific guidance.

## Default Posture

Hold position unless the reviewer's concern scores ≥4/5 on the rubric below.

## Concession Rubric (1-5)

Per `shared/protocols/anti_sycophancy.md`. Reproduced here for rebuttal context:

| Score | Reviewer concern... | Response |
|---|---|---|
| 1 | Misreads the paper, no new information | Clarify; do not concede |
| 2 | Has stylistic preference but not substantive | Brief acknowledgment; minor revision |
| 3 | Identifies real but minor gap | Concede the gap; revision plan |
| 4 | Identifies substantial gap with clear evidence | Concede; commit to fix; new experiment if needed |
| 5 | Identifies fundamental flaw with decisive evidence | Major concession; potentially withdraw or restructure paper |

## When to Concede (score ≥4)

- Acknowledge directly: "We agree this is a gap."
- Specify the fix: experiment, new analysis, restructure, scope tightening
- Add to revision_plan with concrete location

## When to Defend (score 1-3)

- Acknowledge briefly that the concern was raised
- Provide evidence: section number, table reference, or new analysis
- Do NOT concede ground you don't need to lose
- Be respectful; do not call out the misreading explicitly

## Mixed (Partial Concession)

Many concerns are partially valid. Pattern:

> "We agree that [the valid part], and have addressed it by [action]. However, regarding [the invalid part], we point to §[X] which shows [counter-evidence]."

This is honest and avoids fence-sitting.

## Frame-Lock Defense (score-independent)

If the reviewer redefines your claim narrower or broader than what the paper says:

1. State the paper's actual claim verbatim
2. Note that the reviewer's framing differs
3. Either accept the broader/narrower framing AND adjust the claim in revision, OR defend the original framing

```
Pattern: "Our paper claims [X] (see Abstract and §1). The reviewer's reading suggests we claim [Y]. We did not intend to claim [Y]; we have rewritten the Introduction to make this distinction clearer. The original claim [X] is supported by [evidence]."
```

## Cross-Reviewer Conflicts

When R1 and R2 want opposite things:

| Pattern | How to handle |
|---|---|
| R1 wants more of X, R2 wants less | Pick the side with stronger evidence; address the other in revision_plan as "scope tradeoff" |
| R1 wants more theory, R2 wants more experiments | Usually means paper is unbalanced; AC will weight by venue |
| R1 wants different framing, R2 likes current framing | Defend current framing; offer R1 an additional explanation in §1 |

DO NOT promise both reviewers that you'll satisfy them — they read each other's responses on OpenReview.

## Concession Rate Health Check

Per `shared/protocols/anti_sycophancy.md`, target concession rate is 20-50% of issues across the rebuttal.

- < 20%: Likely defending too much; some legitimate concerns being dismissed
- 20-50%: Healthy
- > 50%: Sycophancy risk; too much agreement may signal you don't trust your own paper

auditor_agent reports the actual rate.
