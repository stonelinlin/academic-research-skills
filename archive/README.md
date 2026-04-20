# Archive

Historical content kept for reference and to satisfy the v4.0 → v3.3 migration window.

**Do not depend on anything in this folder for new work.** Treat it as a museum.

---

## What lives here

### `v3/` — academic-research-skills v3.3.6

The previous incarnation of this project, called `academic-research-skills`. It was a
general academic-research toolkit (4 large skills × 24 modes) covering humanities,
social sciences, higher-education research, etc.

| Path | What it was |
|---|---|
| `v3/deep-research/` | 7-mode research skill (full / quick / lit-review / fact-check / systematic-review / socratic / review) |
| `v3/academic-paper/` | 10-mode writing skill (full / plan / outline / revision / abstract / lit-review / format-convert / citation-check / disclosure / revision-coach) |
| `v3/academic-paper-reviewer/` | 6-mode peer-review simulator |
| `v3/academic-pipeline/` | 10-stage end-to-end orchestrator with mandatory checkpoints |
| `v3/MODE_REGISTRY.md` | Single source of truth for all 24 v3 modes |
| `v3/POSITIONING.md` | Project positioning rationale and license stance |
| `v3/QUICKSTART.md` | v3 install + quickstart |
| `v3/README.zh-TW.md` | v3.3.6 Chinese (Traditional) README |
| `v3/docs/ARCHITECTURE.md` | v3 pipeline architecture diagrams |
| `v3/docs/PERFORMANCE.md` (+ zh-TW) | v3 token-usage notes |
| `v3/docs/SETUP.md` (+ zh-TW) | v3 setup details |
| `v3/docs/design/` | v3.4 / v3.5 design specs (PRISMA-trAIce, RAISE compliance, reading-check) |
| `v3/examples/` | v3 showcase artifacts (full paper PDFs, integrity reports, review reports) |

### Why these are still here

1. **Agent reuse.** Some v4 atomic skills delegate to specific v3 agents
   (e.g., `ai-lit-scout` → `archive/v3/deep-research/agents/bibliography_agent.md`).
   See [`docs/MIGRATION_v3_to_v4.md`](../docs/MIGRATION_v3_to_v4.md) for the full mapping.
2. **Migration window.** Users of v3.3.6 have until **2026-10** to migrate.
3. **Historical reference.** Showcase PDFs and design specs document how the project
   evolved.

## Removal schedule

| Date | Action |
|---|---|
| 2026-04-20 | v4.0.0 released; v3 skills moved to `archive/v3/` |
| 2026-07-01 | All v4 skills should have inlined or replaced their v3-agent dependencies |
| 2026-10-20 | `archive/v3/` is **deleted from the default branch** (still recoverable via git history) |

## If you really need the v3 surface

```bash
git checkout v3.3.6   # tagged release
```

Or browse the [v3.3.6 release on GitHub](https://github.com/Imbad0202/academic-research-skills/releases/tag/v3.3.6).
