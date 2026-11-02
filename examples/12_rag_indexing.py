"""Slide 39 · Indexing turns documents into searchable chunks

The slide uses OpenAI's embedding model; here it is nomic-embed-text in Ollama
(768 numbers per vector instead of 1,536).

    python examples/12_rag_indexing.py
"""

from langchain.embeddings import init_embeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_text_splitters import RecursiveCharacterTextSplitter

docs = PyPDFLoader("data/card_fees_policy.pdf").load()               # 1 · load
splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)
chunks = splitter.split_documents(docs)                              # 2 · split
embeddings = init_embeddings("ollama:nomic-embed-text")              # 3 · embed
store = InMemoryVectorStore.from_documents(chunks, embeddings)       # 4 · store

print(len(docs), "pages,", len(chunks), "chunks")
print(chunks[0].metadata["page"], chunks[0].page_content[:80])
print(len(embeddings.embed_query("late fee")), "numbers per vector")
