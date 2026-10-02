# Karpathy Explain — an ELI5-inspired engineering explanation skill

[English](README.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md)

A reusable [Agent Skill](https://agentskills.io/) for explaining code, architecture, bugs, PRs, and technical documents while keeping the evidence engineers need. Inspired by [Andrej Karpathy's October 2, 2026 post](https://x.com/karpathy/status/2105819303471976479): clear writing → diagrams → interactive HTML → optional explainer video. It also applies an ELI5-style approach: explain from the reader's level without talking down to them.

**Independent project. Not created, endorsed, or maintained by Andrej Karpathy.** No measured improvement in comprehension time is claimed.

## What it does

1. **Ground it:** read the supplied source; separate observed code, tested behavior, inference, and unknowns. Cite file/line, function, log, or document section when available.
2. **Layer it:** 30-second summary and analogy → 3-minute success/failure data flow → implementation details and verification steps. State where the analogy breaks.
3. **Choose the lightest useful format:** concise text, diagram, self-contained interactive HTML, or optional storyboard/video only when it helps.
4. **Keep engineering risk visible:** authorization, data loss, security, concurrency, performance, and unknowns are not simplified away.

See the [interactive feature diagram](examples/index.html) and [three synthetic examples](examples/examples.md). These demo files are in Traditional Chinese; the skill answers in the user's language.

## Install

The skill lives at [`skills/karpathy-explain/SKILL.md`](skills/karpathy-explain/SKILL.md). Clone once:

```bash
git clone https://github.com/bounce12340/karpathy-explain-skill.git
cd karpathy-explain-skill
```

### Claude Code

Personal install (all projects on this machine):

```bash
mkdir -p ~/.claude/skills
cp -R skills/karpathy-explain ~/.claude/skills/
```

Project install (commit it for your team):

```bash
mkdir -p .claude/skills
cp -R /path/to/karpathy-explain-skill/skills/karpathy-explain .claude/skills/
```

Use it with `/karpathy-explain`, or ask naturally for an engineering explanation. Claude Code docs: [Skills](https://code.claude.com/docs/en/skills).

### Codex

User install:

```bash
mkdir -p ~/.agents/skills
cp -R skills/karpathy-explain ~/.agents/skills/
```

Repository install: copy the folder to `<repo>/.agents/skills/karpathy-explain/`. In Codex CLI or the IDE extension, run `/skills` or mention `$karpathy-explain`. Restart Codex if it does not appear. Codex docs: [Build skills](https://developers.openai.com/codex/skills).

### Hermes Agent

Install from GitHub with Hermes's security scan:

```bash
hermes skills inspect bounce12340/karpathy-explain-skill/skills/karpathy-explain
hermes skills install bounce12340/karpathy-explain-skill/skills/karpathy-explain
```

Manual alternative: copy the folder to `~/.hermes/skills/engineering/karpathy-explain/`. For a shared cross-tool directory, add `~/.agents/skills` to `skills.external_dirs` in `~/.hermes/config.yaml`. Hermes docs: [Skills System](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills).

### Other Agent Skills-compatible tools

Copy `skills/karpathy-explain/` into that tool's skill directory. The skill is instruction-only: no API key, npm package, script, or network access is required. Optional local `eli5` or `frontend-design` skills can complement it but are not dependencies.

## Try it

> Use karpathy-explain to explain `<path to source code or document>` to an engineer taking over this component. Start with a 30-second ELI5-style summary, show the success and failure paths, then list three source locations to inspect and any unverified assumptions. Reply in English.

For real code, provide files, a repository, logs, or URLs. Without source material, responses should be labeled hypothetical rather than verified.

## Repository contents

- `skills/karpathy-explain/SKILL.md` — skill instructions (written in Traditional Chinese; replies follow the user's language).
- `examples/index.html` — offline, keyboard-accessible interactive diagram.
- `examples/examples.md` — three synthetic examples.
- `README.*.md` — English, Japanese, Korean, Simplified Chinese, and Traditional Chinese guides.

## Attribution and license

The presentation ladder is inspired by Karpathy's linked post. This skill and wording are independently authored; ELI5 is used as an explanation approach, and no external skill source code is bundled. Content supplied from a user's project remains subject to that project's terms. Licensed under [MIT](LICENSE).
