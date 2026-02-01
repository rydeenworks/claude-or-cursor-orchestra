---
name: gemini
description: |
  Research with Gemini CLI for library comparison, documentation lookup,
  codebase analysis, and multimodal processing (PDF/video/audio).
  Triggers: "research", "investigate", "調べて", "リサーチ", "PDF", "動画"
---

# Gemini CLI Research

**Gemini CLI でリサーチ・コードベース分析・マルチモーダル処理を行う。**

## Task

$ARGUMENTS について Gemini でリサーチしてください。

## How to Consult

Bash で直接 Gemini CLI を呼び出す：

```bash
# リサーチ
gemini -p "{question}" 2>/dev/null

# コードベース分析
gemini -p "{question}" --include-directories . 2>/dev/null

# マルチモーダル（PDF/動画/音声）
gemini -p "{prompt}" < /path/to/file 2>/dev/null
```

## When to Use

| Situation | Use Gemini |
|-----------|------------|
| ライブラリ調査 | ✓ |
| ベストプラクティス調査 | ✓ |
| コードベース全体理解 | ✓ |
| PDF/動画/音声分析 | ✓ |
| 最新ドキュメント確認 | ✓ |

## Language Protocol

1. Ask Gemini in **English**
2. Receive response in **English**
3. Report to user in **Japanese**

## Output

1. Gemini の回答を `.claude/docs/research/{topic}.md` に保存
2. 要点を日本語でユーザーに報告
