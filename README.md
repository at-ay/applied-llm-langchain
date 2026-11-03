# Applied LLM Course · LangChain

The LangChain module of the Applied LLM Course:

- **`examples/`:** the code from the LangChain slides, as small programs you can run. There is
  one file per slide (or group of slides), numbered in the order of the deck.
- **`lab/`:** the lab sheet and its starter files. See [lab/README.md](lab/README.md).

**The code is the code on the slides, with one main difference: the model.** The slides use
Anthropic and OpenAI models (for example `"anthropic:claude-sonnet-4-6"`), which need an API key
and cost money. Here every example uses a free Llama model running on your own computer
through [Ollama](https://ollama.com):

| On the slides | Here | Used by |
|---|---|---|
| Anthropic chat model | `ollama:llama3.2:1b` | examples 01–08 |
| Anthropic chat model, with tools | `ollama:llama3.2:3b` (tool calling needs more than 1B) | examples 09, 11, 13, 15 |
| OpenAI embedding model | `ollama:nomic-embed-text` (768 numbers per vector instead of 1,536) | examples 12–15 |

Only the model string changes; the LangChain code stays the same, which is the point of
`init_chat_model`. A few other small differences:

- The tools return made-up transactions instead of querying a bank's database.
- The RAG examples read `data/card_fees_policy.pdf`, a made-up bank policy.
- Some files print a little more than the slide (for example the fields of a reply), so you can see what happened.
- The slide on server tools (web search) has no example: those tools run on the provider's side.
- Small local models make mistakes a large model wouldn't, such as a wrong urgency or a misread
  transaction list. That is worth looking at; it isn't a bug in the code.

## Files

```
applied-llm-langchain/
├── README.md
├── pyproject.toml        dependencies, for uv
├── uv.lock               exact versions, for uv
├── data/
│   ├── card_fees_policy.pdf   for the RAG examples
│   └── complaints.md          for lab Q2
├── examples/
│   └── 01_first_call.py ... 15_rag_chain.py
└── lab/
    ├── README.md              the lab sheet
    ├── lab-sheet.docx         the lab sheet with answer boxes, to hand in
    └── q2a_prompting.py ...   starter files
```

| File | Slide |
|---|---|
| `01_first_call.py` | A first LangChain program is three lines |
| `02_chat_loop.py` | A chat assistant is a loop |
| `03_messages_and_aimessage.py` | The messages list is the context; invoke() returns an AIMessage |
| `04_stream.py` | stream() delivers the reply piece by piece |
| `05_cost.py` | Cost is counted in tokens, per call |
| `06_chain.py` | The \| operator chains steps together |
| `07_structured_output.py` | A schema class and one method do the work |
| `08_structured_output_fields.py` | Descriptions and limits guide the model; the format is enforced in three places |
| `09_create_agent.py` | create_agent runs the tool loop for you |
| `10_mcp_server.py` | MCP: write a server |
| `11_mcp_client.py` | MCP: use the server from LangChain |
| `12_rag_indexing.py` | Indexing turns documents into searchable chunks |
| `13_rag_query.py` | A question runs through four steps in code |
| `14_rag_retriever.py` | A retriever does the search in one call |
| `15_rag_chain.py` | Two-step RAG is a short chain |

## Installation

You need Python 3.11 or newer. Check with:

```bash
python --version
```

On macOS and Linux the command may be `python3` instead of `python`.

### Step 1 · Install Ollama

Ollama runs the Llama models on your computer.

- **macOS:** download the app from https://ollama.com/download and open it, or install it with Homebrew:

  ```bash
  brew install ollama
  ```

- **Linux:**

  ```bash
  curl -fsSL https://ollama.com/install.sh | sh
  ```

- **Windows:** download and run the installer from https://ollama.com/download.

Check that it is running (the app starts the server; on Linux it runs as a service):

```bash
ollama --version
```

If commands below say they can't connect to Ollama, start the server yourself in a separate
terminal and leave it open:

```bash
ollama serve
```

### Step 2 · Download the three models

About 3.5 GB in total; this is a one-time download.

```bash
ollama pull llama3.2:1b
```

```bash
ollama pull llama3.2:3b
```

```bash
ollama pull nomic-embed-text
```

The lab's Q1 bonus also uses a smaller model (about 400 MB):

```bash
ollama pull qwen2.5:0.5b
```

Check that the models are listed:

```bash
ollama list
```

### Step 3 · Get this repository

With git:

```bash
git clone https://github.com/at-ay/applied-llm-langchain.git
```

Without git: on the GitHub page, click **Code → Download ZIP** and unzip it.

Then open a terminal **in the `applied-llm-langchain` folder**. Every command from here on
runs from this folder, because the examples and the lab look for files in `data/` relative to it.

```bash
cd applied-llm-langchain
```

### Step 4 · Install the Python packages with uv

[uv](https://docs.astral.sh/uv/) creates the virtual environment and installs the exact
versions in `uv.lock` in one command.

Install uv (once per computer). On macOS and Linux:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

On Windows (PowerShell):

```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Close and reopen the terminal, then check:

```bash
uv --version
```

Install the packages (this creates a `.venv` folder here):

```bash
uv sync
```

You don't need to activate anything: `uv run python ...` always uses this folder's `.venv`,
even if another environment (such as Anaconda's `base`) is active.

### Step 5 · Check that everything works

```bash
uv run python examples/01_first_call.py
```

You should see a short greeting from the model, such as `Hello! How can I assist you today?`

## Running the examples

All commands run from the `applied-llm-langchain` folder.

### Talking to a model (slides 5–10)

```bash
uv run python examples/01_first_call.py
```

```bash
uv run python examples/02_chat_loop.py
```

`02_chat_loop.py` is interactive: type a message and press Enter; type `quit` to stop.

```bash
uv run python examples/03_messages_and_aimessage.py
```

```bash
uv run python examples/04_stream.py
```

```bash
uv run python examples/05_cost.py
```

### Chains and structured output (slides 12–18)

```bash
uv run python examples/06_chain.py
```

```bash
uv run python examples/07_structured_output.py
```

```bash
uv run python examples/08_structured_output_fields.py
```

### Tools and agents (slide 28)

```bash
uv run python examples/09_create_agent.py
```

### MCP (slide 35): two terminals

Start the server in one terminal and leave it running:

```bash
uv run python examples/10_mcp_server.py
```

Then, in a **second** terminal (also in the `applied-llm-langchain` folder), run the client:

```bash
uv run python examples/11_mcp_client.py
```

The server window logs each request (`ListToolsRequest`, `CallToolRequest`). When the client
disconnects, the server may print an `anyio.ClosedResourceError` traceback: that is noise from
the `mcp` library and the requests themselves succeeded. Stop the server with Ctrl+C.

### RAG (slides 39–43)

```bash
uv run python examples/12_rag_indexing.py
```

```bash
uv run python examples/13_rag_query.py
```

```bash
uv run python examples/14_rag_retriever.py
```

```bash
uv run python examples/15_rag_chain.py
```

These print a `DeprecationWarning` saying that `langchain-community` "is being sunset". It comes
from `PyPDFLoader`, which still lives in that package. The code works; you can ignore the warning.

### All the non-interactive examples at once

On macOS and Linux (skips the chat loop and the MCP pair, which need you):

```bash
for f in examples/0[13-9]*.py examples/1[2-5]*.py; do echo "=== $f"; uv run python "$f"; done
```

## The lab

The questions are in [lab/README.md](lab/README.md). Write your answers in the `lab/` folder
and run them from this folder, like the examples:

```bash
uv run python lab/q2a_prompting.py
```

A starter file prints `Fill in the YOUR TURN lines first.` until you have written your part.

Hand in your answers in [lab/lab-sheet.docx](lab/lab-sheet.docx): the same questions, with a box
for every answer.

## Seeing what an agent did

`09_create_agent.py` and `11_mcp_client.py` print only the final answer. To see the whole
exchange (the question, the model's tool call with its arguments, the tool's result, the answer),
replace the last `print(...)` with:

```python
for m in result["messages"]:
    m.pretty_print()
```

## Common problems

| Message | Cause and fix |
|---|---|
| `can't open file '.../examples/examples/01_first_call.py'` | You are inside `examples/`. Go up one folder (`cd ..`) and run the command again. |
| `No such file or directory: 'data/card_fees_policy.pdf'` | Same cause: run from the `applied-llm-langchain` folder. |
| `ConnectError: All connection attempts failed` (from `ollama`) | Ollama isn't running. Open the Ollama app or run `ollama serve` in another terminal. |
| `ConnectError` from the MCP client | The MCP server isn't running. Start `10_mcp_server.py` in another terminal first. |
| `model "llama3.2:3b" not found` | Pull it: `ollama pull llama3.2:3b` (same for the other models). |
| `address already in use` (MCP server) | A server is already running on port 8000. Stop the old one with Ctrl+C. |
| `ModuleNotFoundError: No module named 'langchain'` | Use `uv run python`, not plain `python`, and run `uv sync` once first. |
