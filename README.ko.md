# Karpathy Explain — ELI5 스타일 엔지니어링 설명 스킬

[English](README.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md)

[![validate](https://github.com/bounce12340/karpathy-explain-skill/actions/workflows/validate.yml/badge.svg)](https://github.com/bounce12340/karpathy-explain-skill/actions/workflows/validate.yml) ![license](https://img.shields.io/badge/license-MIT-blue)

> AI가 코드를 쓰는 속도가 우리가 이해하는 속도를 넘어섰습니다. 이 스킬은 이해를 돕습니다 — 근거 이상의 것을 아는 척하지 않으면서.

코드, 아키텍처, 버그, PR, 로그, 기술 문서를 설명하는 재사용 가능한 [Agent Skill](https://agentskills.io/)입니다. [Andrej Karpathy의 2026년 10월 2일 게시물](https://x.com/karpathy/status/2105819303471976479)(명확한 글 → 다이어그램 → 인터랙티브 HTML → 선택적 설명 영상)에서 영감을 받았고, 독자 수준에 맞추되 낮춰 보지 않는 ELI5 방식을 결합했습니다.

**독립 프로젝트이며 Karpathy가 만들거나 보증하거나 유지 관리하지 않습니다. 이해 시간 단축을 측정했다고 주장하지 않습니다.**

## 한 줄 설치

```bash
npx skills add bounce12340/karpathy-explain-skill
```

[`skills` CLI](https://github.com/vercel-labs/skills)가 설치할 agent를 묻습니다. `-a claude-code`, `-a codex`, `-a hermes-agent`로 직접 지정할 수 있고, `-g`를 붙이면 사용자 전체에 설치합니다. 수동 설치는 [아래](#수동-설치)를 참고하세요.

## 기능

| 단계 | 얻는 것 |
|---|---|
| ⏱ 30초 | 한 문장 요약, 일상적인 비유, 그리고 **비유가 맞지 않는 지점**(코드의 구체적인 줄로 확인) |
| ⏱ 3분 | 실제 데이터 흐름: 성공 경로, 실패 경로, 흔한 오해 |
| 🔍 심화 | 읽어야 할 파일과 줄, 경계와 트레이드오프, 검증 방법 |

중요한 주장마다 **근거 태그**가 붙어 얼마나 믿을 수 있는지 바로 알 수 있습니다:

`[확인됨 src/auth.ts:42]` · `[테스트됨]` · `[추론]` · `[미확인]`

`[확인됨 경로:줄]` 같은 앵커는 기계로 검사할 수 있습니다. 파일이나 줄이 없으면 `scripts/validate.py`가 실패합니다. 앵커는 그 줄이 존재함을 증명할 뿐, 여전히 주장을 뒷받침하는지는 보장하지 않습니다.

글, Mermaid 다이어그램, 독립 실행형 인터랙티브 HTML 중 가장 가벼운 유효한 형식을 고르며, 영상 스토리보드는 요청할 때만 만듭니다. **빠른 모드**는 30초 요약, 다음에 볼 곳, 미확인 사항만 제공합니다.

**ASD-STE100을 바탕으로 한 작성 규칙**으로 글을 쉽게 유지합니다: 누가 무엇을 했는지 쓰기, 한 단어 한 의미, 한 문단 한 주제, 한 줄에 긍정 질문 하나, 문장 성분 생략하지 않기, 짧은 문장. 실제 세션 10개의 답변 218개를 분석해 만들었으며, 각 규칙은 실제 혼란 사례에 대응합니다. STE 준수가 아니라 각색입니다.

활용: 낯선 코드 인수, AI가 생성한 PR 리뷰, 긴 에러 로그 읽기, 모듈 인계.

**자연스러운 문장 점검([Humanizer-zh](https://github.com/bounce12340/Humanizer-zh) 참고)**: 코드를 확인한 뒤 이해를 방해하는 빈 도입, 반복, 틀에 박힌 표현만 다듬습니다. 근거 태그, 불확실성, 필요한 기술 용어는 남깁니다. 다른 스킬은 선택 사항이며 AI 글 감지 또는 감지 회피를 보장하지 않습니다.

## 사용해 보기

```text
karpathy-explain을 사용해 이 모듈을 넘겨받은 엔지니어에게 <경로>를 설명해 주세요.
30초 요약을 먼저 주고, 성공과 실패 경로를 그린 뒤,
확인할 소스 위치 3곳과 검증되지 않은 가정을 나열해 주세요.
```

```text
karpathy-explain 빠른 모드로: 이 PR은 어떤 동작을 바꾸고, 무엇이 위험한가요?
```

스킬은 사용자의 언어로 답합니다. 소스가 없으면 검증된 설명이 아니라 가상의 예시임을 표시합니다.

**예시**

- [온라인 인터랙티브 다이어그램](https://bounce12340.github.io/karpathy-explain-skill/examples/index.html?lang=ko): 브라우저에서 바로 열리며 영어·번체·일본어·한국어·간체로 전환할 수 있습니다.
- [실제 워크스루](examples/real-walkthrough.md): 이 저장소의 검증 스크립트에 스킬을 적용한 예시. 모든 줄 번호를 CI가 자동 검사합니다(영어).
- [세 가지 합성 예시](examples/examples.en.md): API 403, 사라지는 초안, 엇갈린 CI 결과(영어, [번체 중국어판](examples/examples.md)도 있음).

## 수동 설치

먼저 clone 하세요:

```bash
git clone https://github.com/bounce12340/karpathy-explain-skill.git
cd karpathy-explain-skill
```

| Agent | 사용자 전체 | 프로젝트 단위 | 호출 |
|---|---|---|---|
| [Claude Code](https://code.claude.com/docs/en/skills) | `~/.claude/skills/` | `.claude/skills/` | `/karpathy-explain` |
| [Codex](https://developers.openai.com/codex/skills) | `~/.agents/skills/` | `.agents/skills/` | `/skills` 또는 `$karpathy-explain` |
| [Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills) | `~/.hermes/skills/` | `.hermes/skills/` | `/karpathy-explain` |

Hermes 프로젝트 단위 스킬은 저장소를 신뢰한 뒤에 로드됩니다: `hermes skills trust`.

폴더 전체(`references/` 포함)를 복사합니다:

```bash
mkdir -p ~/.claude/skills && cp -R skills/karpathy-explain ~/.claude/skills/
```

**Hermes Agent**는 GitHub에서 바로 설치할 수도 있습니다(보안 검사 포함):

```bash
hermes skills inspect bounce12340/karpathy-explain-skill/skills/karpathy-explain
hermes skills install bounce12340/karpathy-explain-skill/skills/karpathy-explain
```

스킬이 보이지 않으면 agent를 다시 시작하세요. 기타 Agent Skills 호환 도구는 `skills/karpathy-explain/`를 스킬 디렉터리에 복사하면 됩니다.

## 파일 구조

```text
skills/karpathy-explain/
├── SKILL.md                       # 스킬 본체(지침만 포함)
├── references/output-template.md  # 답변 골격, 근거 태그, Mermaid 템플릿
├── references/writing-rules.md     # ASD-STE100을 바탕으로 한 작성 규칙
└── references/natural-writing.md   # Humanizer-zh를 참고한 자연스러운 문장 점검
examples/                          # 인터랙티브 다이어그램(5개 언어)과 예시
CHANGELOG.md                       # 변경 이력. vX.Y.Z 태그를 푸시하면 Release 자동 게시
scripts/validate.py                # 형식·링크·근거 앵커·비밀 정보 검사(CI)
tests/                             # 검증 스크립트 회귀 테스트
```

PR을 열기 전에 실행하세요:

```bash
python3 scripts/validate.py
python3 -m unittest discover -s tests
```

## 현황과 한계

- 설치 경로는 각 agent의 공식 문서를 따랐으며, CI에서 `npx skills add . --list`가 스킬을 찾는지 검증합니다. 모든 agent에서 직접 테스트하지는 않았습니다. 이슈를 환영합니다.
- 코드를 읽지 않아도 되게 해 주지는 않습니다. **어디부터 읽어야 하는지**, **무엇이 아직 추측인지** 알려 줍니다.

## 라이선스

[MIT](LICENSE). 표현 방식은 Karpathy의 게시물에서 영감을 받았지만 스킬 문구는 독자적으로 작성했습니다. ELI5는 방법론으로 사용했으며 제3자 스킬 코드는 포함하지 않습니다.
