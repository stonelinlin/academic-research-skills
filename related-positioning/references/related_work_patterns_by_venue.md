# Related Work Conventions by Venue

Quick reference for related_work_writer_agent. Cross-check against `shared/venue_db/<venue>.yaml` for current page limits.

## NeurIPS

- **Length**: Compact; typically 0.5-1 page (≈3-5 paragraphs)
- **Position**: Conventionally Section 2, after Introduction
- **Citation count**: 20-35 typical
- **Style**: Cluster by theme; differentiation must be explicit; reviewers often check that direct competitors are addressed
- **Watch**: Reviewers will downgrade for "missing related work" — coverage matters

## ICLR

- **Length**: 0.5-1 page; sometimes integrated with Introduction
- **Position**: Section 2 OR woven into Introduction (both common)
- **Citation count**: 25-40 typical (open review allows longer)
- **Style**: OpenReview discussion phase frequently centers on related-work; preempt likely concerns
- **Watch**: Concurrent work pattern is critical; reviewers actively check arxiv dates

## ICML

- **Length**: 0.5-0.75 page (8-page limit pressure)
- **Position**: Section 2
- **Citation count**: 20-30 typical
- **Style**: Stricter on theoretical positioning; if you build on a theorem, cite the source rigorously
- **Watch**: Reviewers expect connection to optimization/learning theory literature when relevant

## ACL / EMNLP

- **Length**: 0.5-0.75 page
- **Position**: Section 2 (between Intro and Method)
- **Citation count**: 25-40 typical (NLP has dense citation culture)
- **Style**: Often divided into "Task-related" and "Method-related" sub-paragraphs
- **Watch**: ACL reviewers track ARR submission cycles; concurrent-work claims are scrutinized

## CVPR

- **Length**: 0.75-1 page
- **Position**: Section 2 OR final section (both common at CVPR)
- **Citation count**: 30-50 typical (CV has very dense citation culture)
- **Style**: Often clustered by sub-area (e.g., "Diffusion editing", "GAN editing", "Inversion-based editing")
- **Watch**: CVPR reviewers evaluate experimental coverage; if you don't compare to a major baseline, expect criticism

## AAAI

- **Length**: 0.5 page (7-page limit + 2-page reference cap is tight)
- **Position**: Section 2
- **Citation count**: 20-30 typical (capped by 2-page reference limit)
- **Style**: Compact; prioritize must-cite ruthlessly
- **Watch**: Reference cap forces hard choices; use strategy_agent's `skip` aggressively

## arXiv (preprint)

- No length constraint, but reader patience matters
- Convention: 0.5-1 page; readers expect normal academic conventions
- Use this as the venue setting before you've decided submission target
