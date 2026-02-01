---
name: init
description: Analyze project structure and update AGENTS.md with detected tech stack, commands, and configurations.
---

# Initialize Project Configuration

**プロジェクトを分析し AGENTS.md を更新する。**

## Steps

### 1. Project Analysis

以下のファイルを探して技術スタックを特定：

- `package.json` → Node.js/TypeScript project
- `pyproject.toml` / `setup.py` / `requirements.txt` → Python project
- `Cargo.toml` → Rust project
- `go.mod` → Go project
- `Makefile` / `Dockerfile` → Build/deploy config
- `.github/workflows/` → CI/CD config

また検出：

- npm scripts / poe tasks / make targets → 共通コマンド
- 主要ライブラリ/フレームワーク

### 2. Ask User

ユーザーに質問：

1. **プロジェクト概要**: このプロジェクトは何をしますか？（1-2文）
2. **コード言語**: コメント/変数名は英語？日本語？
3. **追加ルール**: 他に従うべきコーディング規約は？

### 3. Update AGENTS.md

以下の形式で更新：

```markdown
# Project Overview

{User's answer}

## Language Settings

- **Thinking/Reasoning**: English
- **Code**: {Based on analysis}
- **User Communication**: Japanese

## Tech Stack

- **Language**: {Detected language}
- **Package Manager**: {Detected tools}
- **Dev Tools**: {Detected tools}
- **Main Libraries**: {Detected libraries}

## Common Commands

```bash
# Detected commands
{npm run dev / poe test / make build etc.}
```
```

### 4. Check Unnecessary Rules

`.cursor/rules/` のルールをチェックし、不要なものを削除提案：

- 非Pythonプロジェクト → `dev-environment.mdc`（uv/ruff/ty）は不要かも
- テストなしプロジェクト → `testing` 関連は不要かも

### 5. Report Completion

ユーザーに報告（日本語）：

- 検出した技術スタック
- 更新したセクション
- 削除推奨のルール（あれば）
