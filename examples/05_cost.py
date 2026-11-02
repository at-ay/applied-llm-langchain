"""Slide 10 · Cost is counted in tokens, per call

The slide's pseudocode as a working loop, then the get_usage_metadata_callback() shortcut.
Ollama is free; the prices below are made-up examples, to show the arithmetic.

    python examples/05_cost.py
"""

from langchain.chat_models import init_chat_model
from langchain_core.callbacks import get_usage_metadata_callback

PRICE_IN = 3.00 / 1_000_000    # dollars per input token (example)
PRICE_OUT = 15.00 / 1_000_000  # dollars per output token (example)

model = init_chat_model("ollama:llama3.2:1b")
messages = [{"role": "system", "content": "You are a bank's customer assistant. Be brief."}]
questions = ["What is a minimum payment?", "What if I pay less?", "How can I avoid that?"]

total_in = total_out = 0
for question in questions:
    messages.append({"role": "user", "content": question})
    reply = model.invoke(messages)
    messages.append(reply)
    total_in += reply.usage_metadata["input_tokens"]
    total_out += reply.usage_metadata["output_tokens"]
    print(reply.usage_metadata)

cost = total_in * PRICE_IN + total_out * PRICE_OUT
print(f"input {total_in}, output {total_out}, cost ${cost:.6f}")

# Shortcut: collects the totals for every call made inside the with block
with get_usage_metadata_callback() as cb:
    model.invoke("What is a minimum payment?")
    model.invoke("What is a late fee?")
print(cb.usage_metadata)
