# Codex CLI Consultation

**Codex CLI (gpt-5.2-codex) に設計・デバッグ・分析を相談する。**

## Task

$ARGUMENTS について Codex に相談してください。

## How to Consult

Bash で直接 Codex CLI を呼び出す：

```bash
# 設計・分析（read-only）
codex exec --model gpt-5.2-codex --sandbox read-only --full-auto "
{question}
" 2>/dev/null

# 実装・修正（workspace-write）
codex exec --model gpt-5.2-codex --sandbox workspace-write --full-auto "
{task}
" 2>/dev/null
```

## When to Use

| Situation | Use Codex |
|-----------|-----------|
| 設計判断 | ✓ |
| デバッグ | ✓ |
| トレードオフ分析 | ✓ |
| コードレビュー | ✓ |
| リファクタリング | ✓ |

## Language Protocol

1. Ask Codex in **English**
2. Receive response in **English**
3. Report to user in **Japanese**

## Output

Codex の回答を要約し、日本語でユーザーに報告してください。
