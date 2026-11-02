"""Slide 9 · stream() delivers the reply piece by piece

The same question twice: invoke() waits for the whole reply, stream() prints it as it arrives.

    python examples/04_stream.py
"""

from langchain.chat_models import init_chat_model

model = init_chat_model("ollama:llama3.2:1b")
question = "How do I dispute a card charge? Answer in two sentences."

reply = model.invoke(question)
print(reply.content)
print()

for chunk in model.stream(question):
    print(chunk.content, end="", flush=True)
print()
