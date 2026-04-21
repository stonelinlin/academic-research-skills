# ai-research-skills

[![Version](https://img.shields.io/badge/version-v4.1.1-blue)](CHANGELOG.md)
[![License: CC BY-NC 4.0](https://img.shields.io/badge/license-CC%20BY--NC%204.0-lightgrey)](LICENSE)

> **10 个原子 skill（目录统一 `ai-` 前缀），专为 AI/ML 科研论文流程而生。**
> 每个 skill 只做一件事，自然语言触发，可独立调用，也能组合成完整管线。

---

## TL;DR — 想做什么就直说

| 你想做的事 | 直接说 | 触发的 skill |
|---|---|---|
| 找研究方向 | "give me ideas on long-context evaluation" / "想 idea" | [`ai-idea-forge`](ai-idea-forge/) |
| 调研文献 | "find recent papers on RLHF" / "文献调研" | [`ai-lit-scout`](ai-lit-scout/) |
| 和已有工作做差异化 | "position my work vs DPO and IPO" / "差异化定位" | [`ai-related-positioning`](ai-related-positioning/) |
| 设计实验 | "design experiment for X" / "实验方案" | [`ai-method-architect`](ai-method-architect/) |
| 写论文章节 | "draft method section" / "写方法部分" | [`ai-paper-writer`](ai-paper-writer/) |
| 画图表 | "plot accuracy vs context length" / "画图" | [`ai-figure-smith`](ai-figure-smith/) |
| 校验完整性 / 引用 | "check citations" / "完整性检查" | [`ai-integrity-check`](ai-integrity-check/) |
| 模拟评审 | "review my paper, NeurIPS-style" / "审稿" | [`ai-paper-reviewer`](ai-paper-reviewer/) |
| 回复评审 | "write rebuttal" / "回复评审" | [`ai-rebuttal-coach`](ai-rebuttal-coach/) |
| 投稿排版 | "format for NeurIPS 2026" / "排版投稿" | [`ai-venue-formatter`](ai-venue-formatter/) |
| 走完整流程 | "full pipeline for this idea" / "全流程" | [`ai-research-pipeline`](ai-research-pipeline/) (可选 meta) |

完整触发词与消歧规则见 [`docs/COMMAND_INDEX.md`](docs/COMMAND_INDEX.md)。

### 简体中文 Skill 文档

各 skill 的 **`SKILL.md` 完整中文说明**（简体）位于 [`zh-CN/`](zh-CN/README.md)，目录结构与根目录 `ai-*` 一一对应；`agents/`、`archive/`、`shared/` 仍以英文原文为准，中文文件内已用相对路径链回仓库。

---

## 安装（30 秒）

ai-research-skills 是纯 Markdown skill 集合，没有运行时依赖（lint 脚本除外）。

### Claude Code（重要：两层目录）

Claude Code **只**扫描形如 `~/.claude/skills/<skill-name>/SKILL.md` 的路径（**两层**：`skills` → `skill-name` → `SKILL.md`）。  
若把整个仓库放在 `~/.claude/skills/academic-research-skills/`，skill 实际在第三层 `.../ai-idea-forge/SKILL.md`，**不会被自动发现**。

**正确做法**：把本仓库里每个 skill 目录单独链到 `~/.claude/skills/` 下（11 个：10 个原子 + `ai-research-pipeline`）：

```bash
REPO=/path/to/academic-research-skills   # 或你的 git clone 路径
mkdir -p ~/.claude/skills
for s in ai-idea-forge ai-lit-scout ai-related-positioning ai-method-architect ai-paper-writer \
         ai-figure-smith ai-integrity-check ai-paper-reviewer ai-rebuttal-coach ai-venue-formatter \
         ai-research-pipeline; do
  ln -sf "$REPO/$s" "$HOME/.claude/skills/$s"
done
```

可选：保留 `~/.claude/skills/academic-research-skills -> $REPO` 方便你 `cd` 进整仓，但它**不是**一个 skill（根目录没有 `SKILL.md`），不能替代上面的 11 个链接。

改完后**完全退出并重启** Claude Code，再试自然语言触发（例如「想几个 long-context 的 idea」→ `ai-idea-forge`）。

### Cursor

Cursor 使用 `~/.cursor/skills/<skill-name>/` 或项目内 `.cursor/skills/`；同样要求 **每个 skill 为一级子目录**。可用与上面相同的 `for` 循环，把目标目录换成 `~/.cursor/skills`。

### 手动安装到其他 Agent

把每个 `<skill>/SKILL.md` 注册为可触发的 system prompt fragment，触发词从 frontmatter 的 `description: Triggers:` 段读取。

### 开发者依赖（可选）

```bash
pip install -r requirements-dev.txt
python scripts/check_skill_md_length.py
python scripts/check_trigger_words.py
python scripts/check_venue_db.py
python scripts/check_spec_consistency.py
```

---

## 设计原则

1. **原子优先** — 每个 skill 只做一件事；组合通过对话发生，不通过硬编码。
2. **AI/ML 专用** — 默认 venue 是 NeurIPS / ICLR / ICML / ACL / EMNLP / CVPR / AAAI / arXiv，论文结构是 `intro → related → method → experiments → conclusion`。
3. **自然语言触发** — 不需要记忆 slash command。每个 skill 在 frontmatter 声明 3-12 个非重叠触发词。
4. **诚信优先** — `ai-integrity-check` 是独立 skill，可以在任何阶段插入；7 类 AI 研究失败模式（hallucinated experiments, citation fabrication, etc.）有阻断式检查。
5. **可恢复** — 每个 skill 把状态写到 `.ars-state/`，"resume" 即可继续。
6. **不替代你的判断** — 所有创造性决策（idea 取舍、实验解读、reviewer 反馈如何改）都留给人。

---

## 典型工作流

### A. 想新 idea → 投稿

```
你: "想一些 long-context evaluation 方向的 idea"
→ ai-idea-forge 输出 5 个 idea card（含 novelty/feasibility/risk + Devil's Advocate 挑战）

你: "用第 3 个 idea 调研相关工作"
→ ai-lit-scout 找出 30 篇相关论文 + 验证 + 标注

你: "帮我设计实验"
→ ai-method-architect 给出 baselines / ablations / metrics / risk-of-bias

你: "写 method 和 experiments"
→ ai-paper-writer 起草

你: "画 accuracy vs context length 图"
→ ai-figure-smith 出图（matplotlib / tikz）

你: "完整性检查 + 模拟审稿"
→ ai-integrity-check + ai-paper-reviewer

你: "排版到 NeurIPS 格式"
→ ai-venue-formatter
```

### B. 收到评审意见 → rebuttal

```
你: "帮我解析这份 OpenReview 评审"
→ ai-rebuttal-coach review_parser → issue_inventory.yaml + 优先级

你: "起草 rebuttal"
→ ai-rebuttal-coach response_drafter（限 word budget，按 venue 调风格）

你: "再做一遍诚信检查"
→ ai-integrity-check
```

### C. 想偷懒走完整流程

```
你: "全流程，主题 long-context eval，目标 NeurIPS"
→ ai-research-pipeline 编排所有上面的 skill，3 个强制 checkpoint
```

---

## 项目结构

```
ai-research-skills/
├── README.md                    本文件
├── CHANGELOG.md                 v4.0.0 BREAKING release notes
├── LICENSE                      CC BY-NC 4.0
├── SECURITY.md / CONTRIBUTING.md
│
├── ai-idea-forge/                  ← 10 个原子 skill
├── ai-lit-scout/                       每个含 SKILL.md + agents/ + references/ + templates/
├── ai-related-positioning/
├── ai-method-architect/
├── ai-paper-writer/
├── ai-figure-smith/
├── ai-integrity-check/
├── ai-paper-reviewer/
├── ai-rebuttal-coach/
├── ai-venue-formatter/
├── ai-research-pipeline/           ← 可选 meta-skill，编排上面 10 个
│
├── shared/                      跨 skill 复用的资源
│   ├── agents/                  socratic_mentor / devils_advocate / state_tracker
│   ├── protocols/               anti_sycophancy / integrity_protocol
│   ├── venue_db/                NeurIPS / ICLR / ICML / ACL / EMNLP / CVPR / AAAI / arXiv（YAML）
│   └── *.md                     可复用的 pattern 文档（benchmark report / repro lock / 等）
│
├── docs/                        用户向文档
│   ├── COMMAND_INDEX.md         完整触发词、消歧、handoff 链
│   ├── AI_VENUE_GUIDE.md        AI venue 人工可读指南（venue_db 的 companion）
│   └── MIGRATION_v3_to_v4.md    v3.3 → v4.0 完整迁移映射
│
├── zh-CN/                       各 ai-* skill 的简体中文 SKILL.md 译本 + README
│
├── scripts/                     CI lint 脚本
│   ├── check_skill_md_length.py
│   ├── check_trigger_words.py
│   ├── check_venue_db.py
│   ├── check_spec_consistency.py
│   └── check_task_type.py / check_data_access_level.py 等
│
├── archive/                     ← v3.3 历史代码 / 文档
│   ├── README.md                归档说明 + 移除时间表
│   └── v3/                      4 个 v3 大 skill / v3 文档 / 旧 examples
│
└── .github/workflows/           CI（运行上面所有 lint）
```

---

## 触发词速查（精简版）

| Skill | 主触发词 | 备用触发词 |
|---|---|---|
| `ai-idea-forge` | give me ideas / brainstorm | novelty check, 想 idea |
| `ai-lit-scout` | find papers / literature | bibliography, 文献调研 |
| `ai-related-positioning` | position / differentiate | related work, 差异化定位 |
| `ai-method-architect` | design experiment | baselines, ablation, 实验方案 |
| `ai-paper-writer` | draft / write section | polish, revise, 写论文 |
| `ai-figure-smith` | plot / figure | table, 画图 |
| `ai-integrity-check` | verify / check citations | audit, 完整性检查 |
| `ai-paper-reviewer` | review my paper | NeurIPS-style review, 审稿 |
| `ai-rebuttal-coach` | write rebuttal | respond to reviewers, 回复评审 |
| `ai-venue-formatter` | format for X / camera-ready | compile, 排版投稿 |

完整触发词及消歧规则：[`docs/COMMAND_INDEX.md`](docs/COMMAND_INDEX.md)。

---

## v3.3.6 → v4.0 迁移

旧版（`academic-research-skills` v3.3.6）的 4 大 skill 已移到 `archive/v3/`，6 个月后（**2026-10-20**）从默认分支删除。

| 你以前用 | 现在改用 |
|---|---|
| `deep-research full` | `ai-lit-scout` + `ai-idea-forge` 组合 |
| `deep-research lit-review` | `ai-lit-scout` |
| `deep-research socratic` | 任意 skill 后接 "guide me Socratically" |
| `academic-paper full` | `ai-paper-writer` + `ai-figure-smith` + `ai-venue-formatter` |
| `academic-paper-reviewer full` | `ai-paper-reviewer` |
| `academic-pipeline` | `ai-research-pipeline`（更轻量） |

完整映射见 [`docs/MIGRATION_v3_to_v4.md`](docs/MIGRATION_v3_to_v4.md)。

---

## License

[CC BY-NC 4.0](LICENSE) — source-available, **non-commercial**. 学术用途、教学、研究协作免费；商业 SaaS / 付费咨询服务需要单独授权。

详见 [`SECURITY.md`](SECURITY.md) 和 [`CONTRIBUTING.md`](CONTRIBUTING.md)。

---

## 引用

如果 ai-research-skills 在你发表的工作中起了作用，可以这样致谢：

```
We acknowledge the use of ai-research-skills v4.0.0 (https://github.com/Imbad0202/academic-research-skills)
for {literature search / draft revision / integrity verification / rebuttal drafting}.
All scientific decisions, experimental design, and final text are the authors' responsibility.
```

完整 AI 使用披露模板见 [`shared/references/disclosure_mode_protocol.md`](shared/references/disclosure_mode_protocol.md)。
