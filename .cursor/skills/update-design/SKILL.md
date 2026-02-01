---
name: update-design
description: Explicitly update DESIGN.md with decisions from the current conversation.
---

# Update Design Document

**会話内容に基づいて `.claude/docs/DESIGN.md` に設計決定を記録/更新する。**

> **Note**: design-tracker と同じワークフローを明示的に呼び出します。

## Workflow

1. 既存の `.claude/docs/DESIGN.md` を読む
2. 会話から決定/情報を抽出
3. 適切なセクションを更新
4. Changelog に今日の日付でエントリを追加

## Section Mapping

| トピック | セクション |
|---------|---------|
| ゴール、目的 | Overview |
| 構造、コンポーネント | Architecture |
| デザインパターン | Implementation Plan > Patterns |
| ライブラリ選択 | Implementation Plan > Libraries |
| 決定理由 | Implementation Plan > Key Decisions |
| 将来の作業 | TODO |
| 未解決の問題 | Open Questions |

## Update Format

適切なセクションに追加：

```markdown
### Key Decisions

#### {Decision Title} ({Date})

**Context**: {Why this decision was needed}
**Decision**: {What was decided}
**Rationale**: {Why this option was chosen}
```

## Changelog Entry

必ず Changelog に追加：

```markdown
## Changelog

### {Date}
- {Brief description of what was recorded}
```

## Language

- ドキュメント内容: English (technical), Japanese OK for descriptions
- ユーザーへの報告: Japanese

$ARGUMENTS が指定されていれば、その内容の記録に集中する。
