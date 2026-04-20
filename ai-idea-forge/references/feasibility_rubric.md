# Feasibility Rubric — What Compute / Data / Time Really Cost

This rubric helps `novelty_scorer_agent` calibrate feasibility scores against realistic AI/ML research costs as of 2026.

## Compute Reference (rough order-of-magnitude, 2026 prices)

| Task | Compute |
|---|---|
| Fine-tune 7B on 100K examples (LoRA) | 1× A100, 8 hours |
| Fine-tune 7B on 100K examples (full) | 8× A100, 24 hours |
| Pre-train 1B from scratch | 64× A100, 2 weeks |
| Pre-train 7B from scratch | 256× H100, 1 month |
| Eval 7B on 5 long-context benchmarks | 1× A100, 4 hours |
| Eval GPT-4-class API on 10K prompts | $200-500 API + 6h wall |
| Mechanistic interpretability of 7B | 1× A100 + 1-2 weeks human time |
| Train RLHF 7B from SFT checkpoint | 8× H100, 1 week |
| Diffusion model training (256×256, 100M params) | 8× A100, 1 week |
| Diffusion model fine-tune (LoRA) | 1× A100, 4 hours |

## Wall-time vs Compute

A 6-week project with 4 GPUs ≠ a 6-week project with 64 GPUs. Wall time matters because:
- Iteration speed determines how many ideas you can test
- Submission deadlines are wall-time, not compute-time
- Most projects spend 50%+ of wall time on infra/eval/writing

## Data Access Tiers

| Tier | Examples | Feasibility impact |
|---|---|---|
| Public datasets | HF datasets, ImageNet, CommonCrawl, OpenWebMath | All ideas usable |
| Public APIs | GPT-4, Claude, Gemini API | Cost-bound, not access-bound |
| Public weights | Llama, Mistral, Qwen, DeepSeek (open weights) | Most method-novelty ideas usable |
| Closed APIs (gated) | OpenAI fine-tune API, Anthropic logprobs, internal eval suites | Limits some interpretability + ablation work |
| Internal data | Industrial data not released | Severely limits external novelty score (reviewers can't reproduce) |

## Timeline Reality

| Goal | Realistic timeline (assuming 50% project capacity) |
|---|---|
| arXiv preprint of small empirical study | 6-10 weeks |
| Workshop paper | 2-3 months |
| Top conference (NeurIPS/ICLR/ICML) main track | 4-8 months from idea to submission |
| Position paper | 2-4 months (mostly thinking + writing) |
| Survey/review | 4-6 months |
| Benchmark paper | 3-6 months (data construction is the bottleneck) |

## Feasibility Score Mapping

When `novelty_scorer_agent` assigns feasibility:

| Score | Compute used | Time used |
|---|---|---|
| 5 | <30% of budget | <50% of timeline |
| 4 | 30-60% | 50-70% |
| 3 | 60-90% | 70-90% |
| 2 | 90-150% (overshoot) | 90-110% |
| 1 | >150% | Misses deadline |

## Failure Mode Note

The most common feasibility miscalibration is underestimating *evaluation cost*. Eval often takes 30-50% of project time on top of training. When in doubt, double the eval estimate.
