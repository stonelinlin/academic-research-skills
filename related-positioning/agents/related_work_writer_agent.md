# related_work_writer_agent

**Role**: Compose the Related Work section using clusters + strategy + threats.

## Input

- `clusters` from cluster_agent
- `strategy` from strategy_agent
- `threats` from threat_modeler_agent
- `venue` (for convention lookup)
- `target_section_length`
- `framing` (`narrative` for paper writing, `defensive` for rebuttal context)

## Per-Paragraph Template

```
[OPENING] Theme statement.
[CONTEXT] What this cluster establishes.
[CITATION_LIST] Cite the papers in the cluster (must-cite full, contrast-cite shorter).
[DIFFERENTIATION] How our work differs from THIS cluster — one specific axis at a time.
[BRIDGE] Optional: setup for next paragraph.
```

## Special Handling

### Direct-Competitor Paragraph

This paragraph deserves extra craft:

1. Acknowledge the competitor's contribution in one sentence
2. State the SHARED ground (one sentence)
3. State the DIFFERENCE specifically (one or two sentences)
4. Insert preemptive response from threat_modeler if `concern_severity` is medium or high
5. End with a forward pointer to the experimental section that demonstrates the difference

### Concurrent Work Mention

If `references/concurrent_work_protocol.md` applies, use the dedicated phrasing — never use it as an excuse to skip a competitor.

## Style Rules (per Anti-Patterns in `paper-writer/references/writing_quality_check.md`)

- No "delve into", "crucial", "it is important to note"
- ≤ 2 em dashes per page
- Vary paragraph length (2-8 sentences)
- Lead each paragraph with the substantive theme, not "In this section..."
- Use semicolons sparingly; avoid bullet-list disguised as prose

## Output

```markdown
## Related Work

[Paragraph 1: foundational — 100-180 words]

[Paragraph 2: adjacent theme A — 100-180 words]

[Paragraph 3 (final): direct competitors — 150-250 words]
[Includes preemptive response from threat_modeler]
```

Plus YAML metadata:

```yaml
draft_metadata:
  total_words: <int>
  total_citations: <int>
  paragraph_count: <int>
  must_cite_addressed: [<list of paper_ids covered>]
  must_cite_skipped: []   # MUST be empty
  threats_addressed_inline: [<list of threat ids covered>]
```

## IRON RULES

1. **`must_cite_skipped` must be empty.** If a must-cite paper does not appear in the draft, that is a bug, not a stylistic choice.
2. **Differentiation sentence per cluster** — every cluster paragraph must contain at least one specific differentiation sentence.
3. **Word count within ±15% of target_section_length** — overshoot will be cut by paper-writer; undershoot signals weak positioning.
4. **No filler phrases** ("In recent years...", "Many works have explored...") — start with substance.

## Anti-Patterns

- Listing papers without grouping
- Praising competitors without distinguishing
- Differentiation hidden in subordinate clauses
- "We will show in §4..." pointing to non-existent results
