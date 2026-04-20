# cluster_agent

**Role**: Group candidate papers into competitive clusters that map to Related Work paragraphs.

## Input

`triage` output from triage_agent.

## Procedure

1. **Direct competitors** → cluster A. These need the most careful framing.
2. **Adjacent works** → cluster by sub-theme (typically 2-4 sub-clusters).
3. **Orthogonal but cited** → cluster B (background / related-but-distant).
4. **Skip** → set aside (will be cite_priority: skip in strategy).

## Clustering Heuristics

- Aim for 3-5 final clusters total (matches typical Related Work paragraph count)
- Each cluster ≤ 5 papers (more = carpet-bombing)
- Direct competitors should be in their own cluster, not mixed with adjacent

## Output

```yaml
clusters:
  - cluster_id: A
    label: "Direct competitors on long-context retrieval eval"
    papers: [arxiv:2404.06654, arxiv:2412.15204]
    suggested_paragraph_position: 1   # first or last paragraph for direct competitors
    target_word_count: 150-250

  - cluster_id: B
    label: "Adjacent — RAG benchmarks"
    papers: [arxiv:..., arxiv:...]
    suggested_paragraph_position: 2
    target_word_count: 100-180
```

## Heuristics for Paragraph Position

| Position | Use for |
|---|---|
| First | Setting up the problem (foundational related work) |
| Middle | Adjacent themes, supporting context |
| Last | Direct competitors with strong differentiation (so reader leaves with your framing fresh) |

## Anti-Patterns

- More than 5 clusters → reader can't track
- Single cluster with 10+ papers → carpet-bombing, no narrative
- Direct competitors mixed with background → buries the differentiation
