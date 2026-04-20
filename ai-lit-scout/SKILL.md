---
name: ai-lit-scout
description: "AI/ML literature search, verification, and annotated bibliography. Inputs: research question or topic + venue tags + recency constraint. Outputs: verified citations (Semantic Scholar / arxiv), per-paper annotation (claim, method, evidence quality), citation graph, gap notes. Triggers: literature review, find papers, search related work, citation search, build bibliography, 文献调研, 查找论文, 文献综述, 找相关工作."
metadata:
  version: "4.1.0"
  domain: ai-ml
  data_access_level: redacted
  task_type: outcome-gradable
  related_skills:
    - ai-idea-forge
    - ai-related-positioning
    - ai-integrity-check
    - ai-paper-writer
---

# ai-lit-scout — AI/ML Literature Scout

Find, verify, and annotate the literature you need to cite. Specialized for AI/ML venues (arxiv-heavy citation culture, Semantic Scholar integration, fast trend turnover).

## 30-Second Start

```
"Find recent literature on long-context LLM evaluation since 2024."
"Build a bibliography for diffusion editing methods, ICLR/CVPR papers."
"Verify these 12 citations and add 5 missing key papers."
"做一份 mechanistic interpretability 的文献综述，2025 年以来。"
```

## When to Use

| Use ai-lit-scout when | Use a different skill when |
|---|---|
| You need to find papers in an area | You already have papers and need to position → `ai-related-positioning` |
| You need verified citations for a draft | You need to check citations in existing draft → `ai-integrity-check` |
| You're building an annotated bibliography | You need to write the related work prose → `ai-related-positioning` |

## Inputs

| Field | Required | Example |
|---|---|---|
| `topic` or `research_question` | yes | "long-context LLM evaluation under semantic interference" |
| `target_venues` | recommended | `[neurips, iclr, acl]` |
| `recency` | recommended | "since 2024" or "all time" |
| `existing_bibliography` | optional | Citations you already have (will be verified + extended) |
| `depth` | optional | `quick` (~10 papers, 1-2 turns) / `standard` (~25 papers) / `comprehensive` (~50 papers, systematic review territory) |
| `style` | optional | `narrative-bibliography` / `csv-table` / `bibtex` / `risis` |

## Outputs

### 1. Annotated Bibliography

```yaml
- citation:
    title: ...
    authors: [...]
    venue: ...
    year: ...
    arxiv_id: ...
    doi: ...
    citation_count: <int — from semantic scholar>
  annotation:
    one_line_claim: <verb-led summary of the paper's main claim>
    method: <1-2 sentences>
    evidence_quality: high | medium | low
    key_finding: <1 sentence>
    relation_to_topic: foundational | direct | adjacent | background | tangential
  verification:
    api_verified: yes | no | partial
    api_source: semantic_scholar | arxiv | manual
    cross_check_passed: yes | no
```

### 2. Citation Graph (optional)

When `depth: comprehensive`:
- Co-citation clusters
- Highly-cited foundational papers in the area
- Recent trend nodes

### 3. Gap Notes

Areas where the literature is thin or contested — feeds `ai-idea-forge` and `ai-related-positioning`.

## Workflow

```mermaid
flowchart TD
    Intake[Intake: topic + venue + recency + depth]
    Search[Multi-source search: Semantic Scholar + arxiv + WebSearch]
    Filter[Filter: venue match + recency + relevance threshold]
    Verify[Verify: API cross-check titles + DOIs + arxiv-IDs]
    Annotate[Annotate: claim + method + evidence quality]
    Cluster[Cluster (optional): citation graph + co-citation]
    Gap[Identify literature gaps]
    Output[Annotated Bibliography + Gap Notes]

    Intake --> Search --> Filter --> Verify --> Annotate --> Cluster --> Gap --> Output
```

## Agents (delegated to existing v3 components)

| Agent | Role | File |
|---|---|---|
| `bibliography_agent` | Multi-source search, verification, annotation | [`archive/v3/deep-research/agents/bibliography_agent.md`](../archive/v3/deep-research/agents/bibliography_agent.md) |
| `source_verification_agent` | Cross-check titles, DOIs, citation counts | [`archive/v3/deep-research/agents/source_verification_agent.md`](../archive/v3/deep-research/agents/source_verification_agent.md) |
| `socratic_mentor` (shared) | Used when topic is too vague | [`shared/agents/socratic_mentor.md`](../shared/agents/socratic_mentor.md) |

## Key Protocols

- [`archive/v3/deep-research/references/semantic_scholar_api_protocol.md`](../archive/v3/deep-research/references/semantic_scholar_api_protocol.md) — Semantic Scholar verification
- [`archive/v3/deep-research/references/cross_agent_quality_definitions.md`](../archive/v3/deep-research/references/cross_agent_quality_definitions.md) — citation hygiene + verification thresholds
- [`shared/protocols/integrity_protocol.md`](../shared/protocols/integrity_protocol.md) — verification routing

## IRON RULES

1. **No fabricated citations.** Every entry must be API-verified or marked `api_verified: no` with explicit rationale.
2. **No paraphrased titles.** Titles must be VERBATIM from the source.
3. **Citation count must come from API**, not estimated.
4. **Annotations must reference the abstract or paper at minimum** — never invent claims.
5. **arXiv ID format check.** All arxiv-IDs must match `\d{4}\.\d{4,5}` and resolve.

## Anti-Patterns

| # | Anti-Pattern | Correct Behavior |
|---|---|---|
| 1 | "Smith et al. 2020 showed X" without verification | Verify the year and the claim |
| 2 | Annotating from title only | Read at least the abstract |
| 3 | Inflating relevance ("foundational") for marginal papers | Use `relation_to_topic` honestly |
| 4 | Topping out at 10 papers when topic deserves 30 | Adjust `depth` and re-run |
| 5 | Mixing peer-reviewed and preprint without flagging | Set `venue: arxiv-only` for preprints |

## Resume / Handoff

Standard `state_tracker` handoff:

- Annotated bibliography → `ai-related-positioning` (for differentiation analysis)
- Annotated bibliography → `ai-paper-writer` (for citation insertion)
- Gap notes → `ai-idea-forge` (for new directions)

## Modes (lightweight)

| Mode | When auto-engaged | Behavior |
|---|---|---|
| `quick` | depth=quick OR ≤5 papers needed | Top results only, light annotation |
| `standard` | default | Full pipeline, ≤25 papers |
| `comprehensive` | depth=comprehensive OR systematic review needed | All steps + citation graph + gap analysis |
| `verify-existing` | user provides `existing_bibliography` | Verify-only on provided list, extend if asked |

Mode is auto-detected from inputs; users don't need to specify.

## See Also

- `ai-idea-forge` — for direction generation
- `ai-related-positioning` — for differentiation
- `ai-paper-writer` — to embed citations
- `ai-integrity-check` — to audit citations in a draft
- `deep-research` (legacy) — for the underlying multi-agent search machinery
