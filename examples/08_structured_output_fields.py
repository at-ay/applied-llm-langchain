"""Slides 15-18 · Descriptions and limits guide the model; the format is enforced in three places

Prints the JSON schema the model receives, then classifies a complaint with a system prompt.

    python examples/08_structured_output_fields.py
"""

import json
from typing import Literal

from langchain.chat_models import init_chat_model
from pydantic import BaseModel, Field


class Complaint(BaseModel):
    """A customer complaint received by the bank."""
    product: Literal["credit card", "loan", "account", "mobile app", "other"] = Field(
        description="Banking product the complaint is about")
    urgency: int = Field(ge=1, le=5,
        description="How urgent: 1 = low, 5 = critical")


print(json.dumps(Complaint.model_json_schema(), indent=2))  # what the model sees

model = init_chat_model("ollama:llama3.2:1b")
structured = model.with_structured_output(Complaint)

complaint = "Someone I don't know used my card to buy a TV online."
result = structured.invoke([
    {"role": "system", "content": "Classify bank complaints. Fraud is always urgency 5."},
    {"role": "user", "content": complaint},
])
print(result)
