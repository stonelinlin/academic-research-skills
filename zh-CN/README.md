# 中文版本（zh-CN）

本目录存放 **ai-research-skills** 各原子 skill 的 **简体中文** `SKILL.md` 译本，与仓库根目录下英文 skill 目录 **一一对应**。

## 目录结构

```
zh-CN/
├── README.md                 # 本文件
├── ai-idea-forge/SKILL.md
├── ai-lit-scout/SKILL.md
├── ai-related-positioning/SKILL.md
├── ai-method-architect/SKILL.md
├── ai-paper-writer/SKILL.md
├── ai-figure-smith/SKILL.md
├── ai-integrity-check/SKILL.md
├── ai-paper-reviewer/SKILL.md
├── ai-rebuttal-coach/SKILL.md
├── ai-venue-formatter/SKILL.md
└── ai-research-pipeline/SKILL.md
```

## 与英文版的关系

| 项目 | 说明 |
|------|------|
| **权威来源** | 英文版 `../ai-*/SKILL.md` 为规范；若与中文有歧义，以英文为准。 |
| `name` 字段 | 与英文相同（`ai-idea-forge` 等），便于工具与路由一致。 |
| `description` | 中文说明 + 保留英文触发短语（Triggers），便于自然语言匹配。 |
| **Agent / 协议** | 正文仍引用 `../../ai-*/agents/`、`../../archive/v3/`、`../../shared/` 下的 **英文原文**；未单独翻译 agents。 |

## Claude Code / Cursor 如何使用

- 默认 skill 发现路径为 `~/.claude/skills/<name>/SKILL.md`（两层深度）。  
- 若希望使用 **中文** `SKILL.md`，可将该 skill 的 symlink 指向 **`zh-CN/<name>/`** 而非根目录的 `ai-<name>/`，或复制 `SKILL.md` 覆盖（自行维护同步）。  
- 推荐：**开发/阅读用中文目录**；**自动发现仍用英文根目录**，避免双份维护冲突。

## 维护

- 英文 skill 升级时，请同步更新对应 `zh-CN/*/SKILL.md` 的 `metadata.version` 与正文差异。
- 英文 skill 的 `metadata.version` 见各 `ai-*/SKILL.md`；中文译本在 frontmatter 中标注 **`language: zh-CN`**，版本号与发布时英文 suite 对齐（当前 **4.1.1**）。
