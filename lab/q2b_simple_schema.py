"""Lab · Q2 (ii) · Urgency with a simple schema (slide 14)

    uv run python lab/q2b_simple_schema.py
"""

from collections import Counter

from langchain.chat_models import init_chat_model
from pydantic import BaseModel

# YOUR TURN: a Complaint class with two fields, product: str and urgency: int


model = init_chat_model("ollama:llama3.2:3b", temperature=0, num_predict=100)  # at most 100 tokens per reply
# YOUR TURN: structured = a version of the model that answers with a Complaint
complaints = open("data/complaints.md").read().split("---")

counts = Counter()
for complaint in complaints:
    # YOUR TURN: send only the complaint text to structured and take the urgency field.
    #            If invoke raises an exception (try/except Exception), use "invalid".
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
