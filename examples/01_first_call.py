"""Slide 5 · A first LangChain program is three lines

The slide uses "anthropic:claude-sonnet-4-6". Here the model is llama3.2:1b
in Ollama, so no API key is needed.

    python examples/01_first_call.py
"""

from langchain.chat_models import init_chat_model

model = init_chat_model("ollama:llama3.2:1b")
print(model.invoke("Hello!").content)
