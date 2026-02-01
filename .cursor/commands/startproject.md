# Start Project

**マルチエージェント協調でプロジェクトを開始する。**

## Task

$ARGUMENTS のプロジェクトを開始します。

## Workflow

```
Phase 1: Research (Gemini)
    ↓
Phase 2: Requirements (User Q&A)
    ↓
Phase 3: Design Review (Codex)
    ↓
Phase 4: Task Creation
    ↓
Phase 5: AGENTS.md Update
```

---

## Phase 1: Gemini Research

```bash
gemini -p "Analyze this repository for: {feature}

Provide:
1. Repository structure and architecture
2. Relevant existing code and patterns
3. Library recommendations
4. Technical considerations
" --include-directories . 2>/dev/null
```

結果を `.claude/docs/research/{feature}.md` に保存。

---

## Phase 2: Requirements Gathering

ユーザーに質問（日本語）：

1. **目的**: 何を達成したいですか？
2. **スコープ**: 含めるもの・除外するものは？
3. **技術的要件**: 特定のライブラリ、制約は？
4. **成功基準**: 完了の判断基準は？

---

## Phase 3: Codex Design Review

```bash
codex exec --model gpt-5.2-codex --sandbox read-only --full-auto "
Review this implementation plan:
{plan from Phase 2}

Analyze:
1. Approach assessment
2. Risk analysis
3. Implementation order
4. Improvements
" 2>/dev/null
```

---

## Phase 4: Task Creation

タスクリストを作成してユーザーに提示。

---

## Phase 5: AGENTS.md Update

プロジェクト情報を AGENTS.md に追記：

```markdown
---

## Current Project: {feature}

### Context
- Goal: {1-2 sentences}
- Key files: {list}
- Dependencies: {list}

### Decisions
- {Decision 1}: {rationale}
```

---

## Final Output

```markdown
## プロジェクト計画: {feature}

### 調査結果 (Gemini)
{Key findings - 3-5 bullet points}

### 設計方針 (Codex レビュー済み)
{Approach with refinements}

### タスクリスト
{Task list}

### リスクと注意点
{From Codex analysis}

---
この計画で進めてよろしいですか？
```
