"""Slide 12 · The | operator chains steps together

    python examples/06_chain.py
"""

from langchain.chat_models import init_chat_model
from langchain_core.output_parsers import StrOutputParser


def make_messages(complaint):
    return [
        {"role": "system", "content": "You are a bank's customer service assistant."},
        {"role": "user", "content": f"Write a short, polite reply to this complaint:\n{complaint}"},
    ]


model = init_chat_model("ollama:llama3.2:1b")
chain = make_messages | model | StrOutputParser()
print(chain.invoke("My credit card was charged twice for the same purchase."))
