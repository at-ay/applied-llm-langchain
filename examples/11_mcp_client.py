"""Slide 35 · Use MCP servers from LangChain

Needs the server from 10_mcp_server.py running in another terminal.
The slide's code uses await, so here it sits inside an async function.

    python examples/11_mcp_client.py
"""

import asyncio

from langchain.agents import create_agent
from langchain_mcp_adapters.client import MultiServerMCPClient

async def main():
    client = MultiServerMCPClient({"bank": {"transport": "http", "url": "http://localhost:8000/mcp"}})
    tools = await client.get_tools()  # tools/list → LangChain tools
    print("tools:", [t.name for t in tools])

    agent = create_agent("ollama:llama3.2:3b", tools)
    question = "Was I charged twice last week? My account is ACC-123."
    result = await agent.ainvoke({"messages": [{"role": "user", "content": question}]})
    print(result["messages"][-1].content)


asyncio.run(main())
