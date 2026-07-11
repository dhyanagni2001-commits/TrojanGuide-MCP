"""
server.py

TrojanGuide MCP — entrypoint.

This registers 5 tools with FastMCP and starts the server over stdio,
which is how Claude Desktop (or any other MCP client) talks to it.
Run directly: python server.py
"""

from mcp.server.fastmcp import FastMCP

from tools.building import find_building
from tools.library import find_library
from tools.food import find_food
from tools.services import find_student_service
from tools.search import search_campus

# The name shows up in Claude Desktop's tool list / server picker.
mcp = FastMCP("TrojanGuide")

# Register each tool. The decorator wraps the plain Python function
# so FastMCP can expose it to the LLM, using the function's docstring
# and type hints to generate the tool's schema automatically.
mcp.tool()(find_building)
mcp.tool()(find_library)
mcp.tool()(find_food)
mcp.tool()(find_student_service)
mcp.tool()(search_campus)

if __name__ == "__main__":
    # stdio transport: reads/writes JSON-RPC over stdin/stdout.
    # This is what Claude Desktop expects for locally-run MCP servers.
    mcp.run(transport="stdio")