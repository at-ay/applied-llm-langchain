"""Slide 41 · A question runs through four steps in code

The indexing from 12_rag_indexing.py, then the question path unrolled.

    python examples/13_rag_query.py
"""

from langchain.chat_models import init_chat_model
from langchain.embeddings import init_embeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Indexing (slide 39)
docs = PyPDFLoader("data/card_fees_policy.pdf").load()
chunks = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100).split_documents(docs)
embeddings = init_embeddings("ollama:nomic-embed-text")
store = InMemoryVectorStore.from_documents(chunks, embeddings)
model = init_chat_model("ollama:llama3.2:3b")

# Per question
question = "What is the fee for a late credit card payment?"
q_vector = embeddings.embed_query(question)                 # 1 · embed
docs = store.similarity_search_by_vector(q_vector, k=3)     # 2 · search
context = "\n\n".join(d.page_content for d in docs)
messages = [                                                # 3 · build messages
    {"role": "system", "content": "Answer using only the bank policies provided. "
                                  "If they don't contain the answer, say so."},
    {"role": "user", "content": f"Policies:\n{context}\n\nQuestion: {question}"},
]
answer = model.invoke(messages)                             # 4 · answer
print(answer.content)
