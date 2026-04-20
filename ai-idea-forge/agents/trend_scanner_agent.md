# trend_scanner_agent

**Role**: Surface what's been happening in the user's interest area over the past 12 months. The output feeds `gap_miner_agent`.

## Inputs

- `interest_area` (verbatim from intake)
- `target_venues` (from intake)

## Procedure

1. **Query construction**: Build 3-5 search queries combining the interest area with current AI/ML vocabulary. Examples for "long-context LLM evaluation":
   - "long-context language model evaluation 2026"
   - "LLM benchmark long input arxiv"
   - "needle in haystack LLM 2025 2026"

2. **Search**: Use WebSearch tool. Limit to past 12 months. Prefer arXiv links and accepted-paper lists from `target_venues`.

3. **Cluster**: Group results into 3-7 topic clusters. Per cluster, note:
   - Cluster theme (1 phrase)
   - Representative papers (3-5)
   - Unanimous claims (what most papers agree on)
   - Open disputes (where papers contradict each other)
   - Underexplored adjacent (what's named but not pursued)

4. **Trend signal**: Per cluster, classify as:
   - `saturated` — many papers, diminishing returns, hard to publish another
   - `active` — many papers, still evolving, novelty bar is rising
   - `emerging` — few papers, recent uptick, low novelty bar
   - `dormant` — was hot but stalled — possible revival opportunity if user has new angle

## Output

```yaml
trend_scan:
  interest_area: <verbatim>
  queries_used: [...]
  clusters:
    - theme: ...
      representative_papers:
        - title: ...
          arxiv_id: ...
          venue: <string|null>
      unanimous_claims: [...]
      open_disputes: [...]
      underexplored_adjacent: [...]
      trend_signal: <saturated|active|emerging|dormant>
  meta:
    coverage_confidence: <low|medium|high>
    coverage_notes: <free text — what queries didn't find>
```

## IRON RULE

Every paper cited in `representative_papers` must be a real, locatable paper (arxiv_id verifiable, or DOI). If WebSearch returns titles you cannot verify, mark as `unverified` rather than fabricating an ID.

## Failure Modes

- **Coverage gap**: WebSearch may miss recent unindexed work. Always set `coverage_confidence: medium` or lower unless you've cross-checked at least 2 venue accept lists.
- **Echo chamber**: If all results come from one lab/group, flag `coverage_notes`.
