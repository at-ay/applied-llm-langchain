"""Slide 42 · A retriever does the search in one call

    python examples/14_rag_retriever.py
"""

from langchain.embeddings import init_embeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Indexing (slide 39)
docs = PyPDFLoader("data/card_fees_policy.pdf").load()
chunks = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100).split_documents(docs)
store = InMemoryVectorStore.from_documents(chunks, init_embeddings("ollama:nomic-embed-text"))

retriever = store.as_retriever(search_kwargs={"k": 3})
docs = retriever.invoke("What is the fee for a late credit card payment?")
for d in docs:
    print(d.metadata["page"], d.page_content[:60].replace("\n", " "))
