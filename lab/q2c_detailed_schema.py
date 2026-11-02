"""Lab · Q2 (iii) · Urgency with proper fields and definitions (slides 15-18)

    uv run python lab/q2c_detailed_schema.py
"""

from collections import Counter
from typing import Literal

from langchain.chat_models import init_chat_model
from pydantic import BaseModel, Field

SCALE = """Urgency scale:
5 = money is being lost or is at risk right now (fraud, a stolen card, an unknown payment)
4 = the customer can't get to money they need soon
3 = a wrong charge or a mistake that needs fixing, but no harm yet
2 = a service problem or an inconvenience
1 = feedback or a suggestion, no money involved"""

# YOUR TURN: a Complaint class with
#   - product: a Literal of the allowed products, with a description
#   - urgency: an int limited to 1-5 with Field(ge=..., le=...), with a description


model = init_chat_model("ollama:llama3.2:3b", temperature=0, num_predict=100)  # at most 100 tokens per reply
# YOUR TURN: structured = a version of the model that answers with a Complaint
complaints = open("data/complaints.md").read().split("---")

counts = Counter()
for complaint in complaints:
    # YOUR TURN: send a system message (the task, SCALE, and "judge by the risk to the money,
    #            not by the customer's tone") and the complaint as the user message.
    #            Take the urgency field; if invoke raises an exception, use "invalid".
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
