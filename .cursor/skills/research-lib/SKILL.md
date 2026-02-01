---
name: research-lib
description: Research a library and create comprehensive documentation in .claude/docs/libraries/.
---

# Research Library

**$ARGUMENTS を調査し `.claude/docs/libraries/` にドキュメントを作成する。**

## Research Items

### Always Verify via Web Search or Gemini

- 公式ドキュメント
- GitHub README
- PyPI / npm ページ
- 最新リリースノート

### Content to Document

1. **Basic Information**
   - 正式名称、バージョン、ライセンス
   - 公式URL
   - インストールコマンド

2. **Core Features**
   - 主要機能
   - 基本的な使い方（コード例）

3. **Constraints & Notes**
   - 既知の制限
   - 他ライブラリとの競合
   - パフォーマンス特性
   - async/sync の考慮事項

4. **Usage Patterns in This Project**
   - 推奨される使い方
   - 避けるべきパターン

5. **Troubleshooting**
   - よくあるエラーと解決策

## Gemini Research

```bash
gemini -p "Research {library}:
1. Core features and basic usage
2. Known limitations and constraints
3. Best practices and anti-patterns
4. Common errors and solutions
" 2>/dev/null
```

## Output Location

`.claude/docs/libraries/$ARGUMENTS.md`

## Documentation Template

```markdown
# {Library Name}

## Overview

- **Version**: {version}
- **License**: {license}
- **Official URL**: {url}
- **Installation**: `{install command}`

## Core Features

{Description of main features}

## Basic Usage

\`\`\`python
{Code example}
\`\`\`

## Constraints & Notes

- {Limitation 1}
- {Limitation 2}

## Recommended Patterns

### Do

\`\`\`python
{Good pattern}
\`\`\`

### Don't

\`\`\`python
{Anti-pattern}
\`\`\`

## Troubleshooting

### {Error message}

**Cause**: {cause}
**Solution**: {solution}

## References

- [Official Docs]({url})
- [GitHub]({url})
```
