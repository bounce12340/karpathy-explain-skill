# Karpathy Explain — ELI5 スタイルのエンジニアリング解説スキル

[English](README.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md)

[![validate](https://github.com/bounce12340/karpathy-explain-skill/actions/workflows/validate.yml/badge.svg)](https://github.com/bounce12340/karpathy-explain-skill/actions/workflows/validate.yml) ![license](https://img.shields.io/badge/license-MIT-blue)

> AI がコードを書く速さは、私たちが理解する速さを超えました。このスキルは理解を助けます——根拠以上のことを知っているふりはせずに。

コード、アーキテクチャ、バグ、PR、ログ、技術文書を説明するための再利用可能な [Agent Skill](https://agentskills.io/) です。[Andrej Karpathy の 2026 年 10 月 2 日の投稿](https://x.com/karpathy/status/2105819303471976479)（明快な文章 → 図解 → インタラクティブ HTML → 任意の解説動画）に着想を得て、読み手に合わせつつ見下さない ELI5 的な説明を組み合わせています。

**独立したプロジェクトであり、Karpathy 氏による作成・推奨・保守ではありません。理解時間の短縮を実測したとは主張しません。**

## ワンライナーでインストール

```bash
npx skills add bounce12340/karpathy-explain-skill
```

[`skills` CLI](https://github.com/vercel-labs/skills) がインストール先の agent を尋ねます。`-a claude-code`、`-a codex`、`-a hermes-agent` で直接指定でき、`-g` でユーザー全体にインストールします。手動の手順は[下記](#手動インストール)を参照してください。

## できること

| レイヤー | 得られるもの |
|---|---|
| ⏱ 30 秒 | 一文の要約、身近な例え、そして**例えが成り立たない点**（コードの具体的な行で確認） |
| ⏱ 3 分 | 実際のデータフロー：成功経路、失敗経路、よくある誤解 |
| 🔍 詳細 | 読むべきファイルと行、境界とトレードオフ、検証方法 |

重要な主張にはすべて**根拠タグ**が付き、どこまで信頼できるか一目で分かります：

`[確認済み src/auth.ts:42]` · `[テスト済み]` · `[推測]` · `[不明]`

`[確認済み パス:行]` のようなアンカーは機械的に検証できます。ファイルや行が存在しなければ `scripts/validate.py` が失敗します。アンカーはその行が存在することを示すだけで、主張を今も裏付けているとは限りません。

文章、Mermaid 図、自己完結型のインタラクティブ HTML から最小限で効果的な形式を選び、動画の絵コンテは依頼された場合のみ作成します。**クイックモード**では 30 秒の要約、次に見る場所、未確認事項だけを返します。

**ASD-STE100 を基にした文章ルール**で文章を平易に保ちます：誰が何をしたかを書く、一語一義、一段落一トピック、一行に肯定形の質問を一つ、文の要素を省かない、文を短く。10 の実際のセッションにある 218 件の回答を分析したもので、各ルールは実際の混乱に対応しています。STE への準拠ではなく翻案です。

用途：見知らぬコードの引き継ぎ、AI が生成した PR のレビュー、長いエラーログの読解、モジュールの引き継ぎ。

## 試す

```text
karpathy-explain を使って、このモジュールを引き継ぐエンジニアに <パス> を説明してください。
30 秒の要約を示し、成功と失敗の経路を図示し、
確認すべきソース位置を 3 つと未検証の前提を挙げてください。
```

```text
karpathy-explain のクイックモードで：この PR はどんな挙動を変え、何がリスクですか？
```

スキルはあなたの言語で回答します。ソースがない場合は、検証済みの説明ではなく仮の例であることを明示します。

**例**

- [オンラインのインタラクティブ図解](https://bounce12340.github.io/karpathy-explain-skill/examples/index.html?lang=ja)：ブラウザで直接開けます。英語・繁体字・日本語・韓国語・簡体字を切り替え可能。
- [実例ウォークスルー](examples/real-walkthrough.md)：このリポジトリの検証スクリプトにスキルを適用した例。行番号はすべて CI で自動チェックされます（英語）。
- [3 つの合成例](examples/examples.en.md)：API 403、消える下書き、CI の結果不一致（英語。[繁体字中国語版](examples/examples.md)もあります）。

## 手動インストール

まず clone します：

```bash
git clone https://github.com/bounce12340/karpathy-explain-skill.git
cd karpathy-explain-skill
```

| Agent | ユーザー全体 | プロジェクト単位 | 呼び出し |
|---|---|---|---|
| [Claude Code](https://code.claude.com/docs/en/skills) | `~/.claude/skills/` | `.claude/skills/` | `/karpathy-explain` |
| [Codex](https://developers.openai.com/codex/skills) | `~/.agents/skills/` | `.agents/skills/` | `/skills` または `$karpathy-explain` |
| [Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills) | `~/.hermes/skills/` | `.hermes/skills/` | `/karpathy-explain` |

Hermes のプロジェクト単位のスキルは、リポジトリを信頼した後に読み込まれます：`hermes skills trust`。

フォルダ全体（`references/` を含む）をコピーします：

```bash
mkdir -p ~/.claude/skills && cp -R skills/karpathy-explain ~/.claude/skills/
```

**Hermes Agent** は GitHub から直接インストールすることもできます（セキュリティスキャン付き）：

```bash
hermes skills inspect bounce12340/karpathy-explain-skill/skills/karpathy-explain
hermes skills install bounce12340/karpathy-explain-skill/skills/karpathy-explain
```

スキルが表示されない場合は agent を再起動してください。その他の Agent Skills 対応ツールでは、`skills/karpathy-explain/` をスキルディレクトリにコピーしてください。

## ファイル構成

```text
skills/karpathy-explain/
├── SKILL.md                       # スキル本体（指示文のみ）
├── references/output-template.md  # 回答の骨組み、根拠タグ、Mermaid テンプレート
└── references/writing-rules.md     # ASD-STE100 を基にした文章ルール
examples/                          # インタラクティブ図解（5 言語）と例
CHANGELOG.md                       # 変更履歴。vX.Y.Z タグで Release を自動公開
scripts/validate.py                # 形式・リンク・根拠アンカー・機密情報チェック（CI）
tests/                             # 検証スクリプトの回帰テスト
```

PR を出す前に実行してください：

```bash
python3 scripts/validate.py
python3 -m unittest discover -s tests
```

## 現状と制限

- インストール手順は各 agent の公式ドキュメントに基づいています。CI で `npx skills add . --list` がスキルを検出できることを確認しています。すべての agent での実機テストはまだです。Issue を歓迎します。
- コードを読む必要はなくなりません。**どこから読むべきか**、**何がまだ推測か**を教えてくれます。

## ライセンス

[MIT](LICENSE)。表現方法は Karpathy 氏の投稿に着想を得ていますが、スキルの文章は独自に作成したものです。ELI5 は手法として用いており、第三者のスキルコードは含みません。
