---
name: checkpointing
description: |
  Save session context to agent configuration files or create full checkpoint files.
  Supports session history (default), full checkpoint (--full),
  and skill analysis (--full --analyze).
---

# Checkpointing

**セッションコンテキストを永続化する。**

## Modes

### Mode 1: Session History（デフォルト）

CLI相談履歴を各エージェントの設定ファイルに追記。

```bash
python .claude/skills/checkpointing/checkpoint.py
```

### Mode 2: Full Checkpoint（--full）

作業全体の包括的なスナップショットを作成。

```bash
python .claude/skills/checkpointing/checkpoint.py --full
```

### Mode 3: Skill Analysis（--full --analyze）

チェックポイントからスキル化できるパターンを発見。

```bash
python .claude/skills/checkpointing/checkpoint.py --full --analyze
```

## When to Use

| タイミング | 推奨モード |
|-----------|-----------|
| セッション終了前 | `--full --analyze` |
| 重要な設計決定後 | `--full` |
| 大きな機能実装完了後 | `--full --analyze` |
| 長時間作業の区切り | `--full` |
| 日次の軽い記録 | デフォルト |

## Output

### Session History モード
- `CLAUDE.md`, `AGENTS.md`, `GEMINI.md` に `## Session History` を追記

### Full Checkpoint モード
- `.claude/checkpoints/YYYY-MM-DD-HHMMSS.md` にスナップショットを保存

### Skill Analysis モード
- Full Checkpoint + 分析プロンプト生成
- スキル候補を提案

## Full Checkpoint Format

```markdown
# Checkpoint: 2026-01-28 15:30:00 UTC

## Summary
- **Commits**: 5
- **Files changed**: 12
- **Codex consultations**: 3
- **Gemini researches**: 2

## Git History
### Commits
- `abc1234` Add feature

### File Changes
**Created:**
- `new_feature.py` (+120)

**Modified:**
- `existing.py` (+80, -20)

## CLI Tool Consultations
### Codex
- ✓ 設計相談...

### Gemini
- ✓ 調査...
```

## Notes

- ログが空の場合は何も追記されない
- Git未初期化でもCLIログ部分は動作
- `--analyze` のスキル提案は人間がレビューしてから採用
