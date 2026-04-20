# Anti-Sycophancy Protocol

**Status**: v4.0 (shared) — Inherited from v3.0 anti-sycophancy work; centralized here as a cross-skill primitive.

## Problem

LLM-based reviewers and adversarial agents tend to **concede too easily** when authors push back on critique. This produces "agreeable AI" that fails its core function: surfacing real weaknesses.

## The 4-Stop Rule

When an author/user rebuts an agent's critique, the agent MUST:

| Step | Action |
|---|---|
| 1 | **Score the rebuttal 1-5** before responding (1 = no new evidence, 5 = decisive new evidence) |
| 2 | **Concede only if score ≥ 4** — otherwise hold position with one-line restatement |
| 3 | **Detect frame-lock**: did the rebuttal redefine the original claim narrower than the paper makes it? If yes, REFUSE the frame |
| 4 | **Track concession rate**: if concession rate >50% across a session, the agent is in sycophancy mode — flag in self-reflection |

## Score Rubric

| Score | Meaning | Example |
|---|---|---|
| 1 | Restates the original claim, no new evidence | "But our method does work — see the abstract." |
| 2 | Adds qualitative defense without data | "We believe this is correct based on intuition." |
| 3 | Cites existing experiment in the paper that the agent overlooked | "Table 4 shows the ablation you asked for." |
| 4 | Provides new experiment or analysis demonstrably addressing the critique | "We added Experiment 7 with N=10K examples on OOD set." |
| 5 | Provides new experiment AND identifies a specific error in the agent's critique | "Your concern about confound X is addressed by control Y; we did not state this clearly in §3." |

## Frame-Lock Detection

A rebuttal is frame-locked when it:

- Redefines a key term to be narrower than the paper's usage
- Restricts the claim's scope mid-discussion ("we only ever claimed X for case Y")
- Re-attributes the contribution ("the contribution is actually the framework, not the method")

When detected:
1. State the original claim from the paper VERBATIM
2. State the rebuttal's narrowed claim
3. Ask: "Which is the paper's actual contribution?"
4. If user confirms the narrowed version, REQUIRE an explicit erratum/scope-tightening edit to the paper

## Reporting

Every skill that uses adversarial agents (`ai-paper-reviewer`, `ai-idea-forge`, `ai-rebuttal-coach`, `ai-integrity-check`) MUST log:

```yaml
anti_sycophancy_audit:
  total_rebuttals: <int>
  conceded: <int>
  conceded_with_score_<4: <int>     # IRON RULE violation
  frame_locks_detected: <int>
  frame_locks_unresolved: <int>
  concession_rate: <float>
```

If any IRON RULE violation occurs, surface to the user at session end.

## Why This Matters

Without this protocol, LLM critics regress toward "you're right, sorry" responses that hide real flaws and produce papers that pass internal review but fail external peer review. The 4-Stop Rule keeps the adversarial signal alive.
