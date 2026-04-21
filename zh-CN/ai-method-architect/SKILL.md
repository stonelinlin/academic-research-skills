---
name: ai-method-architect
description: "为 AI/ML 论文设计实验与方法论。输入：研究问题 + 主张 + 约束。输出：实验方案（假设、条件、基线、指标、对照）、预注册模板、消融计划、统计分析计划、可复现性说明。Triggers: design experiment, methodology, experimental design, ablation plan, design study, 设计实验, 实验方案, 方法设计."
metadata:
  version: "4.1.1"
  domain: ai-ml
  data_access_level: redacted
  task_type: outcome-gradable
  related_skills:
    - ai-idea-forge
    - ai-lit-scout
    - ai-paper-writer
    - ai-integrity-check
  language: zh-CN
---

# ai-method-architect — AI/ML 实验设计

为 AI/ML 主张设计**可证伪、可复现**的实验；输出接近预注册水平的协议。

## 30 秒上手

```
"Design an experiment to test that semantic-similarity of distractors degrades long-context accuracy."
"Plan the ablation suite for our diffusion-editing method."
"What baselines should I include for a long-context benchmark paper?"
"为我的 RLHF reward hacking 假设设计实验。"
```

## 何时使用

| 使用 ai-method-architect | 换用其他 skill |
|---|---|
| 有主张需规划如何检验 | 已有结果需撰写 → `ai-paper-writer` |
| 选择基线与消融 | 需检索已发表方法 → `ai-lit-scout` |
| 预注册式实验设计 | 已完成工作可复现性审计 → `ai-integrity-check` |

## 输出

实验协议、统计分析计划、消融计划、可复现性说明 — YAML 结构与英文版一致。

## 工作流

```mermaid
flowchart TD
    Intake[主张 + 约束 + 会议]
    Hypoth[假设分解]
    Var[变量：自变量/因变量/对照]
    Models[模型选择]
    Base[基线：下界/上界/竞争]
    Metric[指标]
    Stats[统计方案]
    Abl[消融]
    Repro[可复现性]
    Output[协议 + 预注册模板]

    Intake --> Hypoth --> Var --> Models --> Base --> Metric --> Stats --> Abl --> Repro --> Output
```

## Agents（`shared/agents`）

| Agent | 角色 | 文件 |
|---|---|---|
| `research_architect_agent` | 核心实验设计 | [`../../shared/agents/research_architect_agent.md`](../../shared/agents/research_architect_agent.md) |
| `risk_of_bias_agent` | 混杂与偏倚 | [`../../shared/agents/risk_of_bias_agent.md`](../../shared/agents/risk_of_bias_agent.md) |
| `devils_advocate`（共享） | 协议压力测试 | [`../../shared/agents/devils_advocate.md`](../../shared/agents/devils_advocate.md) |

## 铁律

1. 每个假设须有**可证伪标准**。  
2. 每个自变量须有**对照**以排除混杂。  
3. 基线须含**下界+上界**，非仅 SOTA。  
4. **统计方案先于跑实验**确定。  
5. 算力预算须在约束内；超预算 >2× 须缩减或标注。

## 参见

`ai-idea-forge`、`ai-lit-scout`、`ai-integrity-check`。
