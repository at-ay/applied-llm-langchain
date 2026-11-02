"""Lab · Q2 (i) · Urgency by prompting

    uv run python lab/q2a_prompting.py
"""

from collections import Counter

from langchain.chat_models import init_chat_model

model = init_chat_model("ollama:llama3.2:3b", temperature=0, num_predict=100)  # at most 100 tokens per reply
complaints = open("data/complaints.md").read().split("---")

counts = Counter()
for complaint in complaints:
    # YOUR TURN: ask the model to rate the complaint from 1 (low) to 5 (critical),
    #            answering with the number only. Turn reply.content into an int;
    #            if that fails (try/except ValueError), use "invalid".
    urgency = None

    if urgency is None:
        raise SystemExit("Fill in the YOUR TURN lines first.")
    if urgency not in [1, 2, 3, 4, 5]:
        urgency = "invalid"
    print(urgency, "|", complaint.strip()[:60])
    counts[urgency] += 1

print()
for urgency in [1, 2, 3, 4, 5, "invalid"]:
    print(f"urgency {urgency}: {counts[urgency]}")
