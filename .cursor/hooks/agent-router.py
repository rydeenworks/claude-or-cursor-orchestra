#!/usr/bin/env python3
"""
beforeSubmitPrompt hook: Route to appropriate agent based on user intent.

Analyzes user prompts and suggests the most appropriate agent
(Codex for design/debug, Gemini for research/multimodal).

Cursor hook I/O:
- Input: JSON via stdin with prompt content
- Output: JSON with additional_context or empty for no suggestion
"""

import json
import sys

# Triggers for Codex (design, debugging, deep reasoning)
CODEX_TRIGGERS = {
    "ja": [
        "設計", "どう設計", "アーキテクチャ",
        "なぜ動かない", "エラー", "バグ", "デバッグ",
        "どちらがいい", "比較して", "トレードオフ",
        "実装方法", "どう実装",
        "リファクタリング", "リファクタ",
        "レビュー", "見て",
        "考えて", "分析して", "深く",
    ],
    "en": [
        "design", "architecture", "architect",
        "debug", "error", "bug", "not working", "fails",
        "compare", "trade-off", "tradeoff", "which is better",
        "how to implement", "implementation",
        "refactor", "simplify",
        "review", "check this",
        "think", "analyze", "deeply",
    ],
}

# Triggers for Gemini (research, multimodal, large context)
GEMINI_TRIGGERS = {
    "ja": [
        "調べて", "リサーチ", "調査",
        "PDF", "動画", "音声", "画像",
        "コードベース全体", "リポジトリ全体",
        "最新", "ドキュメント",
        "ライブラリ", "パッケージ",
    ],
    "en": [
        "research", "investigate", "look up", "find out",
        "pdf", "video", "audio", "image",
        "entire codebase", "whole repository",
        "latest", "documentation", "docs",
        "library", "package", "framework",
    ],
}


def detect_agent(prompt: str) -> tuple[str | None, str]:
    """Detect which agent should handle this prompt."""
    prompt_lower = prompt.lower()

    # Check Codex triggers
    for triggers in CODEX_TRIGGERS.values():
        for trigger in triggers:
            if trigger in prompt_lower:
                return "codex", trigger

    # Check Gemini triggers
    for triggers in GEMINI_TRIGGERS.values():
        for trigger in triggers:
            if trigger in prompt_lower:
                return "gemini", trigger

    return None, ""


def main():
    try:
        data = json.load(sys.stdin)
        # Cursor uses "prompt" field in beforeSubmitPrompt
        prompt = data.get("prompt", data.get("message", ""))

        # Skip short prompts
        if len(prompt) < 10:
            print(json.dumps({}))
            sys.exit(0)

        agent, trigger = detect_agent(prompt)

        if agent == "codex":
            output = {
                "additional_context": (
                    f"[Agent Routing] Detected '{trigger}' - consider using "
                    "/codex-system for design decisions, debugging, or analysis. "
                    "Or call directly: `codex exec --model gpt-5.2-codex --sandbox read-only "
                    '--full-auto "{question}" 2>/dev/null`'
                )
            }
            print(json.dumps(output))

        elif agent == "gemini":
            output = {
                "additional_context": (
                    f"[Agent Routing] Detected '{trigger}' - consider using "
                    "/gemini-system for documentation, library research, or multimodal content. "
                    'Or call directly: `gemini -p "{question}" 2>/dev/null`'
                )
            }
            print(json.dumps(output))

        else:
            print(json.dumps({}))

        sys.exit(0)

    except Exception as e:
        print(f"Hook error: {e}", file=sys.stderr)
        print(json.dumps({}))
        sys.exit(0)


if __name__ == "__main__":
    main()
