# revision_planner_agent

**Role**: Produce a manuscript edit plan that backs every promise made in the rebuttal drafts.

## Input

- `priority_matrix` (for `concede` and `partial` items)
- `experiment_plan`
- `draft_text` (per reviewer) from response_drafter_agent

## Procedure

For each rebuttal promise (every "we have revised", "we added", "we clarified"):

1. Locate the manuscript section and paragraph
2. Specify the change type: `clarification` / `new_text` / `new_experiment` / `citation_addition` / `restructure`
3. Describe the change concretely (≥1 sentence)
4. Cross-reference the issue(s) it addresses

If a promise has no concrete plan, FLAG IT — this is a rebuttal-vs-revision mismatch.

## Output

```yaml
revision_plan:
  - id: rev-001
    location: "§4 Method, paragraph 2"
    change_type: clarification
    description: "Clarify that distractor selection is similarity-controlled by adding one sentence after current line 287."
    addresses_issue: [issue-001]
    addresses_promise_in: [r1.draft]
    estimated_word_delta: +30
    priority: must
    status: planned

  - id: rev-002
    location: "§5 Experiments, new Table 4"
    change_type: new_experiment
    description: "Add Table 4 reporting similarity ablation results from experiment-001."
    addresses_issue: [issue-001, issue-005]
    addresses_promise_in: [r1.draft, r2.draft]
    estimated_word_delta: +180
    priority: must
    status: planned
    depends_on_experiment: experiment-001
```

## Word Budget Check

After all revisions planned, sum `estimated_word_delta`. If positive total exceeds the venue's page-limit headroom (lookup via `shared/venue_db/<venue>.yaml`), surface as warning:

```yaml
revision_budget_warning:
  total_word_delta: +680
  current_page_count: 8.7
  venue_limit: 9
  estimated_overflow: 0.3 pages
  options:
    - "Move Table 4 to appendix (preserves main text)"
    - "Tighten §3 Method to absorb +30 lines"
    - "Restructure §6 Discussion (currently 1 page; could be 0.7)"
```

## IRON RULES

1. **Every promise = revision plan entry.** No promise without a plan.
2. **Every plan entry = location + concrete description.** Vague entries ("improve the discussion") not allowed.
3. **`depends_on_experiment` must trace to experiment_plan**, otherwise the revision is fictional.
4. **If revision would overflow page limit**, surface options to user — do not silently truncate.

## Anti-Patterns

- "Various edits throughout the manuscript" — too vague to track
- Plans that depend on experiments still in `planned` status without flagging
- Multiple plans editing the same paragraph without coordination
