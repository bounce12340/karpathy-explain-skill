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
| ⏱ 30 秒 | 一句话、生活类比，以及**类比在哪里不成立**（对照代码的具体行号） |
| ⏱ 3 分钟 | 真实数据流：成功路径、失败路径、常见误解 |
| 🔍 深入 | 该看的文件与行号、边界与取舍、验证方法 |

每个重要结论都有**证据标记**，一眼看出能不能信：

`[已确认 src/auth.ts:42]` · `[实测]` · `[推断]` · `[未知]`

`[已确认 路径:行号]` 这类锚点可由机器检查：文件或行号不存在时，`scripts/validate.py` 会失败。锚点只证明那一行存在，不证明它仍支持该结论。

它会选择够用的最简单形式：文字、Mermaid 图、自包含交互 HTML；只有你要求时才做视频分镜。**快速模式**只给 30 秒摘要、下一步看哪里、哪些还没确认。

**改编自 ASD-STE100 的写作规则**让文字更直白：说出谁做了什么、一词一义、一段一个主题、一句一个肯定问句、不省略句子成分、句子要短。这些规则来自分析 10 个真实会话的 218 条回复，每条都对应实际的困惑。这是改编，不是 STE 合规。

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

**示例**

- [在线交互图解](https://bounce12340.github.io/karpathy-explain-skill/examples/index.html?lang=zh-Hans)：直接在浏览器打开，可切换英文、繁中、日文、韩文、简中。
- [真实演练](examples/real-walkthrough.md)：把技能用在本仓库的验证脚本上，每个行号都由 CI 自动检查（英文）。
- [三个合成示例](examples/examples.md)：API 403、草稿消失、CI 一红一绿（繁体中文；另有[英文版](examples/examples.en.md)）。

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
├── references/output-template.md  # 回复骨架、证据标记、Mermaid 模板
└── references/writing-rules.md     # 改编自 ASD-STE100 的写作规则
examples/                          # 交互图解（五语）与示例
CHANGELOG.md                       # 版本记录；推送 vX.Y.Z 标签会自动发布 Release
scripts/validate.py                # 格式、链接、证据锚点、密钥检查（CI 会运行）
tests/                             # 验证脚本的回归测试
```

提交 PR 前请运行：

```bash
python3 scripts/validate.py
python3 -m unittest discover -s tests
```

## 状态与限制

- 安装路径依据各家官方文档编写；CI 会验证 `npx skills add . --list` 能找到技能。尚未在每家 agent 实机测试，欢迎反馈问题。
- 它不会让你不用读代码，而是告诉你**先读哪里**、**哪些还是猜的**。

## 许可

[MIT](LICENSE)。呈现方式受 Karpathy 帖子启发；技能文字为独立撰写，ELI5 是采用的方法，未包含第三方技能代码。
