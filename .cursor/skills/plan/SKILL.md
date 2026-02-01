---
name: plan
description: Create a detailed implementation plan for a feature or task. Use when user wants to plan before coding.
---

# Create Implementation Plan

**$ARGUMENTS の実装計画を作成する。**

## Planning Process

### 1. Requirements Analysis

まず明確化：

- **Purpose**: 何を達成するか
- **Scope**: 含めるもの・除外するもの
- **Constraints**: 技術的制約、時間、依存関係

### 2. Current State Investigation

コードベースを調査：

- 関連する既存コード
- 影響を受けるファイル
- 使用するライブラリ/パターン
- 既存のテスト

### 3. Break Down Implementation Steps

小さなステップに分解：

1. 各ステップは独立してテスト可能
2. 依存関係の順序を考慮
3. リスクの高いステップを先に

### 4. Output Format

```markdown
## Implementation Plan: {Title}

### Purpose
{1-2 sentences}

### Scope
- New files: {list}
- Modified files: {list}
- Dependencies: {list}

### Implementation Steps

#### Step 1: {Title}
- [ ] {Specific task}
- [ ] {Specific task}
**Verification**: {Completion criteria for this step}

#### Step 2: {Title}
...

### Risks & Considerations
- {Potential issues and mitigations}

### Open Questions
- {Items to clarify before implementation}
```

## Optional: Codex Review

計画を Codex でレビュー：

```bash
codex exec --model gpt-5.2-codex --sandbox read-only --full-auto "
Review this implementation plan:
{plan}

Analyze approach, risks, and suggest improvements.
" 2>/dev/null
```

## Notes

- 計画は実行可能な粒度で
- 各ステップに検証方法を含める
- 不明点は計画段階で質問
- 過度に詳細化しない（実装時に調整）
