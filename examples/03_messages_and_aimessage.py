"""Slides 6 and 8 · The messages list is the context; invoke() returns an AIMessage

Sends the conversation from slide 6 and prints the fields of the reply.

    python examples/03_messages_and_aimessage.py
"""

from langchain.chat_models import init_chat_model

model = init_chat_model("ollama:llama3.2:1b")

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "How do I dispute a card charge?"},
    {"role": "assistant", "content": "Open the app, pick the charge, tap Dispute."},
    {"role": "user", "content": "How long does it take?"},
    {"role": "assistant", "content": "Usually up to 10 working days."},
    {"role": "user", "content": "Thanks!"},
]

reply = model.invoke(messages)
print(type(reply).__name__)
print(reply.content)                         # a field: use a dot
print(reply.usage_metadata["input_tokens"])  # a key in a dict: use brackets
print(reply.usage_metadata)
print(reply.response_metadata)
print(reply.tool_calls)                      # empty: no tools here
