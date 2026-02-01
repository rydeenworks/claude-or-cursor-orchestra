# Implementation Plan: Cursor CLI Orchestration

## Purpose

Cursor Agent が Codex/Gemini を Bash 経由で直接呼び出すデュアルモード対応を実現する。

## Current State

```
claude コマンド → Claude Code が統括 → Codex/Gemini (Bash経由)
```

## Target State

```
claude コマンド → Claude Code が統括 → Codex/Gemini  (現状維持)
Cursor         → Cursor Agent が統括 → Codex/Gemini  (Bash経由、Claude Codeと同じ設計)
```

## Scope

### New files
- `AGENTS.md` - Cursor 用メインコンテキスト
- `.cursor/rules/*.mdc` - Cursor 用ルールファイル（MDC形式）

### Preserved files (no changes)
- `CLAUDE.md` - Claude Code 用（維持）
- `.claude/` - Claude Code 設定全体（維持）

### Design Decision
- **MCP は使用しない** - Bash 経由で直接 CLI を呼び出す（Claude Code と統一設計）
- Cursor も Claude Code と同様に hooks システムを持つため、同じアプローチが可能

---

## Implementation Steps

### Step 1: Create AGENTS.md ✅

Cursor 用のメインコンテキストファイルを作成。

- [x] `AGENTS.md` を作成（`CLAUDE.md` をベースに Cursor 向けに調整）
- [x] オーケストレーション構造を Cursor 中心に記述
- [x] Codex/Gemini への Bash 呼び出しルールを記載

---

### Step 2: Create .cursor/rules/ directory ✅

MDC 形式のルールファイルを作成。

- [x] `.cursor/rules/` ディレクトリ作成
- [x] `codex-delegation.mdc` - Codex 委譲ルール（Bash呼び出し）
- [x] `gemini-delegation.mdc` - Gemini 委譲ルール（Bash呼び出し）
- [x] `coding-principles.mdc` - コーディング原則
- [x] `language.mdc` - 言語ルール
- [x] `dev-environment.mdc` - 開発環境ルール

---

### Step 3: Test Dual-Mode Operation

両方のモードが正しく動作することを確認。

- [ ] `claude` コマンドで Claude Code 統括モードをテスト
- [ ] Cursor で Agent モードをテスト
- [ ] Codex/Gemini の Bash 呼び出しが両モードで動作することを確認

---

## File Structure (After Implementation)

```
claude-or-cursor-orchestra/
├── CLAUDE.md                    # Claude Code 用（維持）
├── AGENTS.md                    # Cursor Agent 用（新規）
├── .claude/                     # Claude Code 設定（維持）
│   ├── rules/
│   ├── skills/
│   ├── hooks/
│   └── ...
├── .cursor/                     # Cursor Agent 設定（新規）
│   └── rules/
│       ├── codex-delegation.mdc  # Bash で codex を呼び出す
│       ├── gemini-delegation.mdc # Bash で gemini を呼び出す
│       ├── coding-principles.mdc
│       ├── language.mdc
│       └── dev-environment.mdc
└── pyproject.toml
```

---

## Risks & Considerations

1. **設定の重複**
   - `.claude/rules/` と `.cursor/rules/` で内容が重複
   - 将来的に共通化の仕組みを検討（symlink 等）

2. **MDC vs Markdown 形式**
   - Claude Code は `.md`、Cursor は `.mdc` 形式
   - 内容は同じだがフロントマター形式が異なる

---

## Resolved Questions

1. ~~**MCP サーバーの実装方式**~~
   - → **MCP は使用しない**。Bash 経由で直接 CLI を呼び出す設計に統一。
   - Cursor も hooks を持つため、Claude Code と同じアプローチが可能。

2. **ルールの共通化**
   - 現状は両方にコピーして管理
   - 将来的に symlink や共通ディレクトリでの管理を検討
