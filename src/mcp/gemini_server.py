"""MCP Server for Gemini CLI integration.

This server provides tools for Cursor Agent to consult Gemini CLI
for research, codebase analysis, and multimodal processing.
"""

import subprocess
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

server = Server("gemini-mcp")


def run_gemini(prompt: str, include_codebase: bool = False) -> str:
    """Execute Gemini CLI with the given prompt."""
    cmd = ["gemini", "-p", prompt]

    if include_codebase:
        cmd.extend(["--include-directories", "."])

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
        return "Error: Gemini CLI timed out after 5 minutes"
    except FileNotFoundError:
        return "Error: Gemini CLI not found. Please install it first."


@server.list_tools()
async def list_tools() -> list[Tool]:
    """List available Gemini tools."""
    return [
        Tool(
            name="gemini_research",
            description=(
                "Research using Gemini with Google Search grounding. "
                "Use for: library comparison, best practices, documentation lookup, "
                "latest information, breaking changes."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "prompt": {
                        "type": "string",
                        "description": "The research question (in English)",
                    },
                },
                "required": ["prompt"],
            },
        ),
        Tool(
            name="gemini_analyze",
            description=(
                "Analyze codebase with Gemini's 1M token context. "
                "Includes all files in current directory. "
                "Use for: architecture understanding, finding patterns, "
                "repository-wide analysis."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "prompt": {
                        "type": "string",
                        "description": "The analysis question (in English)",
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

    if name == "gemini_research":
        result = run_gemini(prompt, include_codebase=False)
    elif name == "gemini_analyze":
        result = run_gemini(prompt, include_codebase=True)
    else:
        result = f"Unknown tool: {name}"

    return [TextContent(type="text", text=result)]


def main() -> None:
    """Run the MCP server."""
    import asyncio

    asyncio.run(stdio_server(server))


if __name__ == "__main__":
    main()
