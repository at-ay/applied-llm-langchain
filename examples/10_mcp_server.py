"""Slide 35 · Write a server (Python, FastMCP)

A bank MCP server with one tool, served at http://localhost:8000/mcp.
Start it in one terminal, then run 11_mcp_client.py in another. Stop it with Ctrl+C.
When a client disconnects, the server may print a ClosedResourceError traceback:
that's noise from the mcp library, and the requests themselves succeeded.

    python examples/10_mcp_server.py
"""

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("bank")


@mcp.tool()
def get_transactions(account_id: str, days: int) -> str:
    """Return the account's transactions from the last N days."""
    return "28 Oct, Coffee Co, 49.90\n28 Oct, Coffee Co, 49.90\n27 Oct, Grocery Mart, 23.15"


mcp.run(transport="streamable-http")
