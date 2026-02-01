# Test-Driven Development

**$ARGUMENTS を TDD (Red-Green-Refactor) で実装する。**

## TDD Cycle

```
Repeat: Red → Green → Refactor

1. Red:    失敗するテストを書く
2. Green:  テストを通す最小限のコードを書く
3. Refactor: コードを整理（テストは通ったまま）
```

## Implementation Steps

### Phase 1: Test Design

1. **要件確認**
   - 入力は何か
   - 出力は何か
   - エッジケースは何か

2. **テストケース一覧**
   ```
   - [ ] Happy path: 基本機能
   - [ ] Happy path: 境界値
   - [ ] Error case: 無効な入力
   - [ ] Error case: エラー処理
   ```

### Phase 2: Red-Green-Refactor

#### Step 1: 最初のテストを書く (Red)

```python
# tests/test_{module}.py
def test_{function}_basic():
    """Test the most basic case"""
    result = function(input)
    assert result == expected
```

テストを実行して**失敗を確認**：
```bash
uv run pytest tests/test_{module}.py -v
```

#### Step 2: 実装 (Green)

テストを通す**最小限**のコードを書く：
- 完璧を目指さない
- ハードコードでもOK
- とにかくテストを通す

テストを実行して**成功を確認**：
```bash
uv run pytest tests/test_{module}.py -v
```

#### Step 3: リファクタリング (Refactor)

テストが通ったまま改善：
- 重複を除去
- 命名を改善
- 構造を整理

```bash
uv run pytest tests/test_{module}.py -v  # まだ通ることを確認
```

#### Step 4: 次のテスト

一覧から次のテストケースで Step 1 に戻る。

### Phase 3: Completion Check

```bash
# 全テスト実行
uv run pytest -v

# カバレッジ確認（目標80%以上）
uv run pytest --cov={module} --cov-report=term-missing
```

## Report Format

```markdown
## TDD Complete: {Feature Name}

### Test Cases
- [x] {test1}: {description}
- [x] {test2}: {description}
...

### Coverage
{Coverage report}

### Implementation Files
- `src/{module}.py`: {description}
- `tests/test_{module}.py`: {N} tests
```

## Notes

- テストを**先に**書く（後ではない）
- 各サイクルを**小さく**保つ
- テストが通ってから**リファクタ**
- 完璧より**動くコード**を優先
