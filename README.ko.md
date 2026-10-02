# Karpathy Explain — ELI5 스타일 엔지니어링 설명 스킬

[English](README.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md)

코드, 아키텍처, 버그, PR, 기술 문서를 설명하는 재사용 가능한 [Agent Skill](https://agentskills.io/)입니다. **이해의 진입 장벽은 낮추되, 엔지니어의 판단에 필요한 근거는 유지합니다.** [Andrej Karpathy의 2026년 10월 2일 게시물](https://x.com/karpathy/status/2105819303471976479)에서 영감을 받았습니다: 명확한 글 → 다이어그램 → 인터랙티브 HTML → 선택적 설명 영상. 또한 독자 수준에 맞추되 낮춰 보지 않는 ELI5 방식의 설명을 사용합니다.

**독립 프로젝트이며 Karpathy가 만들거나 보증하거나 유지 관리하지 않습니다. 이해 시간 단축을 측정했다고 주장하지 않습니다.**

## 기능

1. **근거 확인**: 제공된 소스를 읽고 코드에서 보이는 사실, 테스트 결과, 추론, 미확인 사항을 구분합니다. 가능하면 파일/줄, 함수, 로그, 문서 위치를 제시합니다.
2. **단계별 설명**: 30초 요약과 비유 → 3분 성공/실패 데이터 흐름 → 구현 세부 사항과 검증 단계. 비유가 맞지 않는 부분도 설명합니다.
3. **가장 가벼운 유효한 형식 선택**: 글, 다이어그램, 독립 실행형 인터랙티브 HTML. 도움이 될 때만 스토리보드나 영상을 만듭니다.
4. **위험 유지**: 권한, 데이터 손실, 보안, 경쟁 상태, 성능, 미확인 사항을 단순화 과정에서 지우지 않습니다.

[인터랙티브 기능 다이어그램](examples/index.html)과 [세 가지 합성 예시](examples/examples.md)(번체 중국어)를 참고하세요. 스킬은 사용자의 언어로 답합니다.

## 설치

스킬 파일은 [`skills/karpathy-explain/SKILL.md`](skills/karpathy-explain/SKILL.md)에 있습니다. 먼저 clone 하세요.

```bash
git clone https://github.com/bounce12340/karpathy-explain-skill.git
cd karpathy-explain-skill
```

### Claude Code

개인 설치(이 컴퓨터의 모든 프로젝트):

```bash
mkdir -p ~/.claude/skills
cp -R skills/karpathy-explain ~/.claude/skills/
```

프로젝트 설치(팀과 공유하려면 커밋): `<repo>/.claude/skills/karpathy-explain/`에 복사합니다. `/karpathy-explain`으로 호출하거나 자연어로 엔지니어링 설명을 요청하세요. 문서: [Skills](https://code.claude.com/docs/en/skills).

### Codex

사용자 설치:

```bash
mkdir -p ~/.agents/skills
cp -R skills/karpathy-explain ~/.agents/skills/
```

저장소 설치: `<repo>/.agents/skills/karpathy-explain/`에 복사합니다. Codex CLI 또는 IDE 확장에서 `/skills`를 실행하거나 `$karpathy-explain`을 입력하세요. 보이지 않으면 Codex를 다시 시작하세요. 문서: [Build skills](https://developers.openai.com/codex/skills).

### Hermes Agent

GitHub에서 설치(Hermes 보안 검사 포함):

```bash
hermes skills inspect bounce12340/karpathy-explain-skill/skills/karpathy-explain
hermes skills install bounce12340/karpathy-explain-skill/skills/karpathy-explain
```

수동 설치: `~/.hermes/skills/engineering/karpathy-explain/`에 복사합니다. 여러 도구에서 공유하려면 `~/.hermes/config.yaml`의 `skills.external_dirs`에 `~/.agents/skills`를 추가하세요. 문서: [Skills System](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills).

### 기타 Agent Skills 호환 도구

`skills/karpathy-explain/`를 해당 도구의 스킬 디렉터리에 복사하세요. 지침만 있는 스킬이므로 API 키, npm 패키지, 스크립트, 네트워크가 필요하지 않습니다. `eli5`나 `frontend-design` 스킬은 보완용이며 필수 의존성이 아닙니다.

## 사용해 보기

> karpathy-explain을 사용해 이 컴포넌트를 넘겨받은 엔지니어에게 `<소스 코드 또는 문서 경로>`를 설명해 주세요. 먼저 30초 ELI5 스타일 요약을 제공하고, 성공 및 실패 경로를 보여 준 다음, 확인할 소스 위치 세 곳과 검증되지 않은 가정을 나열해 주세요. 한국어로 답해 주세요.

실제 코드는 파일, 저장소, 로그 또는 URL을 제공하세요. 소스가 없으면 검증된 설명이 아니라 가상의 예시로 표시해야 합니다.

## 라이선스

[MIT](LICENSE). Karpathy의 게시물은 표현 방식의 영감일 뿐입니다. 스킬 문구는 이 프로젝트가 독자적으로 작성했으며 외부 스킬 소스 코드는 포함하지 않습니다. 사용자 프로젝트 자료에는 해당 프로젝트의 조건이 적용됩니다.
