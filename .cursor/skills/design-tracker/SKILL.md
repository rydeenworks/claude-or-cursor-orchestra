---
name: design-tracker
description: |
  PROACTIVELY track and document project design decisions.
  Activate when detecting architecture discussions, implementation decisions,
  pattern choices, or library selections.
  Triggers: "記録して", "設計どうなってる", "record this"
---

# Design Tracker

**設計決定を `.claude/docs/DESIGN.md` に記録する。**

## Purpose

プロジェクトの設計ドキュメントを管理：
- アーキテクチャ決定
- 実装計画
- ライブラリ選択とその理由
- TODO項目と未解決の質問

## When to Activate

- アーキテクチャや設計パターンの議論時
- 実装決定時（例：「ReActパターンを使おう」）
- ユーザーが「記録して」「設計どうなってる」と言った時
- 重要な技術的決定が行われた時

## Workflow

### Recording Decisions

1. 既存の `.claude/docs/DESIGN.md` を読む
2. 会話から決定/情報を抽出
3. 適切なセクションを更新
4. Changelog に今日の日付でエントリを追加

### Sections to Update

| 会話のトピック | 更新セクション |
|---------------|----------------|
| 全体の目標、目的 | Overview |
| システム構造、コンポーネント | Architecture |
| パターン（ReAct等） | Implementation Plan > Patterns |
| ライブラリ選択 | Implementation Plan > Libraries |
| XをYより選んだ理由 | Implementation Plan > Key Decisions |
| 後で実装するもの | TODO |
| 未解決の質問 | Open Questions |

## Output Format

記録時、日本語で確認：
- 何を記録したか
- どのセクションを更新したか
- 変更の簡単な要約

## Language Rules

- **Thinking/Reasoning**: English
- **Code examples**: English
- **Document content**: English (technical terms) + Japanese (descriptions OK)
- **User communication**: Japanese
