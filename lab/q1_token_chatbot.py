"""Lab · Q1 · A chatbot that counts its tokens

Chat in an endless loop; type "quit" to stop. After every reply, print the tokens
of that turn and the running totals.

    uv run python lab/q1_token_chatbot.py
"""

from langchain.chat_models import init_chat_model

model = init_chat_model("ollama:llama3.2:1b")

messages = [{"role": "system", "content": "You are a helpful assistant. Be brief."}]
total_in = total_out = 0

# YOUR TURN: an endless loop (examples/02_chat_loop.py stops after 10 turns; yours must not).
#            In each turn:
#              - ask "You: " and stop when the user types quit
#              - add the user's message, call the model with the whole list, add the reply, print it
#              - add this turn's input and output tokens (reply.usage_metadata) to total_in and total_out
#              - print this turn's tokens and the totals, for example:
#                  [this turn: 69 in, 68 out | total: 110 in, 79 out, 189 tokens]
#            Then delete the line below.

raise SystemExit("Fill in the YOUR TURN lines first.")
