# Cursor Agent Orchestra

**マルチエージェント協調フレームワーク**

Cursor Agent が Codex CLI（深い推論）と Gemini CLI（大規模リサーチ）を MCP 経由で統合し、各エージェントの強みを活かして開発を加速する。

---

## Dual-Mode Architecture

このプロジェクトは2つのオーケストレーターをサポート：

| Command | Orchestrator | Config |
|---------|--------------|--------|
| `claude` | Claude Code | `CLAUDE.md`, `.claude/` |
| `agent` | Cursor Agent | `AGENTS.md`, `.cursor/` |

**現在のモード: Cursor Agent**

---

## Why This Exists

| Agent | Strength | Use For |
|-------|----------|---------|
| **Cursor Agent** | オーケストレーション、ユーザー対話 | 全体統括、タスク管理 |
| **Codex CLI** | 深い推論、設計判断、デバッグ | 設計相談、エラー分析、トレードオフ評価 |
| **Gemini CLI** | 1Mトークン、マルチモーダル、Web検索 | コードベース全体分析、ライブラリ調査、PDF/動画処理 |

**IMPORTANT**: 単体では難しいタスクも、3エージェントの協調で解決できる。

---

## How to Call Codex/Gemini

Cursor Agent は **MCP (Model Context Protocol)** 経由で Codex/Gemini を呼び出す。

### Available MCP Tools

| Tool | Description |
|------|-------------|
| `codex_consult` | Codex に設計・デバッグを相談 |
| `codex_implement` | Codex にコード実装を依頼 |
| `gemini_research` | Gemini にリサーチを依頼 |
| `gemini_analyze` | Gemini にコードベース分析を依頼 |

### Usage Examples

```
# Design consultation
Use codex_consult tool: "How should I implement authentication?"

# Research
Use gemini_research tool: "What are the best practices for Python async?"

# Codebase analysis
Use gemini_analyze tool: "Understand the architecture of this project"
```

---

## Quick Reference

### Codex を使う時

- 設計判断（「どう実装？」「どのパターン？」）
- デバッグ（「なぜ動かない？」「エラーの原因は？」）
- 比較検討（「AとBどちらがいい？」）

→ 詳細: `.cursor/rules/codex-delegation.mdc`

### Gemini を使う時

- リサーチ（「調べて」「最新の情報は？」）
- 大規模分析（「コードベース全体を理解して」）
- マルチモーダル（「このPDF/動画を見て」）

→ 詳細: `.cursor/rules/gemini-delegation.mdc`

---

## Workflow

1. ユーザーがタスクを依頼
2. Cursor Agent が必要に応じて Codex/Gemini を MCP 経由で呼び出し
3. 結果を統合してユーザーに報告
4. 実装・テスト・コミット

---

## Tech Stack

- **Python** / **uv** (pip禁止)
- **ruff** (lint/format) / **ty** (type check) / **pytest**
- `poe lint` / `poe test` / `poe all`

→ 詳細: `.cursor/rules/dev-environment.mdc`

---

## Documentation

| Location | Content |
|----------|---------|
| `.cursor/rules/` | コーディング・セキュリティ・言語ルール |
| `.claude/docs/DESIGN.md` | 設計決定の記録（共有） |
| `.claude/docs/research/` | 調査結果（共有） |

---

## Language Protocol

- **思考・コード**: 英語
- **ユーザー対話**: 日本語
