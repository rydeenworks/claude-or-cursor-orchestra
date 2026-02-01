# Code Review

**$ARGUMENTS のコードをレビューする。**

## Review Process

### 1. Read Target Code

対象のコード/変更を確認：
- `git diff` で変更内容を確認
- 関連ファイルを読む

### 2. Codex Review

```bash
codex exec --model gpt-5.2-codex --sandbox read-only --full-auto "
Review this code:
{code or diff}

Check:
1. Code quality and patterns
2. Potential bugs
3. Missing edge cases
4. Security concerns
5. Performance issues
6. Readability
" 2>/dev/null
```

### 3. Report Findings

日本語でユーザーに報告：

```markdown
## コードレビュー結果

### 良い点
- {Good point 1}
- {Good point 2}

### 改善提案
- {Issue 1}: {suggestion}
- {Issue 2}: {suggestion}

### セキュリティ/パフォーマンス
- {Security/Performance concern if any}
```

## Review Checklist

- [ ] 単一責任の原則
- [ ] 適切な命名
- [ ] エラーハンドリング
- [ ] エッジケース処理
- [ ] テストカバレッジ
- [ ] セキュリティ（入力検証、SQLインジェクション等）
- [ ] パフォーマンス
- [ ] ドキュメント/コメント

## For Pull Request Review

```bash
# 変更内容を確認
git diff main...HEAD

# Codexでレビュー
codex exec --model gpt-5.2-codex --sandbox read-only --full-auto "
Review this PR diff:
$(git diff main...HEAD)

Provide:
1. Overall assessment
2. Specific issues with line numbers
3. Suggestions for improvement
" 2>/dev/null
```
