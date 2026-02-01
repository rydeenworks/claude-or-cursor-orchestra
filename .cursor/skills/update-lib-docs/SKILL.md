---
name: update-lib-docs
description: Update library documentation in .claude/docs/libraries/ with latest information.
---

# Update Library Documentation

**`.claude/docs/libraries/` のドキュメントを最新情報で更新する。**

## Steps

### 1. Check Existing Documents

現在のライブラリドキュメントを確認：

```bash
ls .claude/docs/libraries/
```

### 2. Search for Latest Info

各ライブラリについて検索（Web または Gemini）：

- 最新バージョン
- 破壊的変更
- 非推奨機能
- 新機能
- セキュリティアップデート

```bash
gemini -p "What are the latest updates for {library}?
Include: version changes, breaking changes, deprecations, security updates" 2>/dev/null
```

### 3. Update Documents

変更があったライブラリについて：

1. バージョン情報を更新
2. 新機能/制約を追加
3. 非推奨APIをマーク
4. 必要ならコード例を更新
5. 更新日をトップに記録

### 4. Check Impact on Code

ドキュメント更新後、確認：

- 非推奨APIを使用していないか？
- 破壊的変更の影響はあるか？
- プロジェクトの依存関係を更新する必要があるか？

## Key Items to Check

| カテゴリ | 確認内容 |
|----------|----------|
| Security | CVE、セキュリティパッチ |
| Breaking | API変更、削除された機能 |
| Deprecated | 削除予定のAPI |
| Performance | 最適化改善 |
| New Features | 有用な追加機能 |

## Update Format

ファイルのトップに更新通知を追加：

```markdown
# {Library Name}

> **Last Updated**: {Date}
> **Version Checked**: {version}

## Recent Changes

- {Change 1}
- {Change 2}

---

{Rest of documentation}
```

## Report

更新後、ユーザーに報告（日本語）：

- 更新したライブラリ
- 発見した重要な変更
- プロジェクトへのアクション項目
