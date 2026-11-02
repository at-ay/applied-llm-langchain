"""Slide 7 · A chat assistant is a loop

Type a message, get a reply; type "quit" to stop.

    python examples/02_chat_loop.py
"""

from langchain.chat_models import init_chat_model

model = init_chat_model("ollama:llama3.2:1b")

messages = [{"role": "system", "content": "You are a helpful assistant."}]

for turn in range(10):  # up to 10 turns
    user_input = input("You: ")
    if user_input == "quit":
        break
    messages.append({"role": "user", "content": user_input})
    reply = model.invoke(messages)
    messages.append(reply)
    print("Assistant:", reply.content)
