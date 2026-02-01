# Cursor Agent Orchestra

**マルチエージェント協調フレームワーク**

Cursor Agent が Codex CLI（深い推論）と Gemini CLI（大規模リサーチ）を Bash 経由で統合し、各エージェントの強みを活かして開発を加速する。

---

## Dual-Mode Architecture

このプロジェクトは2つのオーケストレーターをサポート：

| Command | Orchestrator | Config |
|---------|--------------|--------|
| `claude` | Claude Code | `CLAUDE.md`, `.claude/` |
| Cursor | Cursor Agent | `AGENTS.md`, `.cursor/` |

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

Cursor Agent は **Bash** 経由で直接 Codex/Gemini を呼び出す（Claude Code と同じ設計）。

### Codex CLI

```bash
# 設計・デバッグ相談（read-only）
codex exec --model gpt-5.2-codex --sandbox read-only --full-auto "prompt" 2>/dev/null

# コード実装（workspace-write）
codex exec --model gpt-5.2-codex --sandbox workspace-write --full-auto "prompt" 2>/dev/null
```

### Gemini CLI

```bash
# リサーチ
gemini -p "prompt" 2>/dev/null

# コードベース分析
gemini -p "prompt" --include-directories . 2>/dev/null

# マルチモーダル（PDF等）
gemini -p "prompt" < file.pdf 2>/dev/null
```

---

## Skills

Cursor Agent で `/` を入力してスキルを実行できます。

| Skill | Description |
|-------|-------------|
| `/codex` | Codex CLI に設計・デバッグを相談 |
| `/gemini` | Gemini CLI でリサーチ |
| `/startproject` | マルチエージェント協調でプロジェクト開始 |
| `/init` | プロジェクト分析・AGENTS.md 更新 |
| `/plan` | 実装計画を作成 |
| `/tdd` | テスト駆動開発 |
| `/design-tracker` | 設計決定を自動記録 |
| `/update-design` | 設計ドキュメントを明示的に更新 |
| `/simplify` | コードをシンプル化 |
| `/review` | コードレビュー |
| `/research-lib` | ライブラリ調査・ドキュメント作成 |
| `/update-lib-docs` | ライブラリドキュメントを最新化 |
| `/checkpointing` | セッションを永続化 |

→ 詳細: `.cursor/skills/`

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
2. Cursor Agent が必要に応じて Bash で Codex/Gemini を呼び出し
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
