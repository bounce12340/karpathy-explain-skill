# Karpathy Explain — ELI5 風格的工程解說技能

[English](README.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md)

可重複使用的 [Agent Skill](https://agentskills.io/)，用來解釋程式碼、架構、錯誤、PR 與技術文件：**降低閱讀門檻，同時保留工程判斷所需的證據**。靈感來自 [Andrej Karpathy 於 2026 年 10 月 2 日的貼文](https://x.com/karpathy/status/2105819303471976479)：清楚文字 → 圖解 → 互動 HTML → 可選解說影片；並採用 ELI5 式、依讀者程度說明但不居高臨下的方法。

**獨立作品，並非 Karpathy 建立、背書或維護；未宣稱已實測縮短理解時間。**

## 功能

1. **先查證**：讀取來源，區分程式可見事實、實測、推論與未知；盡量附檔案／行號、函式、log 或文件段落。
2. **分層**：30 秒摘要與類比 → 3 分鐘成功／失敗資料流 → 實作細節與驗證步驟，並說明類比哪裡不適用。
3. **選最輕的有效形式**：文字、圖解、自包含互動 HTML；確有幫助時才做分鏡或影片。
4. **保留風險**：授權、資料遺失、資安、競態、效能與未知點，不因簡化而消失。

參考[互動功能圖解](examples/index.html)與[三個合成範例](examples/examples.md)（繁體中文）。技能會依使用者語言回覆。

## 安裝

技能位於 [`skills/karpathy-explain/SKILL.md`](skills/karpathy-explain/SKILL.md)。先 clone：

```bash
git clone https://github.com/bounce12340/karpathy-explain-skill.git
cd karpathy-explain-skill
```

### Claude Code

個人安裝（本機所有專案）：

```bash
mkdir -p ~/.claude/skills
cp -R skills/karpathy-explain ~/.claude/skills/
```

專案安裝（可 commit 給團隊）：複製到 `<repo>/.claude/skills/karpathy-explain/`。用 `/karpathy-explain` 呼叫，或直接自然語言要求工程解說。文件：[Skills](https://code.claude.com/docs/en/skills)。

### Codex

使用者安裝：

```bash
mkdir -p ~/.agents/skills
cp -R skills/karpathy-explain ~/.agents/skills/
```

專案安裝：複製到 `<repo>/.agents/skills/karpathy-explain/`。在 Codex CLI 或 IDE 擴充執行 `/skills`，或輸入 `$karpathy-explain`；未出現時重啟 Codex。文件：[Build skills](https://developers.openai.com/codex/skills)。

### Hermes Agent

從 GitHub 安裝（含 Hermes 安全掃描）：

```bash
hermes skills inspect bounce12340/karpathy-explain-skill/skills/karpathy-explain
hermes skills install bounce12340/karpathy-explain-skill/skills/karpathy-explain
```

手動安裝：複製到 `~/.hermes/skills/engineering/karpathy-explain/`。若想多個工具共用，可在 `~/.hermes/config.yaml` 的 `skills.external_dirs` 加入 `~/.agents/skills`。文件：[Skills System](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills)。

### 其他相容 Agent Skills 的工具

把 `skills/karpathy-explain/` 複製到該工具的技能目錄。本技能只有指示文字，不需要 API key、npm 套件、腳本或網路；`eli5`、`frontend-design` 技能可加強效果，但不是必要依賴。

## 試用

> 用 karpathy-explain 向剛接手此模組的工程師解釋 `〈原始碼或文件路徑〉`：先給 30 秒 ELI5 式摘要，再畫成功與失敗路徑，最後列出三個值得看的原始碼位置及尚未驗證的假設。請用繁體中文回答。

真實專案請提供檔案、repo、log 或網址；沒有來源時應標示為假設示範。

## 授權

[MIT](LICENSE)。Karpathy 貼文只是呈現方式的靈感；技能文字為本專案獨立撰寫，未收錄外部技能原始碼。使用者專案資料仍受其自身條款約束。
