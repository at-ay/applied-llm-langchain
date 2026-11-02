"""Slide 28 · create_agent runs the tool loop for you

Uses llama3.2:3b in Ollama: tool calling needs a bigger model than 1B.
get_transactions returns made-up data instead of querying a database.

    python examples/09_create_agent.py
"""

from langchain.agents import create_agent
from langchain.tools import tool


@tool
def get_transactions(account_id: str, days: int) -> str:
    """Return the account's transactions from the last N days."""
    return "28 Oct, Coffee Co, 49.90\n28 Oct, Coffee Co, 49.90\n27 Oct, Grocery Mart, 23.15"


agent = create_agent("ollama:llama3.2:3b", tools=[get_transactions])

question = "Was I charged twice last week? My account is ACC-123."
result = agent.invoke({"messages": [{"role": "user", "content": question}]})
print(result["messages"][-1].content)

# To see the whole exchange (question, tool call, tool result, answer):
# for m in result["messages"]:
#     m.pretty_print()
