# Venue Phrasing Conventions

Brief style guide per venue. Use alongside `shared/venue_db/<venue>.yaml`.

## NeurIPS

- **Address**: "We thank Reviewer N..." OR "Response to Reviewer N"
- **Length**: 1500 words/reviewer typical; total budget 6000
- **Format**: Markdown sections per concern; no headings deeper than ##
- **Closing**: Optional 1-line; many strong rebuttals have no closing

## ICLR

- **Address**: OpenReview thread; respond directly to reviewer's comment
- **Multi-round**: First response is the substantive one; later rounds are clarification
- **Length**: Conventionally 600-1000 words/round; multi-round can total higher
- **Engagement signal**: Reviewers explicitly track whether authors engage; brief responses can lower scores
- **Closing**: "We have updated the manuscript to reflect [X]." after first round

## ICML

- **Address**: "We thank Reviewer N..." (formal)
- **Length**: 5000 words total; 3 reviewers = ~1600/reviewer
- **Format**: Per-reviewer Markdown
- **No multi-round**: Make the first (and only) response count

## ACL / EMNLP

- **Address**: Bullet form is acceptable
- **Length**: 1500 words ACROSS all reviewers (very tight)
- **Format**: Often one combined response listing concerns by reviewer ID, then bulleting addresses
- **Phrasing**: Telegraphic; "Added Table 5 (similarity buckets); +30% gap supports claim."

## CVPR

- **Address**: One PDF page, max
- **Length**: ~600 words + figures
- **Format**: 2-column LaTeX, often with inline figures
- **Critical**: Include a figure if defending an experimental claim — visual rebuttals are highly effective

## AAAI

- **Address**: "Response to Reviewer N"
- **Length**: 4500 words
- **Format**: Standard per-reviewer Markdown

## Universal Closings (Optional)

- "We have updated the manuscript to incorporate these revisions."
- "All revisions are tracked in [PDF/repo link]."
- "We are grateful for the engagement and look forward to further discussion."

## Avoid Universally

- Personal apologies ("we are sorry…")
- Defensive openings ("contrary to the reviewer's claim…")
- Promises of "future work" for critical concerns
- "Thank you" as a substitute for substance
- Repeating the reviewer's concern verbatim before answering (wastes words)
