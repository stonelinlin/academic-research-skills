# Example Session: Long-Context LLM Evaluation

User opens with: "Give me ideas on long-context LLM evaluation. I have 8 H100s for 2 months."

## Step 1 — Intake

```
Agent: Got it. Two clarifying questions:
- Public datasets only, or private data available?
- Target venue? (NeurIPS / ICLR / ACL / arXiv-only)

User: Public only. ICLR 2027.
```

intake_agent emits:
```yaml
intake:
  interest_area: long-context LLM evaluation
  constraints:
    compute: 8 H100s
    timeline: 4 months until ICLR 2027 deadline
    data_access: public datasets only
  target_venues: [iclr]
  style_preference: empirical (default)
```

## Step 2 — Trend Scan

trend_scanner_agent runs queries. Output excerpt:

```yaml
clusters:
  - theme: "Needle-in-haystack benchmarks"
    representative_papers:
      - title: "RULER: What's the Real Context Size of Your Long-Context Language Models?"
        arxiv_id: 2404.06654
      - title: "LongBench v2"
        arxiv_id: 2412.15204
    unanimous_claims:
      - "Models claim long context but degrade beyond 32K"
    open_disputes:
      - "Whether degradation is positional or semantic"
    underexplored_adjacent:
      - "Multi-needle compositional reasoning"
      - "Distractor-similarity to needle"
    trend_signal: active

  - theme: "RAG vs long-context"
    representative_papers: [...]
    open_disputes:
      - "RAG superiority claim is dataset-dependent"
    trend_signal: active
```

## Step 3 — Gap Mining

gap_miner_agent identifies 6 gaps. Two examples:

```yaml
gaps:
  - id: gap-001
    cluster_source: "Needle-in-haystack benchmarks"
    type: hidden_assumption
    one_sentence_claim: "Existing benchmarks assume the needle is semantically distinct from distractors; semantic similarity has not been controlled."
    exploit_difficulty: low
    why_it_matters: "If similarity matters, current benchmarks underestimate the failure mode."
    nearest_existing_attempt:
      title: "RULER"
      arxiv_id: 2404.06654
      what_they_did_not_address: "Distractor similarity is held constant by design."

  - id: gap-002
    cluster_source: "RAG vs long-context"
    type: contested_finding
    one_sentence_claim: "Whether RAG beats long-context depends on retriever quality, but no paper isolates retriever-quality vs context-length effects."
    exploit_difficulty: medium
    ...
```

## Step 4 — Idea Generation

3 ideas generated from gap-001 alone. Best one:

```yaml
- id: idea-001
  one_line_claim: "We show that needle-in-haystack accuracy drops 30%+ when the needle is semantically similar (cosine ≥ 0.7) to surrounding distractors, even when positional location is held constant."
  contribution_shape: analysis
  motivation: "Current long-context benchmarks systematically underestimate failure modes by selecting semantically distinct needles. This makes published numbers unreliable for real-world retrieval scenarios."
  novelty_score: 4
  novelty_reasoning: "RULER and LongBench fix needle distinctness; controlling similarity is unaddressed."
  feasibility_score: 5
  feasibility_reasoning: "8 H100s for 4 months is overkill; eval-only project."
  risk_score: 2
  risk_reasoning: "Effect is likely real and measurable; minimal chance of null result."
  minimum_experiment:
    setup: "Construct controlled benchmark where needle and distractors are matched on length but vary in cosine similarity (5 buckets, 0.0-1.0). Evaluate Llama-3.1-70B, Qwen2.5-72B, GPT-4o on N=1K examples per bucket."
    metrics: [accuracy, calibration]
    expected_signal: "Accuracy curve sloping down as similarity increases; ≥30% gap between extremes."
    estimated_compute_hours: 80
  closest_existing_work:
    - title: "RULER"
      arxiv_id: 2404.06654
      differentiation: "RULER varies needle position and length, not semantic similarity."
  devils_advocate:
    strongest_attack: "If similarity is just a proxy for retrieval difficulty, the contribution reduces to 'long-context is bad at retrieval' which is already established."
    intensity: 3
    mitigation: "Include a control showing that pure retrieval (with separate retriever) is unaffected by similarity at the same level."
  fits_venue: [iclr, neurips]
  recommended: true
  recommendation_reason: "Highest feasibility × novelty product; clear experiment; addresses a real gap."
```

## Step 5 — User Picks One

```
Agent: Top 3 are idea-001, idea-004, idea-007.

User: I'll take idea-001. What next?

Agent: Suggested handoff:
- /ai-lit-scout for full bibliography
- /ai-related-positioning to nail differentiation vs RULER and LongBench v2
- /ai-method-architect to design the controlled benchmark construction

State saved as session-20260420-1431-ai-idea-forge. Resume anytime.
```

state_tracker writes idea-001 as a handoff_artifact for downstream skills.
