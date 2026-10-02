# Changelog

All notable changes to this skill. Versions match `metadata.version` in [SKILL.md](skills/karpathy-explain/SKILL.md).

## 1.3.2 — 2026-10-03

- Writing rule 7: put steps in a numbered list, one instruction per line (20 English words max), and keep instructions apart from descriptions.
- Diagrams: use an ASCII diagram where Mermaid does not render (terminals such as Claude Code and Codex). Also draw one when a process or structure has more than 3 steps or parts. Template added to `references/output-template.md`.
- "Explain in HTML" (「用 HTML 解釋」) is now an explicit trigger: convert the explanation into a single-file interactive HTML page without asking.

## 1.3.1 — 2026-10-03

- Where an analogy breaks must now be checked against the code: cite the specific behavior with `[confirmed path:line]` and quote the key part of that line. Prefer differences that would lead a reader to write wrong code (authorization, data loss, error handling, edge cases). If no matching code is found, mark it `[inferred]`.
- Reader self-check adds a sixth question: does the analogy's break point map to a line of code?

## 1.3.0 — 2026-10-02

- Writing rules adapted from ASD-STE100: active voice, one word one meaning, one topic per paragraph, one positive question per line, no dropped sentence parts, short descriptive sentences. Details and good/bad examples in [references/writing-rules.md](skills/karpathy-explain/references/writing-rules.md).
- Rules come from analyzing 218 replies in 10 real interactive sessions; each maps to an observed point of confusion. Not STE compliance; the STE dictionary is not applied to Chinese.

## 1.2.1 — 2026-10-02

- Interactive demo is now available in five languages (English, 繁體中文, 日本語, 한국어, 简体中文), with a language switcher, `?lang=` links, and browser-language detection.
- English version of the three synthetic examples: [examples/examples.en.md](examples/examples.en.md).
- Tag-driven release workflow: pushing `vX.Y.Z` validates, checks the version, and attaches a zipped skill with `SHA256SUMS.txt`.

## 1.2.0 — 2026-10-02

- Evidence anchors such as `[confirmed path:line]` are machine-checked: `scripts/validate.py` fails if the file or line does not exist.
- Real walkthrough of this repo's own validator; every line reference is checked in CI.
- Validator scans only git-tracked files; 13 regression tests.
- Live demo on GitHub Pages.

## 1.1.0 — 2026-10-02

- Quick mode, evidence tags (confirmed / tested / inferred / unknown), common scenarios (AI PR review, error logs, module handover).
- `references/output-template.md`: response skeleton, Mermaid template, reader self-check.
- Spec fields (`license`, `compatibility`, `metadata`), bilingual description.
- One-line install with `npx skills add`; validation CI.

## 1.0.0 — 2026-10-02

- Initial release: layered explanation (30 seconds / 3 minutes / deep dive), fact card, format ladder (text → diagram → HTML → video), five-language README.
