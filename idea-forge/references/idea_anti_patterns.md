# Idea Anti-Patterns (drop or rewrite these)

idea_generator_agent should refuse or rewrite ideas matching these patterns.

## A. Framing Problems

### A1. "We will explore X"
**Why it fails**: Not falsifiable. "Explore" doesn't commit to a claim.
**Fix**: Pick the strongest hypothesis you'd find during the exploration and commit to it as the claim.

### A2. "We propose a framework for X"
**Why it fails**: Frameworks without empirical validation rarely get accepted at top AI venues.
**Fix**: Either tie the framework to a concrete experiment that demonstrates its value, OR pivot to position paper.

### A3. "We study X using Y"
**Why it fails**: Methodology-led, not contribution-led. Reader doesn't know what you'll show.
**Fix**: Lead with the contribution: "We show that Y reveals previously unobserved property Z of X."

### A4. "We benchmark X models on Y"
**Why it fails**: Pure benchmarking is a workshop paper at best.
**Fix**: Benchmark + the failure mode discovered + the explanation.

## B. Novelty Problems

### B1. "First to apply X to Y"
**Why it fails**: Substitution alone is not novel.
**Fix**: Show that Y exposes a property of X (or vice versa) that wasn't visible in the original setting.

### B2. "Improves SOTA on benchmark Z"
**Why it fails**: SOTA is a side-effect, not a contribution. Unless Z is a genuinely hard, recent benchmark and the gain is large.
**Fix**: Frame as: "We identify [bottleneck], propose [fix], and demonstrate [improvement]."

### B3. "Combines insights from A and B"
**Why it fails**: Combination is not creation.
**Fix**: Show that the combination reveals a property neither paper alone could reveal.

## C. Feasibility Problems

### C1. "Train a 100B model from scratch"
**Why it fails**: Beyond academic compute, even with concessions.
**Fix**: Use existing checkpoints (Llama, Mistral, Qwen) and focus on a method that doesn't require pretraining.

### C2. "Need GPT-4 outputs on 1M prompts"
**Why it fails**: API cost likely >$5K, often >$20K.
**Fix**: Subsample to 5-10K, justify with statistical power calculation.

### C3. "Comprehensive evaluation across all major benchmarks"
**Why it fails**: Eval cost dominates. "All major" usually means 8-15 benchmarks × multiple models.
**Fix**: Pick 3 benchmarks that maximally separate hypotheses; justify the choice.

## D. Risk Problems

### D1. "Solve hallucination"
**Why it fails**: The problem is too big; the contribution becomes one paper among many.
**Fix**: Pick one specific failure mode (e.g., "factual recall under instruction conflicts") and contribute a measurement + mitigation.

### D2. "Build AGI by improving X"
**Why it fails**: Mismatch between scope and contribution.
**Fix**: Honestly state what the work would and would not contribute.

### D3. Anything requiring multi-year human evaluation
**Why it fails**: IRB delays + human eval at scale rarely fits a research timeline.
**Fix**: Use proxy metrics or limited human eval (n<100) with explicit limitation discussion.

## E. Ethics / Dual-Use

### E1. "Bypass alignment training"
**Why it fails**: Most venues require ethical review; many will desk-reject without strong dual-use justification.
**Fix**: Frame as red-teaming with disclosure protocol; coordinate with model providers.

### E2. Anything involving real personal data without consent
**Why it fails**: IRB violation + ethical concerns.
**Fix**: Use synthetic data or publicly released anonymized datasets.

## How to use this file

`idea_generator_agent` should self-check each generated idea against this list. If ANY pattern matches, either:
- Rewrite the idea to remove the anti-pattern, OR
- Drop the idea (if the anti-pattern is structural, not surface)
