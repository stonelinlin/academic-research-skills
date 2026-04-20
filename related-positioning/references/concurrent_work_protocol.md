# Concurrent Work Protocol

## Definition

A paper qualifies as "concurrent work" if:
- arXiv-dated within ±2 months of your earliest public release (arxiv preprint, blog post, or submission)
- Tackles the same or directly overlapping problem
- Was not available to you during your method development

## Why It Matters

Reviewers are skeptical of "concurrent work" claims because they're sometimes used as an excuse to skip differentiation. You need to demonstrate:

1. The paper genuinely was published after you started work
2. You still cite it (concurrent ≠ ignorable)
3. Your work makes a meaningfully different contribution

## Phrasing Patterns

### Pattern A: Same finding, independent verification

> "Concurrent work by [Author et al., 2026] independently arrives at a similar conclusion using [different method/dataset]. The convergence strengthens the finding; we differ from their approach in [specific axis]."

Use when: claim_axis = same, but you took different paths to get there.

### Pattern B: Adjacent contribution

> "Concurrent work by [Author et al., 2026] addresses [related but distinct] aspect of the same problem; their work focuses on [their angle], while ours focuses on [your angle]."

Use when: claim_axis = adjacent.

### Pattern C: Method-similarity, different application

> "Concurrent work by [Author et al., 2026] employs a similar [method family] for [different task/setting]; we extend it to [your setting] and contribute [your specific addition]."

Use when: method_axis = similar, data_axis = disjoint.

## Anti-Pattern

> ~~"Concurrent work [Author et al., 2026] also addresses this problem; we leave detailed comparison to future work."~~

This will get the paper rejected. If concurrent work is direct competitor, you MUST:
- Either run an experimental comparison if feasible (post-hoc but acceptable for camera-ready)
- OR explicitly acknowledge the limitation and explain why comparison was infeasible (incompatible code, different dataset access, etc.)

## How to Verify Concurrent Status

When user claims a paper is concurrent:

1. Check arxiv-id submission date
2. Compare with user's first public release (arxiv, openreview, blog)
3. If gap > 2 months, the work is NOT concurrent — strategy_agent should treat it as standard prior work

## Output Marker

When concurrent work is identified, mark in positioning_matrix.csv:

```
concurrent_work=true,arxiv_date=2026-MM-DD,user_release_date=2026-MM-DD
```
