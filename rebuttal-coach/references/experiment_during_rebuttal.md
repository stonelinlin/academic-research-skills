# Experiments You Can Run During Rebuttal Window

Reference for experiment_planner_agent. Window assumed = 7-21 days depending on venue.

## Venue Rebuttal Windows (typical)

| Venue | Window | Compute reality |
|---|---|---|
| NeurIPS | ~10 days | Reasonable for ablations |
| ICLR | ~3 weeks (multi-round) | Most flexible |
| ICML | ~10 days | Tight |
| ACL/EMNLP | ~7 days | Very tight; bullet rebuttal |
| CVPR | ~5 days | Extremely tight; figures in rebuttal more than experiments |
| AAAI | ~7-10 days | Standard |

## Feasibility Heuristics

### Definitely Feasible (`yes`)

- Single ablation (one component on/off)
- Hyperparameter sensitivity (3-5 settings)
- Adding 1 baseline if pretrained weights are public
- Re-running experiment with different random seeds (variance estimate)
- Additional analysis on existing model outputs (no retraining)
- Failure case analysis on existing eval set

### Tight (`tight`)

- 2-3 ablations
- Adding 1 baseline requiring ≤24 hour fine-tune
- Scaling to 1 additional model size (assuming weights available)
- New eval on existing dataset

### Partial Feasibility (`partial`)

- Full ablation suite (5+ items) → run subset
- Cross-dataset evaluation → pick 1 representative
- Multiple model sizes → pick 2 (small + large)

### Infeasible (`no`)

- Pre-training a new model
- New large-scale dataset construction
- Theoretical proof requiring substantial new math
- Human evaluation requiring IRB approval
- Reproducing competitor's training pipeline from scratch
- Anything requiring access to data not currently available

## Common Reviewer Asks → Feasibility

| Reviewer ask | Typical feasibility |
|---|---|
| "Add ablation on component X" | yes (small component) / tight (large component) |
| "Compare to baseline X" | yes if X is open-weight + small / no if X is gated API + expensive / partial if can compare on subset |
| "Try larger model" | yes if next-size up exists / tight if requires scaling code changes |
| "Try smaller model" | yes |
| "Different dataset" | tight if dataset is similar in size+format / no if requires new preprocessing |
| "Statistical significance" | yes (rerun with seeds) |
| "Hyperparameter sensitivity" | yes |
| "Theoretical analysis" | partial (sketch) / no (full proof) |
| "Failure case discussion" | yes |
| "Different evaluation metric" | yes |
| "Human evaluation" | no (IRB / time) |

## What to Do When Infeasible

1. Acknowledge the request specifically (don't generalize)
2. Explain WHY infeasible (compute, time, access, IRB)
3. Offer the closest feasible alternative if possible
4. Acknowledge as a limitation in revised manuscript

> "Reproducing the [Competitor] pipeline from scratch is not feasible in the rebuttal window — their training code is not public and reproduction would require ~3 weeks of compute. We instead [closest alternative: e.g., compare on the published subset where their results are available]. We acknowledge this gap as a limitation in §6."

## What to Do When Mostly Feasible

> "We ran the requested ablation with similarity buckets {0.3, 0.5, 0.7, 0.9} (Table R1, attached). Results: accuracy drops from 91% (sim=0.3) to 53% (sim=0.9), a 38-point gap that supports the central claim."

Lead with the result number. Reviewers scan for numbers in rebuttals.
