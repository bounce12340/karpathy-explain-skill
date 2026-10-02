# Karpathy Explain — ELI5 风格的工程讲解技能

[English](README.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md)

可复用的 [Agent Skill](https://agentskills.io/)，用于讲解代码、架构、错误、PR 和技术文档：**降低阅读门槛，同时保留工程判断所需的证据**。灵感来自 [Andrej Karpathy 2026 年 10 月 2 日的帖子](https://x.com/karpathy/status/2105819303471976479)：清晰文字 → 图解 → 交互式 HTML → 可选讲解视频；并采用 ELI5 式、按读者水平讲解但不居高临下的方法。

**独立项目，并非 Karpathy 创建、背书或维护；未声称已实测缩短理解时间。**

## 功能

1. **先核实**：读取来源，区分代码可见事实、实测、推断与未知；尽量附文件／行号、函数、日志或文档段落。
2. **分层**：30 秒摘要与类比 → 3 分钟成功／失败数据流 → 实现细节与验证步骤，并说明类比哪里不适用。
3. **选择最轻的有效形式**：文字、图解、自包含交互式 HTML；确有帮助时才做分镜或视频。
4. **保留风险**：权限、数据丢失、安全、竞态、性能与未知点不会因简化而消失。

参见[交互式功能图解](examples/index.html)和[三个合成示例](examples/examples.md)（繁体中文）。技能会使用用户的语言回复。

## 安装

技能位于 [`skills/karpathy-explain/SKILL.md`](skills/karpathy-explain/SKILL.md)。先 clone：

```bash
git clone https://github.com/bounce12340/karpathy-explain-skill.git
cd karpathy-explain-skill
```

### Claude Code

个人安装（本机所有项目）：

```bash
mkdir -p ~/.claude/skills
cp -R skills/karpathy-explain ~/.claude/skills/
```

项目安装（可提交给团队）：复制到 `<repo>/.claude/skills/karpathy-explain/`。使用 `/karpathy-explain` 调用，或直接用自然语言请求工程讲解。文档：[Skills](https://code.claude.com/docs/en/skills)。

### Codex

用户安装：

```bash
mkdir -p ~/.agents/skills
cp -R skills/karpathy-explain ~/.agents/skills/
```

项目安装：复制到 `<repo>/.agents/skills/karpathy-explain/`。在 Codex CLI 或 IDE 扩展中运行 `/skills`，或输入 `$karpathy-explain`；未出现时重启 Codex。文档：[Build skills](https://developers.openai.com/codex/skills)。

### Hermes Agent

从 GitHub 安装（含 Hermes 安全扫描）：

```bash
hermes skills inspect bounce12340/karpathy-explain-skill/skills/karpathy-explain
hermes skills install bounce12340/karpathy-explain-skill/skills/karpathy-explain
```

手动安装：复制到 `~/.hermes/skills/engineering/karpathy-explain/`。如需多个工具共用，可在 `~/.hermes/config.yaml` 的 `skills.external_dirs` 中加入 `~/.agents/skills`。文档：[Skills System](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills)。

### 其他兼容 Agent Skills 的工具

将 `skills/karpathy-explain/` 复制到该工具的技能目录。本技能只有指令文本，不需要 API key、npm 包、脚本或网络；`eli5`、`frontend-design` 技能可增强效果，但不是必需依赖。

## 试用

> 用 karpathy-explain 向刚接手此模块的工程师讲解 `〈源码或文档路径〉`：先给出 30 秒 ELI5 式摘要，再画出成功与失败路径，最后列出三个值得查看的源码位置及尚未验证的假设。请用简体中文回答。

真实项目请提供文件、仓库、日志或网址；没有来源时应标注为假设示例。

## 许可

[MIT](LICENSE)。Karpathy 的帖子只是呈现方式的灵感；技能文字由本项目独立撰写，未包含外部技能源码。用户项目资料仍受其自身条款约束。
