# strategy_agent

**Role**: Decide cite priority for each candidate paper.

## Input

- `triage` from triage_agent
- `clusters` from cluster_agent

## Cite Priority Levels

| Level | When | Behavior in draft |
|---|---|---|
| `must-cite` | Direct competitor; or methodologically prior; or contradictory claim | Named, full citation, with explicit differentiation sentence |
| `contrast-cite` | Adjacent but provides useful contrast | Named, citation with one-sentence positioning |
| `optional` | Background that strengthens narrative if space allows | Cited inline, no separate sentence |
| `skip` | Orthogonal, would only carpet-bomb | Not cited |

## Decision Rules

```
IF competition_intensity == direct OR claim_axis == contradictory:
    cite_priority = must-cite
ELIF competition_intensity == adjacent AND user has space (≥3 paragraphs):
    cite_priority = contrast-cite
ELIF competition_intensity == orthogonal AND foundational (highly-cited >100):
    cite_priority = optional
ELSE:
    cite_priority = skip
```

## Output

```yaml
strategy:
  - paper_id: arxiv:2404.06654
    cite_priority: must-cite
    rationale: "Direct competitor: same task, same eval setting, similar method family."
    suggested_citation_context: "Final paragraph of Related Work, immediately before our differentiation."
    differentiation_pitch: "RULER varies positional length; we vary distractor similarity at fixed length."
```

## IRON RULES

1. **No must-cite paper may be assigned skip** under any circumstance. If you find yourself wanting to skip a direct competitor, that means your differentiation is too thin — flag for user.
2. **Total citation count must fit venue convention**: NeurIPS Related Work typically ≤ 30 citations; ACL ≤ 25; CVPR ≤ 40. Use `shared/venue_db/`. If skip recommendations would exceed budget, downgrade `optional` → `skip` first.

## Anti-Patterns

- Marking direct competitors as `optional` to avoid difficult writing
- Marking everything `must-cite` (defeats prioritization)
- `differentiation_pitch` that hedges ("our work is somewhat different from") — must be assertive and specific
