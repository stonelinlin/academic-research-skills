# Rebuttal Anti-Patterns

Common rebuttal failure modes observed across NeurIPS / ICLR / ICML / ACL submissions. response_drafter_agent and auditor_agent should detect and prevent these.

## A. Tone Failures

### A1. Sycophantic opening
> ~~"We are deeply grateful for the reviewer's thoughtful and insightful comments. Your careful reading has greatly improved our work."~~

**Why it fails**: Wastes word budget; reviewers know it's boilerplate; some reviewers actively penalize it.

**Fix**: One-sentence acknowledgment max:
> "We thank the reviewer; we address each concern below."

### A2. Apologetic concession
> ~~"We apologize for the lack of clarity. The reviewer is absolutely correct that we should have made this clearer."~~

**Why it fails**: Apology is performative; doesn't address the issue; makes the rest of the response sound defensive.

**Fix**: Acknowledge briefly, then act:
> "Section 3 was unclear. We have revised it to state explicitly that [X]."

### A3. Combative defense
> ~~"The reviewer appears to misunderstand our central claim. As clearly stated in §3, we are not arguing that…"~~

**Why it fails**: Patronizing; AC will side against you.

**Fix**: Clarify without blaming:
> "To clarify: our claim in §3 is [X], not [Y]. We have rewritten the paragraph to make this distinction clearer."

## B. Substance Failures

### B1. Promising experiments you can't run
> ~~"We will add the requested ablation in the revised version."~~ (when it requires 2 weeks of compute and you have 4 days)

**Why it fails**: AC tracks promises across rounds; broken promises reduce trust.

**Fix**: Be honest about feasibility. Use experiment_planner_agent. If infeasible:
> "This ablation would require [X compute / data] which is outside our current resources. We acknowledge this limitation in the revised §6 and propose [partial alternative]."

### B2. "Future work" deflection
> ~~"We will explore this in future work."~~ (for a critical concern)

**Why it fails**: Reviewers will downgrade for treating critical concerns as optional.

**Fix**: Either run something now, or acknowledge as a real limitation in the paper.

### B3. Claims of contributions reviewer didn't notice
> ~~"As the reviewer may have missed, our paper makes contributions A, B, C, D, E, F, and G."~~

**Why it fails**: Listing inflates; reviewers assume the paper would have made it clearer if true.

**Fix**: Pick the ONE contribution most relevant to the reviewer's concern and clarify it.

## C. Structural Failures

### C1. Same response to multiple reviewers
**Why it fails**: Reviewers can see all responses (in OpenReview); duplicated text signals lazy engagement.

**Fix**: Even if the substance overlaps, tailor the framing to each reviewer's specific words.

### C2. Burying the answer
> [Long context], [acknowledgment], [restatement of reviewer's concern], [discussion], [eventually the answer in paragraph 4]

**Why it fails**: Reviewer reads top-down with limited time; if the answer isn't in the first 2 sentences of the response, they may miss it.

**Fix**: Lead each response with the answer. Justification follows.

### C3. Hand-waving on missing related work
> ~~"We will add the suggested references in the revised version."~~

**Why it fails**: Doesn't address the substantive concern (what differentiates your work from the missing reference).

**Fix**: Use ai-related-positioning skill. Add a sentence in the rebuttal that ARTICULATES the differentiation, not just promises a citation.

## D. Word-Budget Failures

### D1. Over budget by 200+ words
**Why it fails**: Many venues hard-cap; over-budget rebuttals get truncated arbitrarily.

**Fix**: Use auditor_agent's trim sequence:
1. Cut acknowledgments
2. Cut closings
3. Drop can-defer items
4. Compress should-fix to one sentence each
5. Combine related must-fix paragraphs

### D2. Under budget by 30%+
**Why it fails**: Wasted opportunity; reviewers expect substance to fill the limit.

**Fix**: Expand evidence on must-fix items, or address one more should-fix concern.

## E. Honesty Failures

### E1. Quoting reviewer text inaccurately
**Why it fails**: Reviewers spot misquotes immediately; destroys credibility.

**Fix**: review_parser_agent stores VERBATIM text. Use that.

### E2. Citing a paper that doesn't say what you claim
**Why it fails**: Easy for reviewers to check; lethal to acceptance.

**Fix**: ai-integrity-check skill on rebuttal claims involving citations.

### E3. Phantom experimental results
> ~~"We added the ablation, achieving 78.4% accuracy."~~ (when no such experiment was run)

**Why it fails**: This is fabrication; it's also extremely common when LLMs auto-fill numbers.

**Fix**: experiment_planner status enforcement; placeholders only until results in hand.
