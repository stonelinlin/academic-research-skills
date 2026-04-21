---
name: ai-research-pipeline
description: "可选元 skill：编排完整 AI/ML 研究流程（想法→文献→定位→方法→写作→完整性→审稿→rebuttal→定稿）。仅当用户明确要求编排流程时使用；否则请直接调用原子 skill。Triggers: full pipeline, end-to-end paper, research to publication, complete workflow, orchestrated research, 完整研究流程, 端到端论文, 全流程引导."
metadata:
  version: "4.1.1"
  domain: ai-ml
  data_access_level: redacted
  task_type: outcome-gradable
  related_skills:
    - ai-idea-forge
    - ai-lit-scout
    - ai-related-positioning
    - ai-method-architect
    - ai-paper-writer
    - ai-figure-smith
    - ai-integrity-check
    - ai-paper-reviewer
    - ai-rebuttal-coach
    - ai-venue-formatter
  language: zh-CN
---

# ai-research-pipeline — 可选全流程编排器

多数用户应**直接**使用原子 skill（`ai-idea-forge`、`ai-lit-scout`、`ai-paper-writer` 等）。本元 skill 仅面向**明确希望**被引导走完端到端流程、并接受检查点的用户。

## 何时使用（请诚实）

| 使用 ai-research-pipeline | 使用原子 skill |
|---|---|
| 希望每阶段被引导 | 已知当前阶段 |
| 希望阶段间强制完整性门 | 自己会按需调用 `ai-integrity-check` |
| 需要任意阶段恢复 | 只做单任务 |

不确定时：**从原子 skill 开始**。元 skill 会增加开销。

## 十阶段（轻量）

```mermaid
flowchart LR
    S1[1. idea] --> S2[2. lit] --> S3[3. position] --> S4[4. method]
    S4 --> S5[5. integrity #1]
    S5 --> S6[6. write] --> S7[7. figures] --> S8[8. integrity #2]
    S8 --> S9[9. self-review]
    S9 --> S10[10. format]
    S10 -.-> R1[rebuttal]
    R1 -.-> S10
```

阶段与 skill 对应、强制检查点（3 个）及 workspace 目录结构 — 见英文版详表。

## Agents

| Agent | 文件 |
|---|---|
| `pipeline_orchestrator_agent` | [`../../shared/agents/pipeline_orchestrator_agent.md`](../../shared/agents/pipeline_orchestrator_agent.md) |
| `state_tracker`（共享） | [`../../shared/agents/state_tracker.md`](../../shared/agents/state_tracker.md) |

## 铁律

1. **原子 skill 逻辑不在这里重写**，仅编排调用。  
2. **任意阶段可恢复**（`state_tracker` + `.ars-state/`）。  
3. **仅 3 个强制检查点**（相对 v3.3 的 7–10 次）。  
4. **第 5 与第 8 阶段**的 `ai-integrity-check` 不可被编排器自动覆盖 BLOCK。  
5. **跳过阶段须用户明确同意**。

## 恢复与参见

```
"resume pipeline"
"resume pipeline at stage 6"
```

- [`../../archive/v3/academic-pipeline/`](../../archive/v3/academic-pipeline/)（v3.3 冻结快照，仅供对照）  
- [`../../docs/COMMAND_INDEX.md`](../../docs/COMMAND_INDEX.md)
