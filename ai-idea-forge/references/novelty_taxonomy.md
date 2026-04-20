# Novelty Taxonomy for AI/ML Research

There is no single thing called "novelty". Reviewers use at least 5 distinct senses, often without naming which one. ai-idea-forge scores against the strongest applicable type.

## The 5 Types

### 1. Method Novelty
A new algorithm, architecture, or training procedure.
- **Bar in 2026**: Very high. "We added X to Transformer" rarely passes alone.
- **Productive form**: New method + analysis of *why* it works.

### 2. Setting Novelty
Same method family, but applied to a setting where its behavior is unknown.
- **Bar**: Medium. The setting must be non-trivially different (not just "tested on a new dataset").
- **Examples**: Long-context behavior of methods designed for short context; cross-lingual transfer of methods evaluated only on English.

### 3. Insight Novelty
A new explanation for known observations.
- **Bar**: Medium-high. Must be falsifiable and have one experiment that distinguishes the new explanation from the old.
- **Example**: "Layer-norm placement matters for stability" → "Pre-LN stability comes from gradient norm preservation, not from the LN itself."

### 4. Resource Novelty
A new dataset, benchmark, or evaluation protocol.
- **Bar**: High in 2026. Saturated benchmarks no longer get accepted; the resource must expose a *failure mode* the community cares about.
- **Productive form**: Benchmark + evidence that current models systematically fail on it.

### 5. Reframe Novelty
Same data and methods, but a new conceptual framework that changes how the community should think about a problem.
- **Bar**: Very high (rare). Usually position-paper or perspective-paper format.
- **Example**: "Memorization is not the opposite of generalization."

## Anti-Novelty Patterns (downgrade to 1-2)

- "We're the first to combine A and B" — almost never sufficient
- "We achieve SOTA on benchmark X" — only matters if SOTA is meaningfully large or X is a hard benchmark
- "We use [new model] for [old task]" — substitution alone is not novel
- "We extend [method] to multi-modal" — only counts if multi-modality changes the method's behavior

## Calibration Note

LLM-based novelty scoring tends to inflate. To counter:
- Anchor each score to a specific known paper (`closest_existing_work`)
- Require a verbal articulation ("X is more novel than Y because…")
- Score 5 requires explicit confirmation search

Inflated novelty estimates lead to wasted research effort. Honest 3 > false 5.
