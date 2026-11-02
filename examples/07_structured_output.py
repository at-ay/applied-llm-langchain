"""Slide 14 · A schema class and one method do the work

    python examples/07_structured_output.py
"""

from langchain.chat_models import init_chat_model
from pydantic import BaseModel


class Complaint(BaseModel):
    product: str
    urgency: int


model = init_chat_model("ollama:llama3.2:1b")
structured = model.with_structured_output(Complaint)

text = ("My credit card was charged twice for the same purchase. "
        "I need the money back before my rent is due tomorrow!")
result = structured.invoke(text)
print(result)
print(result.urgency)  # a number your code can use
