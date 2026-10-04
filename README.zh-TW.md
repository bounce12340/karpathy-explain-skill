# Karpathy Explain — ELI5 風格的工程解說技能

[English](README.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md)

[![validate](https://github.com/bounce12340/karpathy-explain-skill/actions/workflows/validate.yml/badge.svg)](https://github.com/bounce12340/karpathy-explain-skill/actions/workflows/validate.yml) ![license](https://img.shields.io/badge/license-MIT-blue)

> AI 寫程式的速度，已經超過我們看懂它的速度。這個技能幫你看懂——而且不假裝知道證據以外的事。

可重複使用的 [Agent Skill](https://agentskills.io/)，用來解釋程式碼、架構、錯誤、PR、log 與技術文件。靈感來自 [Andrej Karpathy 2026 年 10 月 2 日的貼文](https://x.com/karpathy/status/2105819303471976479)：清楚文字 → 圖解 → 互動網頁 → 可選解說影片；並結合 ELI5，依讀者程度說明但不把人當小孩。

**獨立作品，並非 Karpathy 建立、背書或維護；未宣稱已實測縮短理解時間。**

## 一行安裝

```bash
npx skills add bounce12340/karpathy-explain-skill
```

[`skills` CLI](https://github.com/vercel-labs/skills) 會詢問要裝給哪些 agent。也可直接指定 `-a claude-code`、`-a codex` 或 `-a hermes-agent`；加 `-g` 安裝到使用者層級。各家手動安裝見[下方](#手動安裝)。

## 功能

| 層級 | 你會得到 |
|---|---|
| ⏱ 30 秒 | 一句話、生活比喻，以及**比喻在哪裡不成立**（對照程式碼的具體行號） |
| ⏱ 3 分鐘 | 真實資料流：成功路徑、失敗路徑、常見誤解 |
| 🔍 深入 | 該看的檔案與行號、邊界與取捨、驗證方法 |

每個重要結論都有**證據標記**，一眼看出能不能信：

`[已確認 src/auth.ts:42]` · `[實測]` · `[推論]` · `[未知]`

`[已確認 路徑:行號]` 這種錨點可由機器檢查：檔案或行號不存在時，`scripts/validate.py` 會失敗。錨點只證明那一行存在，不證明它仍支持該結論。

它會選夠用的最簡單形式：文字、Mermaid 圖（終端機無法渲染時改用 ASCII 圖）、自包含互動 HTML；只有你要求時才做影片分鏡。說「用 HTML 解釋」就會直接產出單一檔案的互動頁。只有內容需要時才畫圖（3 個以上相關概念、有分支的流程、3 個以上面向的比較、層級、時間演進），並依資訊類型選圖的種類；修改既有頁面時只改要求的那一段。**快速模式**只給 30 秒摘要、下一步看哪裡、哪些還沒確認。

**改編自 ASD-STE100 的寫作規則**讓文字更白：說出誰做了什麼、一詞一義、一段一個主題、一句一個肯定問句、不省略句子成分、句子要短。這些規則來自分析 10 個真實工作階段的 218 則回覆，每條都對應到實際的困惑。這是改編，不是 STE 合規。

適合：接手陌生程式、審查 AI 產生的 PR、讀很長的錯誤 log、交接模組。

**自然文字檢查（借鏡 [Humanizer-zh](https://github.com/bounce12340/Humanizer-zh)）**：先核對程式碼，再修空泛鋪陳、重複或妨礙理解的模板句。保留證據標記、未知點和必要術語。另一項技能可選裝；這不是 AI 文字偵測器，也不保證通過偵測器。

## 試用

```text
用 karpathy-explain 向剛接手這個模組的工程師解釋〈路徑〉：
先給 30 秒摘要，再畫成功與失敗路徑，
最後列出 3 個該看的原始碼位置和尚未驗證的假設。
```

```text
用 karpathy-explain 快速模式：這個 PR 改變了什麼行為？有什麼風險？
```

技能會用你的語言回覆。沒有提供來源時，會標明是假設示範，而非經查證的結論。

**範例**

- [線上互動圖解](https://bounce12340.github.io/karpathy-explain-skill/examples/index.html?lang=zh-Hant)：直接在瀏覽器開啟，可切換英文、繁中、日文、韓文、簡中。
- [真實演練](examples/real-walkthrough.md)：把技能套用在本 repo 的驗證腳本上，每個行號都由 CI 自動檢查（英文）。
- [三個合成範例](examples/examples.md)：API 403、草稿消失、CI 一紅一綠（另有[英文版](examples/examples.en.md)）。

## 手動安裝

先 clone：

```bash
git clone https://github.com/bounce12340/karpathy-explain-skill.git
cd karpathy-explain-skill
```

| Agent | 使用者層級 | 專案層級 | 呼叫方式 |
|---|---|---|---|
| [Claude Code](https://code.claude.com/docs/en/skills) | `~/.claude/skills/` | `.claude/skills/` | `/karpathy-explain` |
| [Codex](https://developers.openai.com/codex/skills) | `~/.agents/skills/` | `.agents/skills/` | `/skills` 或 `$karpathy-explain` |
| [Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills) | `~/.hermes/skills/` | `.hermes/skills/` | `/karpathy-explain` |

Hermes 的專案層級技能需先信任該 repo：`hermes skills trust`。

複製整個資料夾（含 `references/`）：

```bash
mkdir -p ~/.claude/skills && cp -R skills/karpathy-explain ~/.claude/skills/
```

**Hermes Agent** 也可直接從 GitHub 安裝（含安全掃描）：

```bash
hermes skills inspect bounce12340/karpathy-explain-skill/skills/karpathy-explain
hermes skills install bounce12340/karpathy-explain-skill/skills/karpathy-explain
```

技能沒出現時請重啟 agent。其他相容 Agent Skills 的工具，把 `skills/karpathy-explain/` 複製到技能目錄即可。

## 檔案結構

```text
skills/karpathy-explain/
├── SKILL.md                       # 技能本體（純指示文字）
├── references/output-template.md  # 回覆骨架、證據標記、Mermaid 模板
├── references/writing-rules.md     # 改編自 ASD-STE100 的寫作規則
└── references/natural-writing.md   # 借鏡 Humanizer-zh 的自然文字檢查
examples/                          # 互動圖解（五語）與範例
CHANGELOG.md                       # 版本紀錄；推送 vX.Y.Z 標籤會自動發布 Release
scripts/validate.py                # 格式、連結、證據錨點、機密檢查（CI 會跑）
tests/                             # 驗證腳本的回歸測試
```

送 PR 前請執行：

```bash
python3 scripts/validate.py
python3 -m unittest discover -s tests
```

## 狀態與限制

- 安裝路徑依各家官方文件撰寫；CI 會驗證 `npx skills add . --list` 能找到技能。隔離 iSH/aarch64 使用 DeepSeek 相容服務的實測結果：Claude Code **v1.3.0 通過**（呼叫 Skill 工具、讀取程式並產出快速解說；較新版本未重測）；Codex CLI 0.160.0 **v1.3.1 受阻**（技能安裝成功，但轉送與直接 API 兩條路都無法完成模型回合，沒有成功使用技能的證據）。Hermes Agent 依使用者要求略過。
- 它不會讓你不用讀程式，而是告訴你**先讀哪裡**、**哪些還是猜的**。

## 授權

[MIT](LICENSE)。呈現方式受 Karpathy 貼文啟發；技能文字為獨立撰寫，ELI5 是採用的方法，未收錄第三方技能程式碼。
