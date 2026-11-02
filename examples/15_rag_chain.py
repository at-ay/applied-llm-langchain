"""Slide 43 · Two-step RAG is a short chain

    python examples/15_rag_chain.py
"""

from langchain.chat_models import init_chat_model
from langchain.embeddings import init_embeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Indexing (slide 39) and the retriever (slide 42)
docs = PyPDFLoader("data/card_fees_policy.pdf").load()
chunks = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100).split_documents(docs)
store = InMemoryVectorStore.from_documents(chunks, init_embeddings("ollama:nomic-embed-text"))
retriever = store.as_retriever(search_kwargs={"k": 3})

model = init_chat_model("ollama:llama3.2:3b")


def make_messages(question):
    docs = retriever.invoke(question)                       # step 1: retrieve
    context = "\n\n".join(d.page_content for d in docs)
    return [
        {"role": "system", "content": "Answer using only the bank policies provided. "
                                      "If they don't contain the answer, say so."},
        {"role": "user", "content": f"Policies:\n{context}\n\nQuestion: {question}"},
    ]


rag_chain = make_messages | model | StrOutputParser()      # step 2: answer
print(rag_chain.invoke("What is the fee for a late credit card payment?"))
