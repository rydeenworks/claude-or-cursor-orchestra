# Simplify Code

**$ARGUMENTS をシンプル化・リファクタリングする。**

## Simplification Principles

1. **Single Responsibility** - 1関数 = 1つのこと
2. **Short Functions** - 目標20行以下
3. **Shallow Nesting** - 早期リターン、深さ≤2
4. **Clear Naming** - コメント不要なほど明確に
5. **Type Hints Required** - 全関数に型ヒント

## Steps

### 1. Analyze Target Code

- ファイルを読んで現在の構造を理解
- 複雑さのホットスポットを特定（深いネスト、長い関数）
- シンプル化する関数/クラスをリスト

### 2. Check Library Constraints

- 対象コードで使用しているライブラリを特定
- `.claude/docs/libraries/` で制約を確認
- 不明な点は Web 検索

### 3. Plan Refactoring

各複雑さの問題に対して：
- 何を変更するか
- なぜ可読性が向上するか
- ライブラリ使用を壊さないか確認

### 4. Execute Refactoring

以下のパターンに従って変更を適用：

**Early Return:**
```python
# Before
def process(value):
    if value is not None:
        if value > 0:
            return do_something(value)
    return None

# After
def process(value):
    if value is None:
        return None
    if value <= 0:
        return None
    return do_something(value)
```

**Extract Function:**
```python
# Before
def main():
    # 50 lines of mixed concerns
    ...

# After
def main():
    data = load_data()
    result = process_data(data)
    save_result(result)
```

### 5. Verify with Tests

```bash
uv run pytest -v
```

## Optional: Codex Review

リファクタリング後に Codex でレビュー：

```bash
codex exec --model gpt-5.2-codex --sandbox read-only --full-auto "
Review this refactored code:
{code}

Check for:
1. Readability improvements
2. Potential issues
3. Further simplification opportunities
" 2>/dev/null
```

## Notes

- ライブラリの機能/制約を常に保持
- 不明点は Web 検索
- 動作を変えない（リファクタリングのみ）
- 重要な変更後はテストを実行
