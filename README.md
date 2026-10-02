# Karpathy Explain — an ELI5-inspired engineering explanation skill

[English](README.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md)

[![validate](https://github.com/bounce12340/karpathy-explain-skill/actions/workflows/validate.yml/badge.svg)](https://github.com/bounce12340/karpathy-explain-skill/actions/workflows/validate.yml) ![license](https://img.shields.io/badge/license-MIT-blue)

> AI writes code faster than we can understand it. This skill helps you understand it — without pretending to know more than the evidence shows.

A reusable [Agent Skill](https://agentskills.io/) for explaining code, architecture, bugs, PRs, logs, and technical documents. Inspired by [Andrej Karpathy's October 2, 2026 post](https://x.com/karpathy/status/2105819303471976479): clear writing → diagrams → interactive HTML → optional explainer video, combined with an ELI5 approach that adapts to the reader without talking down to them.

**Independent project — not created, endorsed, or maintained by Andrej Karpathy.** No measured improvement in comprehension time is claimed.

## Quick install

```bash
npx skills add bounce12340/karpathy-explain-skill
```

The [`skills` CLI](https://github.com/vercel-labs/skills) asks which agents to install for. Target one directly with `-a claude-code`, `-a codex`, or `-a hermes-agent`; add `-g` for a user-wide install. Manual steps for each agent are [below](#manual-install).

## What it does

| Layer | You get |
|---|---|
| ⏱ 30 seconds | One sentence, an everyday analogy, and **where the analogy breaks**, checked against a line of code |
| ⏱ 3 minutes | The real data flow: success path, failure path, common misconception |
| 🔍 Deep dive | Files and lines to read, boundaries and trade-offs, how to verify |

Every important claim carries an **evidence tag** so you know what to trust:

`[confirmed src/auth.ts:42]` · `[tested]` · `[inferred]` · `[unknown]`

Anchors like `[confirmed path:line]` are machine-checkable: `scripts/validate.py` fails if the file or line does not exist. A valid anchor proves the line exists, not that it still supports the claim.

It picks the lightest format that works — text, a Mermaid diagram (or an ASCII diagram in terminals that cannot render Mermaid), self-contained interactive HTML, or a video storyboard only when you ask for one. Say "explain in HTML" to get a single-file interactive page directly. A **quick mode** returns just the 30-second summary, where to look next, and what's unverified.

**Writing rules adapted from ASD-STE100** keep the text plain: say who did what, one word per meaning, one topic per paragraph, one positive question per line, no dropped sentence parts, short sentences. They come from analyzing 218 replies in 10 real sessions; each rule maps to an observed point of confusion. This is an adaptation, not STE compliance.

Good for: onboarding onto unfamiliar code, reviewing AI-generated PRs, reading long error logs, and handing over modules.

## Try it

```text
Use karpathy-explain to explain <path> to an engineer taking over this module.
Give a 30-second summary, draw the success and failure paths,
then list three source locations to read and any unverified assumptions.
```

```text
Use karpathy-explain in quick mode: what behavior does this PR change, and what's risky?
```

The skill replies in your language. Without source material, it labels the answer as a hypothetical example rather than a verified explanation.

**Examples**

- [Live interactive diagram](https://bounce12340.github.io/karpathy-explain-skill/examples/index.html?lang=en) — opens in the browser; switch between English, 繁體中文, 日本語, 한국어, and 简体中文.
- [Real walkthrough](examples/real-walkthrough.md) — the skill applied to this repo's own validator. Every line reference is checked by CI.
- [Three synthetic examples](examples/examples.en.md) — API 403, disappearing drafts, mixed CI results ([繁體中文](examples/examples.md)).

## Manual install

Clone first:

```bash
git clone https://github.com/bounce12340/karpathy-explain-skill.git
cd karpathy-explain-skill
```

| Agent | User-wide | Per project | Invoke |
|---|---|---|---|
| [Claude Code](https://code.claude.com/docs/en/skills) | `~/.claude/skills/` | `.claude/skills/` | `/karpathy-explain` |
| [Codex](https://developers.openai.com/codex/skills) | `~/.agents/skills/` | `.agents/skills/` | `/skills` or `$karpathy-explain` |
| [Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills) | `~/.hermes/skills/` | `.hermes/skills/` | `/karpathy-explain` |

Hermes project skills load only after you trust the repo: `hermes skills trust`.

Copy the whole folder (it includes `references/`):

```bash
mkdir -p ~/.claude/skills && cp -R skills/karpathy-explain ~/.claude/skills/
```

**Hermes Agent** can also install straight from GitHub with its security scan:

```bash
hermes skills inspect bounce12340/karpathy-explain-skill/skills/karpathy-explain
hermes skills install bounce12340/karpathy-explain-skill/skills/karpathy-explain
```

Restart the agent if the skill does not appear. Any other Agent Skills–compatible tool works the same way: copy `skills/karpathy-explain/` into its skill directory.

## Repository layout

```text
skills/karpathy-explain/
├── SKILL.md                       # the skill (instruction-only)
├── references/output-template.md  # response skeleton, evidence tags, Mermaid template
└── references/writing-rules.md     # writing rules adapted from ASD-STE100
examples/                          # interactive diagram (5 languages) + examples
CHANGELOG.md                       # version history; tags vX.Y.Z publish a Release
scripts/validate.py                # spec, links, evidence anchors, secrets (CI)
tests/                             # validator regression tests
```

Before opening a PR:

```bash
python3 scripts/validate.py
python3 -m unittest discover -s tests
```

## Status and limits

- Install paths follow each agent's official docs; `npx skills add . --list` is verified in CI. Not yet hands-on tested inside every agent — issues welcome.
- It does not replace reading the code. It tells you **where to read first** and **what is still a guess**.

## Attribution and license

The presentation ladder is inspired by Karpathy's linked post. The skill text is independently written; ELI5 is used as an approach, and no third-party skill code is bundled. [MIT](LICENSE).
