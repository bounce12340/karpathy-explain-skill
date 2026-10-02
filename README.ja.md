# Karpathy Explain — ELI5 スタイルのエンジニアリング解説スキル

[English](README.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md)

コード、アーキテクチャ、バグ、PR、技術文書を説明するための再利用可能な [Agent Skill](https://agentskills.io/) です。**理解のハードルを下げつつ、エンジニアの判断に必要な根拠は残します。** [Andrej Karpathy の 2026 年 10 月 2 日の投稿](https://x.com/karpathy/status/2105819303471976479)（明快な文章 → 図解 → インタラクティブな HTML → 任意の解説動画）に着想を得ています。また、相手のレベルに合わせつつ見下さない ELI5 的な説明方法を取り入れています。

**独立したプロジェクトであり、Karpathy 氏による作成・推奨・保守ではありません。理解時間の短縮を実測したとは主張しません。**

## できること

1. **根拠を確認**：提供されたソースを読み、コード上の事実、テスト結果、推測、不明点を区別します。可能ならファイル／行、関数、ログ、文書の箇所を示します。
2. **段階的に説明**：30 秒の要約と例え → 3 分の成功／失敗データフロー → 実装の詳細と検証手順。例えが当てはまらない点も示します。
3. **最小限で効果的な形式を選択**：文章、図解、自己完結型のインタラクティブ HTML。役立つ場合のみ絵コンテや動画を作成します。
4. **リスクを残す**：認可、データ消失、セキュリティ、競合状態、性能、不明点を単純化で消しません。

[インタラクティブな機能図](examples/index.html)と[3 つの合成例](examples/examples.md)（繁体字中国語）をご覧ください。スキルはユーザーの言語で回答します。

## インストール

スキル本体は [`skills/karpathy-explain/SKILL.md`](skills/karpathy-explain/SKILL.md) です。まず clone します。

```bash
git clone https://github.com/bounce12340/karpathy-explain-skill.git
cd karpathy-explain-skill
```

### Claude Code

個人用（このマシンのすべてのプロジェクト）：

```bash
mkdir -p ~/.claude/skills
cp -R skills/karpathy-explain ~/.claude/skills/
```

プロジェクト用（チームで共有するならコミット）：`<repo>/.claude/skills/karpathy-explain/` にコピーします。`/karpathy-explain` で呼び出すか、自然な言葉で解説を依頼してください。ドキュメント：[Skills](https://code.claude.com/docs/en/skills)。

### Codex

ユーザー用：

```bash
mkdir -p ~/.agents/skills
cp -R skills/karpathy-explain ~/.agents/skills/
```

リポジトリ用：`<repo>/.agents/skills/karpathy-explain/` にコピーします。Codex CLI または IDE 拡張で `/skills` を実行するか、`$karpathy-explain` と入力します。表示されない場合は Codex を再起動してください。ドキュメント：[Build skills](https://developers.openai.com/codex/skills)。

### Hermes Agent

GitHub からインストール（Hermes のセキュリティスキャン付き）：

```bash
hermes skills inspect bounce12340/karpathy-explain-skill/skills/karpathy-explain
hermes skills install bounce12340/karpathy-explain-skill/skills/karpathy-explain
```

手動の場合：`~/.hermes/skills/engineering/karpathy-explain/` にコピーします。複数ツールで共有するには、`~/.hermes/config.yaml` の `skills.external_dirs` に `~/.agents/skills` を追加します。ドキュメント：[Skills System](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills)。

### その他の Agent Skills 対応ツール

`skills/karpathy-explain/` を各ツールのスキルディレクトリにコピーしてください。指示文のみのスキルで、API キー、npm パッケージ、スクリプト、ネットワークは不要です。`eli5` や `frontend-design` スキルは補助として使えますが、必須ではありません。

## 試す

> karpathy-explain を使って、`<ソースコードまたは文書のパス>` をこのコンポーネントを引き継ぐエンジニアに説明してください。まず 30 秒の ELI5 風の要約、次に成功と失敗の経路を示し、最後に確認すべきソース位置を 3 つと未検証の前提を挙げてください。日本語で回答してください。

実際のコードでは、ファイル、リポジトリ、ログ、URL を提供してください。ソースがない場合、回答は検証済みではなく仮の例として示されるべきです。

## ライセンス

[MIT](LICENSE)。Karpathy 氏の投稿は表現方法の着想元にすぎません。スキルの文章は本プロジェクトで独自に作成し、外部スキルのソースコードは含みません。ユーザーのプロジェクト資料には、そのプロジェクト自身の条件が適用されます。
