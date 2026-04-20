# 3-Axis Positioning Taxonomy (Detailed)

The triage_agent classifies each candidate paper on three orthogonal axes. This file expands the definitions with examples.

## Method Axis

**Question**: Are the algorithmic approaches in the same family?

| Value | Definition | Example (vs paper proposing "rotary embeddings for length extrapolation") |
|---|---|---|
| same | Same algorithmic family AND same key components | Another paper using rotary embeddings for length extrapolation |
| similar | Same family, one or more components different | Rotary + new interpolation scheme |
| different | Different family but tackles same problem | ALiBi for length extrapolation (different positional scheme) |
| orthogonal | Different problem entirely | Paper on retrieval-based long context (no positional encoding focus) |

## Data Axis

**Question**: Same evaluation setting?

| Value | Definition | Example |
|---|---|---|
| same | Identical benchmark | Both report on RULER 32K |
| overlapping | Different benchmark, same task | One uses RULER, other uses LongBench v2 — both long-context QA |
| disjoint | Different task | One on long-context QA, other on long-context summarization |

## Claim Axis

**Question**: What scientific finding does the paper make?

| Value | Definition | Example |
|---|---|---|
| same | Same scientific finding | Both: "Models degrade past 32K due to positional decay" |
| adjacent | Related but distinguishable | One: positional decay; other: attention dilution |
| orthogonal | Different finding | One: positional decay; other: chain-of-thought helps |
| contradictory | Claims the opposite | One: long-context > RAG; other: RAG > long-context |

## Composite — Competition Intensity

| Method × Data × Claim | Intensity |
|---|---|
| same/similar × same/overlapping × same/adjacent | **direct** — strongest competitor |
| any × any × contradictory | **direct** — must address |
| same/similar × disjoint × any | **adjacent** — methodologically related |
| different/orthogonal × any × same | **adjacent** — convergent finding from different angle |
| different/orthogonal × any × adjacent/orthogonal | **orthogonal** — useful background |
| orthogonal × disjoint × orthogonal | **none** — likely skip |

## Edge Cases

### Case: Concurrent work
A paper posted to arXiv within ±2 months of your submission, on overlapping topic.
- Treat as `direct` if intensity would be direct
- Use the concurrent-work phrasing pattern (see `concurrent_work_protocol.md`)
- DO NOT use "concurrent work" as escape from comparison

### Case: Your own prior work
- Treat as `direct` (strong overlap with self)
- Self-citation is required to establish lineage
- Be ESPECIALLY careful with self-plagiarism check (`integrity-check`)

### Case: Survey paper covering your area
- Method axis: orthogonal (surveys don't propose methods)
- Data axis: orthogonal
- Claim axis: orthogonal
- Cite as foundational background; not a competitor

### Case: Industry technical report (not peer-reviewed)
- Score on the same axes regardless of venue
- Note in `differentiation_pitch` if peer-review status is relevant
- Some venues (like CVPR) treat tech reports as concurrent work; others don't
