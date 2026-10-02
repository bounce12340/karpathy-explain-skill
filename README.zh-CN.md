# Karpathy Explain — ELI5 风格的工程讲解技能

[English](README.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md)

[![validate](https://github.com/bounce12340/karpathy-explain-skill/actions/workflows/validate.yml/badge.svg)](https://github.com/bounce12340/karpathy-explain-skill/actions/workflows/validate.yml) ![license](https://img.shields.io/badge/license-MIT-blue)

> AI 写代码的速度，已经超过我们看懂它的速度。这个技能帮你看懂——而且不假装知道证据以外的事。

可复用的 [Agent Skill](https://agentskills.io/)，用于讲解代码、架构、错误、PR、日志和技术文档。灵感来自 [Andrej Karpathy 2026 年 10 月 2 日的帖子](https://x.com/karpathy/status/2105819303471976479)：清晰文字 → 图解 → 交互网页 → 可选讲解视频；并结合 ELI5，按读者水平讲解但不居高临下。

**独立项目，并非 Karpathy 创建、背书或维护；未声称已实测缩短理解时间。**

## 一行安装

```bash
npx skills add bounce12340/karpathy-explain-skill
```

[`skills` CLI](https://github.com/vercel-labs/skills) 会询问要安装给哪些 agent。也可直接指定 `-a claude-code`、`-a codex` 或 `-a hermes-agent`；加 `-g` 安装到用户级。各家手动安装见[下方](#手动安装)。

## 功能

| 层级 | 你会得到 |
|---|---|
| ⏱ 30 秒 | 一句话、生活类比，以及**类比在哪里不成立** |
| ⏱ 3 分钟 | 真实数据流：成功路径、失败路径、常见误解 |
| 🔍 深入 | 该看的文件与行号、边界与取舍、验证方法 |

每个重要结论都有**证据标记**，一眼看出能不能信：

`[已确认 src/auth.ts:42]` · `[实测]` · `[推断]` · `[未知]`

它会选择够用的最简单形式：文字、Mermaid 图、自包含交互 HTML；只有你要求时才做视频分镜。**快速模式**只给 30 秒摘要、下一步看哪里、哪些还没确认。

适合：接手陌生代码、审查 AI 生成的 PR、阅读很长的错误日志、交接模块。

## 试用

```text
用 karpathy-explain 向刚接手这个模块的工程师讲解〈路径〉：
先给 30 秒摘要，再画出成功与失败路径，
最后列出 3 个该看的源码位置和尚未验证的假设。
```

```text
用 karpathy-explain 快速模式：这个 PR 改变了什么行为？有什么风险？
```

技能会用你的语言回复。没有提供来源时，会标注为假设示例，而非经核实的结论。

参见[交互功能图解](examples/index.html)和[三个合成示例](examples/examples.md)（繁体中文）。

## 手动安装

先 clone：

```bash
git clone https://github.com/bounce12340/karpathy-explain-skill.git
cd karpathy-explain-skill
```

| Agent | 用户级 | 项目级 | 调用方式 |
|---|---|---|---|
| [Claude Code](https://code.claude.com/docs/en/skills) | `~/.claude/skills/` | `.claude/skills/` | `/karpathy-explain` |
| [Codex](https://developers.openai.com/codex/skills) | `~/.agents/skills/` | `.agents/skills/` | `/skills` 或 `$karpathy-explain` |
| [Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills) | `~/.hermes/skills/` | `.hermes/skills/` | `/karpathy-explain` |

Hermes 的项目级技能需先信任该仓库：`hermes skills trust`。

复制整个文件夹（含 `references/`）：

```bash
mkdir -p ~/.claude/skills && cp -R skills/karpathy-explain ~/.claude/skills/
```

**Hermes Agent** 也可直接从 GitHub 安装（含安全扫描）：

```bash
hermes skills inspect bounce12340/karpathy-explain-skill/skills/karpathy-explain
hermes skills install bounce12340/karpathy-explain-skill/skills/karpathy-explain
```

技能没出现时请重启 agent。其他兼容 Agent Skills 的工具，把 `skills/karpathy-explain/` 复制到技能目录即可。

## 文件结构

```text
skills/karpathy-explain/
├── SKILL.md                       # 技能本体（纯指令文本）
└── references/output-template.md  # 回复骨架、证据标记、Mermaid 模板
examples/                          # 交互图解与合成示例
scripts/validate.py                # 格式、链接、密钥检查（CI 会运行）
```

提交 PR 前请运行 `python3 scripts/validate.py`。

## 状态与限制

- 安装路径依据各家官方文档编写；CI 会验证 `npx skills add . --list` 能找到技能。尚未在每家 agent 实机测试，欢迎反馈问题。
- 它不会让你不用读代码，而是告诉你**先读哪里**、**哪些还是猜的**。

## 许可

[MIT](LICENSE)。呈现方式受 Karpathy 帖子启发；技能文字为独立撰写，ELI5 是采用的方法，未包含第三方技能代码。
