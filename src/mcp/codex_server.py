"""MCP Server for Codex CLI integration.

This server provides tools for Cursor Agent to consult Codex CLI
for design decisions, debugging, and implementation tasks.
"""

import subprocess
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

CODEX_MODEL = "gpt-5.2-codex"

server = Server("codex-mcp")


def run_codex(prompt: str, sandbox: str = "read-only") -> str:
    """Execute Codex CLI with the given prompt."""
    cmd = [
        "codex",
        "exec",
        "--model",
        CODEX_MODEL,
        "--sandbox",
        sandbox,
        "--full-auto",
        prompt,
    ]
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=300,
        )
        if result.returncode != 0:
            return f"Error: {result.stderr}"
        return result.stdout
    except subprocess.TimeoutExpired:
        return "Error: Codex CLI timed out after 5 minutes"
    except FileNotFoundError:
        return "Error: Codex CLI not found. Please install it first."


@server.list_tools()
async def list_tools() -> list[Tool]:
    """List available Codex tools."""
    return [
        Tool(
            name="codex_consult",
            description=(
                "Consult Codex for design decisions, debugging analysis, "
                "and trade-off evaluation. Read-only mode - does not modify files. "
                "Use for: design questions, error analysis, comparing approaches."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "prompt": {
                        "type": "string",
                        "description": "The question or task for Codex (in English)",
                    },
                },
                "required": ["prompt"],
            },
        ),
        Tool(
            name="codex_implement",
            description=(
                "Ask Codex to implement, fix, or refactor code. "
                "Can modify files in the workspace. "
                "Use for: implementing features, fixing bugs, refactoring."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "prompt": {
                        "type": "string",
                        "description": "The implementation task for Codex (in English)",
                    },
                },
                "required": ["prompt"],
            },
        ),
    ]


@server.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    """Handle tool calls."""
    prompt = arguments.get("prompt", "")

    if name == "codex_consult":
        result = run_codex(prompt, sandbox="read-only")
    elif name == "codex_implement":
        result = run_codex(prompt, sandbox="workspace-write")
    else:
        result = f"Unknown tool: {name}"

    return [TextContent(type="text", text=result)]


def main() -> None:
    """Run the MCP server."""
    import asyncio

    asyncio.run(stdio_server(server))


if __name__ == "__main__":
    main()
