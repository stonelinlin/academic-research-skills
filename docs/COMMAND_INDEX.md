# Command Index — What Triggers What

Natural-language phrases that activate each ai-research-skills skill. Skills auto-trigger from these patterns; you don't need to type slash commands.

## At a Glance

| Skill | Most common triggers | Sample phrasings |
|---|---|---|
| ai-idea-forge | give me ideas, brainstorm, novelty | "give me ideas on X", "brainstorm research directions in Y", "novelty check on idea Z", "想 idea" |
| ai-lit-scout | find papers, literature, citations | "find recent papers on X", "build bibliography for Y", "literature review on Z", "文献调研" |
| ai-related-positioning | position, differentiate, related work | "position my work vs A and B", "how is my work different from X", "write related work", "差异化定位" |
| ai-method-architect | design experiment, methodology | "design experiment for X", "what baselines do I need", "ablation plan for Y", "实验方案" |
| ai-paper-writer | write, draft, polish, revise | "draft method section", "write abstract for X", "polish §3", "写论文" |
| ai-figure-smith | plot, figure, table | "plot accuracy vs X", "make ablation table", "design qualitative grid", "画图" |
| ai-integrity-check | verify, audit, check citations | "check citations", "run integrity check", "verify §4 claims", "完整性检查" |
| ai-paper-reviewer | review, critique, peer review | "review my paper", "NeurIPS-style review", "Devil's Advocate", "审稿" |
| ai-rebuttal-coach | rebuttal, response, address reviewer | "write rebuttal", "respond to reviewers", "OpenReview response", "回复评审" |
| ai-venue-formatter | format, compile, submit, camera-ready | "format for NeurIPS", "compile paper", "camera-ready", "排版投稿" |
| ai-research-pipeline | full pipeline, end-to-end, complete workflow | "full research pipeline", "guide me end-to-end", "全流程" |

## Disambiguation Rules

When a phrase could trigger multiple skills, the most specific takes precedence:

| Phrase | Goes to | Why |
|---|---|---|
| "review my paper" | `ai-paper-reviewer` (not `ai-rebuttal-coach`) | "review" = simulate review, not respond to one |
| "write related work" | `ai-related-positioning` (not `ai-paper-writer`) | Related work is positioning-driven |
| "find papers and write related work" | `ai-lit-scout` then `ai-related-positioning` then `ai-paper-writer` | Multi-skill chain |
| "fix this section" | `ai-paper-writer revise mode` | Editing, not new draft |
| "fix this rebuttal" | `ai-rebuttal-coach revise` | Different deliverable |
| "is my draft solid" | `ai-paper-reviewer` or `ai-integrity-check` | Disambiguate by asking user |
| "give me ideas" alone | `ai-idea-forge` | Default |
| "give me writing ideas" | `ai-paper-writer outline mode` | Specific to writing |

## Negative Patterns (DO NOT trigger)

These phrases should NOT auto-invoke a skill — they're conversational:

- "what's a good idea for…" (too vague — ask for clarification first)
- "papers" alone (unclear which skill)
- "review" alone (unclear: simulate or respond)
- "write" alone (unclear: section, abstract, rebuttal)

When ambiguous, the assistant asks ONE clarifying question before invoking.

## Skill-to-Skill Handoffs (recommended)

After each skill completes, the assistant suggests likely next skill:

```
ai-idea-forge   → ai-lit-scout / ai-method-architect
ai-lit-scout    → ai-related-positioning / ai-paper-writer
ai-related-positioning → ai-paper-writer / ai-paper-reviewer
ai-method-architect → ai-paper-writer / ai-integrity-check
ai-paper-writer → ai-figure-smith / ai-integrity-check / ai-paper-reviewer
ai-figure-smith → ai-paper-writer (insert refs) / ai-venue-formatter
ai-integrity-check → ai-paper-writer revise (if BLOCK) / ai-venue-formatter (if PASS)
ai-paper-reviewer → ai-paper-writer revise / ai-rebuttal-coach (if reviews real)
ai-rebuttal-coach → ai-paper-writer revise / ai-venue-formatter (camera-ready)
ai-venue-formatter → (submit) / arxiv-export
```

User can decline or pick a different next skill at any handoff.

## State Persistence

Each skill writes to `.ars-state/session-<timestamp>-<skill>.yaml`. Resume:

```
"resume"                              → resume most recent
"resume ai-idea-forge"                   → resume most recent ai-idea-forge session
"resume session-20260420-1431"        → resume specific session
"rewind to checkpoint 3"              → load earlier state
```

## Mode Selection (Implicit)

v4.0 collapses v3.3's 24 explicit modes into auto-detected sub-modes. Examples:

- `ai-lit-scout` auto-picks `quick` / `standard` / `comprehensive` from inputs
- `ai-paper-writer` auto-picks `draft` / `revise` / `polish` / `outline` based on whether `existing_draft` is provided
- `ai-paper-reviewer` auto-picks `full` / `quick` / `methodology-focus` / `re-review` based on phrasing and whether `prior_review` exists

Users CAN override:

```
"ai-lit-scout comprehensive"        → force comprehensive depth
"ai-paper-reviewer methodology-focus" → force the focus
"ai-paper-writer outline mode"      → start with outline + Socratic
```

But explicit override is rarely needed.
