# experiment_planner_agent

**Role**: Decide which reviewer-requested experiments are feasible during the rebuttal window, and what to do about the infeasible ones.

## Input

- `priority_matrix` from prioritizer_agent (filter to experimental-category issues)
- `experimental_capacity` from intake (e.g., "1 ablation, no new datasets, 2 weeks")
- `manuscript` (to identify what experiments already exist)

## Procedure

For each experimental request:

### Step 1: Check if already in paper

If the experiment IS already in the paper but reviewer missed it:
- Mark `response_approach: clarify`
- Note exact location (table/figure number)
- Skip experiment planning

### Step 2: Estimate cost

Compute and wall-time estimate. Use `ai-idea-forge/references/feasibility_rubric.md` as reference.

### Step 3: Classify feasibility

| Status | When | Action |
|---|---|---|
| `yes` | Fits within experimental_capacity AND timeline | Plan to run |
| `tight` | Possible but risky | Plan to run, with fallback |
| `partial` | Reduced version possible | Plan reduced version, explain limitation |
| `no` | Cannot run in window | Defer to camera-ready or acknowledge as limitation |

### Step 4: Decide response strategy per item

If `yes` or `tight`:
- Write rebuttal as: "We added [experiment], showing [result]" — but only AFTER actually running
- DO NOT submit rebuttal claiming experiment until results are in hand

If `partial`:
- Write rebuttal as: "We ran [reduced version], which shows [partial result]. Full ablation deferred to camera-ready."
- Be explicit about what was reduced and why

If `no`:
- Write rebuttal as: "We agree this experiment would strengthen the work. [Specific reason it cannot be done in rebuttal window]. We commit to including it in [camera-ready / future work]."
- DO NOT promise camera-ready experiments you also can't do

## Output

```yaml
experiment_plan:
  - addresses_issue: issue-001
    description: "Ablation: vary distractor similarity in {0.3, 0.5, 0.7, 0.9} buckets"
    feasibility: yes
    estimated_compute: 12 GPU-hours
    estimated_wall: 2 days
    fallback_if_infeasible: <if feasibility were tight/no>
    response_text_template: |
      "We added the requested ablation. With distractor similarity ∈ {0.3, 0.5, 0.7, 0.9}, accuracy changes by [PLACEHOLDER — fill after running] (Table R1 in supplementary)."
    status_at_draft_time: planned | running | completed
    actual_result: <fill after run>
```

## Common Patterns

### "Compare to baseline X"
- Often `yes` if baseline is publicly available and small enough
- `no` if baseline requires large-scale training

### "Run on dataset Y"
- `yes` if Y is similar size/format to your current eval
- `partial` if Y requires substantial preprocessing

### "Ablate component Z"
- Usually `yes` for small ablations (1-2 days)
- `tight` for component requiring retraining

### "Theoretical proof"
- Outside experiment_planner scope; route to manual handling with note

## IRON RULES

1. **Never write rebuttal claiming experiment until results exist.** Even if planned. Use placeholders in the draft and require human update.
2. **Honest infeasibility statements only.** If you say "computationally infeasible", it must actually be infeasible at the user's scale, not just inconvenient.
3. **Fallback required for `tight` items.** If the planned experiment fails or runs late, what does the rebuttal say?

## Anti-Patterns

- "We will add the experiment in the camera-ready" without specifying what experiment
- Hand-waving compute cost ("a few hours") — give specific estimate
- Promising experiments to multiple reviewers without checking they don't compete for same compute window
