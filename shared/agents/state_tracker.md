# state_tracker (shared)

**Role**: Cross-session persistence for multi-step skill invocations. Lightweight; not a database.

**Status**: v4.0 — Canonical shared state tracker (supersedes the v3.3 `state_tracker_agent` spec).

## When to use

- User runs `ai-idea-forge` and wants to come back later to refine ideas
- A skill spans multiple turns and the user pauses
- Two skills hand off (e.g., `ai-lit-scout` → `ai-paper-writer` reusing the bibliography)

## Storage

State files live in `.ars-state/` at the project root (gitignored by default). Each session has one YAML file:

```
.ars-state/
├── session-20260420-1431-ai-idea-forge.yaml
├── session-20260420-1502-ai-lit-scout.yaml
└── session-active.yaml          # symlink to most recent
```

## Schema

```yaml
session_id: <YYYYMMDD-HHMM-skill-name>
skill: <skill-name>
started_at: <iso-timestamp>
last_updated: <iso-timestamp>
inputs:
  <skill-specific input snapshot>
outputs:
  <skill-specific output snapshot>
checkpoints:
  - timestamp: <iso>
    note: <what just completed>
handoff_artifacts:
  - schema: <schema-name from shared/handoff_schemas.md>
    path: <relative-path or inline content>
status: <in-progress|paused|completed|failed>
next_skill_recommended: <name|null>
```

## Resume Pattern

User says: `resume session-20260420-1431-ai-idea-forge` (or just `resume` for most recent)

The calling skill:
1. Reads the YAML
2. Replays the last checkpoint to the user as a summary
3. Asks: "Continue from here, or rewind to [earlier checkpoint]?"
4. Resumes the skill workflow with the loaded state

## Handoff Pattern

When skill A finishes and user wants to feed into skill B:

```
A writes:
  handoff_artifacts:
    - schema: AnnotatedBibliography
      path: outputs/bib.yaml

B reads .ars-state/session-active.yaml on launch and detects available handoff_artifacts. If a matching schema is present, B skips the equivalent intake step.
```

## Anti-patterns

- Don't put large artifacts (full paper text, image data) inline; use `path:` reference
- Don't auto-resume without user confirmation
- Don't merge state across different skills silently — handoff requires explicit user OK

## Implementation Note

This document defines the *contract*. Actual file I/O is handled by the calling Claude session via `Write`/`Read` tools. There is no daemon; state is just YAML on disk.
