# LangChain lab sheet

Write each answer in this `lab/` folder (some questions give you a starter file) and run it from the
`applied-llm-langchain` folder, as with the examples:

```bash
uv run python lab/q1_token_chatbot.py
```

Use `"ollama:llama3.2:1b"` as the model unless a question says otherwise.

**Handing in:** download [lab-sheet.docx](lab-sheet.docx) (the same questions, with a box for every
answer). Fill in each box with your code, the pasted terminal output, a screenshot and your answers,
then hand in the Word file.

---

## Q1 · A chatbot that counts its tokens

Open `lab/q1_token_chatbot.py` and fill in the `YOUR TURN` part: a chatbot that runs in an
infinite loop and, after every assistant reply, shows how many tokens the conversation has used so far.

**Requirements**

1. The loop never stops on its own: it keeps asking `You: ` until the user types `quit`.
2. The bot remembers the conversation. Ask "What is my name?" after telling it your name to check.
3. After every reply, print the tokens of that turn (input and output) and the
   **cumulative** totals since the start: input, output and both together.

**Example run** (your replies and numbers will differ)

```
You: Hi, my name is Ada.
Assistant: Hello Ada, how can I assist you today?
  [this turn: 41 in, 11 out | total: 41 in, 11 out, 52 tokens]
You: What is a credit card late fee?
Assistant: A credit card late fee is a charge imposed by a credit card issuer ...
  [this turn: 69 in, 68 out | total: 110 in, 79 out, 189 tokens]
You: What is my name?
Assistant: Your name is Ada.
  [this turn: 151 in, 6 out | total: 261 in, 85 out, 346 tokens]
You: quit
```

**Hints**

- Start from `examples/02_chat_loop.py` (slide 7). It stops after 10 turns; yours must not.
- Every reply has a `usage_metadata` field (slide 8); `examples/05_cost.py` (slide 10) adds it up.

**Think about**

- The third question is the shortest, so why does it have the most input tokens?
- If the chat goes on for 50 turns, what happens to the input tokens of each turn, and to the total?

**Bonus · switch to a smaller model when the chat gets long**

Copy your Q1 answer to `lab/q1_bonus_switch_model.py`. Start with `"ollama:llama3.2:1b"`. When the cumulative
total passes a threshold (say 300 tokens), switch to the smaller `"ollama:qwen2.5:0.5b"` for the
rest of the chat. Tell the user when the switch happens, and show which model answered on every
token line. Keep the conversation history: the new model gets the same `messages` list.

First, download the model once:

```bash
ollama pull qwen2.5:0.5b
```

Example run:

```
You: Hi, my name is Ada.
Assistant: Hello Ada, how can I help you today?
  [ollama:llama3.2:1b | this turn: 41 in, 11 out | total: 41 in, 11 out, 52 tokens]
You: What is a credit card late fee?
Assistant: A credit card late fee is a charge imposed by some credit card issuers ...
  [ollama:llama3.2:1b | this turn: 69 in, 64 out | total: 110 in, 75 out, 185 tokens]
You: How can I avoid it?
Assistant: To avoid late fees, make sure to: ...
  [ollama:llama3.2:1b | this turn: 148 in, 107 out | total: 258 in, 182 out, 440 tokens]
  >>> 440 tokens used, over the limit of 300: switching to ollama:qwen2.5:0.5b. The conversation so far is kept.
You: What is my name?
Assistant: Your name is Ada.
  [ollama:qwen2.5:0.5b | this turn: 259 in, 6 out | total: 517 in, 188 out, 705 tokens]
You: quit
```

Think about: does the smaller model still know your name? Why can you swap the model in the
middle of a conversation at all?

---

## Q2 · Counting complaints by urgency, three ways

`data/complaints.md` holds 18 customer complaints, separated by lines with only `---`.
The bank wants to know how many complaints there are for each urgency, using this scale:

| Urgency | Meaning |
|---|---|
| 5 | Money is being lost or is at risk right now (fraud, a stolen card, an unknown payment) |
| 4 | The customer can't get to money they need soon |
| 3 | A wrong charge or a mistake that needs fixing, but no harm yet |
| 2 | A service problem or an inconvenience |
| 1 | Feedback or a suggestion, no money involved |

Read through the file first. Some complaints are tricky on purpose: an angry customer with a
small problem, a polite one with a serious problem, and numbers in the text that aren't urgencies.

There is one file per method, and they all look alike: the loop reads the complaints, counts
the urgencies and prints the totals. You only fill in the lines marked `YOUR TURN`, which set
`urgency` to an `int` or to `"invalid"` when the answer can't be used. Every answer outside 1–5
is counted as `invalid`. Q2 uses `ollama:llama3.2:3b`, and each file takes about 20 seconds to run.

**(i) Prompting:** `lab/q2a_prompting.py`. Ask the model to rate the complaint from 1 to 5
and to answer with the number only. Turn `reply.content` into an `int` yourself; if that
fails, use `"invalid"`.

**(ii) A simple schema:** `lab/q2b_simple_schema.py`. Write a pydantic class with just
`product: str` and `urgency: int`, as on slide 14 (`examples/07_structured_output.py`).
Send only the complaint text and take the `urgency` field.

**(iii) A schema with proper fields and definitions:** `lab/q2c_detailed_schema.py`. As on
slides 15–18 (`examples/08_structured_output_fields.py`):

- make `product` a `Literal` of the allowed products;
- limit `urgency` to 1–5 with `Field(ge=..., le=...)` and give it a `description`;
- send the scale (`SCALE` in the file) in a system prompt, and tell the model to judge by
  the risk to the money, not by the customer's tone.

In (ii) and (iii), `invoke` raises an exception when the reply doesn't fit the schema: catch
it and use `"invalid"`.

**Expected counts**

| Urgency | 1 | 2 | 3 | 4 | 5 | invalid |
|---|---|---|---|---|---|---|
| Complaints | 4 | 3 | 4 | 3 | 4 | 0 |

Your numbers won't match these exactly; the point is to compare the three methods.

**Hints**

- `model.with_structured_output(Complaint)` returns a version of the model whose `invoke`
  returns a `Complaint` object.
- A system prompt goes in a messages list: `[{"role": "system", ...}, {"role": "user", ...}]`.

**Think about**

- What does (i) do with an answer like `"Urgency: 4"`? What does (ii) return that isn't a valid urgency?
- Look at the line printed for each complaint. Which complaints does each method get wrong?
- (ii) and (iii) both return an `int`. Why does (iii) give so much better answers?
- Structured output guarantees the **format** of the answer. Does it guarantee the answer is **right**?

**Bonus for (i) · does the system prompt make a difference?**

Copy `lab/q2a_prompting.py` to `lab/q2a_bonus_prompts.py` and run method (i) with several
system prompts. Try at least these three, and add your own ideas (for example, two or three
example complaints with their correct urgency):

1. **bare:** your prompt from (i), with only "from 1 (low) to 5 (critical)";
2. **scale:** the same prompt plus the urgency scale (copy `SCALE` from `lab/q2c_detailed_schema.py`);
3. **scale + tone:** the scale plus "judge by the risk to the customer's money, not by how angry
   or polite the customer sounds".

Print the counts of every prompt side by side, next to the expected ones. Example output:

```
urgency    expected        bare       scale  scale+tone
1                 4           0           1           1
2                 3           5           5           3
3                 4           3           6           8
4                 3           7           1           1
5                 4           3           5           5
invalid           0           0           0           0
```

Think about: which complaints change urgency when you change the prompt? Compare your best prompt
with (iii): how much of (iii)'s improvement came from the schema, and how much from the prompt?
