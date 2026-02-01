# Implementation Plan: Cursor CLI Orchestration

## Purpose

`agent` コマンド（Cursor CLI）で起動した際に、Cursor が Codex/Gemini を直接統括するデュアルモード対応を実現する。

## Current State

```
claude コマンド → Claude Code が統括 → Codex/Gemini
```

## Target State

```
claude コマンド → Claude Code が統括 → Codex/Gemini  (現状維持)
agent コマンド  → Cursor CLI が統括 → Codex/Gemini  (新規作成)
```

## Scope

### New files
- `AGENTS.md` - Cursor 用メインコンテキスト
- `.cursor/rules/*.mdc` - Cursor 用ルールファイル（MDC形式）
- `.cursor/mcp.json` - プロジェクト固有 MCP 設定
- `src/mcp/codex_server.py` - Codex MCP サーバー
- `src/mcp/gemini_server.py` - Gemini MCP サーバー

### Preserved files (no changes)
- `CLAUDE.md` - Claude Code 用（維持）
- `.claude/` - Claude Code 設定全体（維持）

### Dependencies
- `mcp` (Python MCP SDK)
- `codex-as-mcp` (optional, existing solution)

---

## Implementation Steps

### Step 1: Create AGENTS.md

Cursor CLI 用のメインコンテキストファイルを作成。

- [ ] `AGENTS.md` を作成（`CLAUDE.md` をベースに Cursor 向けに調整）
- [ ] オーケストレーション構造を Cursor 中心に記述
- [ ] Codex/Gemini への委譲ルールを記載

**Verification**: `agent` コマンドで起動時に `AGENTS.md` が読み込まれる

---

### Step 2: Create .cursor/rules/ directory

MDC 形式のルールファイルを作成。

- [ ] `.cursor/rules/` ディレクトリ作成
- [ ] `codex-delegation.mdc` - Codex 委譲ルール
- [ ] `gemini-delegation.mdc` - Gemini 委譲ルール
- [ ] `coding-principles.mdc` - コーディング原則
- [ ] `language.mdc` - 言語ルール
- [ ] `dev-environment.mdc` - 開発環境ルール

**Verification**: `agent` コマンドでルールが適用される

---

### Step 3: Create MCP Servers for Codex/Gemini

Cursor から Codex/Gemini を呼び出すための MCP サーバーを作成。

- [ ] `src/mcp/` ディレクトリ作成
- [ ] `codex_server.py` - Codex CLI をラップする MCP サーバー
- [ ] `gemini_server.py` - Gemini CLI をラップする MCP サーバー
- [ ] `pyproject.toml` に依存関係追加

**Verification**: MCP サーバーが単体で動作する

---

### Step 4: Configure .cursor/mcp.json

プロジェクト固有の MCP 設定を作成。

- [ ] `.cursor/mcp.json` を作成
- [ ] Codex MCP サーバーを登録
- [ ] Gemini MCP サーバーを登録

**Verification**: `agent` コマンドで MCP ツールが利用可能

---

### Step 5: Test Dual-Mode Operation

両方のモードが正しく動作することを確認。

- [ ] `claude` コマンドで Claude Code 統括モードをテスト
- [ ] `agent` コマンドで Cursor CLI 統括モードをテスト
- [ ] Codex/Gemini の呼び出しが両モードで動作することを確認

**Verification**: 両コマンドで適切なオーケストレーターが統括する

---

## File Structure (After Implementation)

```
claude-code-orchestra/
├── CLAUDE.md                    # Claude Code 用（維持）
├── AGENTS.md                    # Cursor CLI 用（新規）
├── .claude/                     # Claude Code 設定（維持）
│   ├── rules/
│   ├── skills/
│   ├── hooks/
│   └── ...
├── .cursor/                     # Cursor CLI 設定（新規）
│   ├── rules/
│   │   ├── codex-delegation.mdc
│   │   ├── gemini-delegation.mdc
│   │   ├── coding-principles.mdc
│   │   ├── language.mdc
│   │   └── dev-environment.mdc
│   └── mcp.json
├── src/
│   └── mcp/
│       ├── codex_server.py
│       └── gemini_server.py
└── pyproject.toml
```

---

## Risks & Considerations

1. **MCP サーバーの安定性**
   - 自作 MCP サーバーの動作検証が必要
   - `codex-as-mcp` 等の既存ソリューションの評価も検討

2. **Cursor CLI の制約**
   - シェルコマンド実行時に承認が必要な場合がある
   - MCP 経由での呼び出しでこれを回避できるか検証

3. **設定の重複**
   - `.claude/rules/` と `.cursor/rules/` で内容が重複
   - 将来的に共通化の仕組みを検討（symlink 等）

---

## Open Questions

1. **MCP サーバーの実装方式**
   - 既存の `codex-as-mcp` を使用するか、自作するか
   - Gemini 用の既存 MCP サーバーはあるか

2. **ルールの共通化**
   - `.claude/rules/` と `.cursor/rules/` を共通化する方法はあるか
   - MDC 形式と Markdown 形式の変換が必要か
