# agents/retrieval_agent.py
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.schema import Document
from mcp.context_protocol import create_mcp_message

def retrieval_agent(documents, query, trace_id):
    embeddings = HuggingFaceEmbeddings()
    texts = [Document(page_content=doc) for doc in documents]
    db = FAISS.from_documents(texts, embeddings)
    retriever = db.as_retriever()
    results = retriever.get_relevant_documents(query)
    chunks = [res.page_content for res in results]

    return create_mcp_message(
        sender="RetrievalAgent",
        receiver="LLMResponseAgent",
        type_="RETRIEVAL_RESULT",
        payload={"retrieved_context": chunks, "query": query},
        trace_id=trace_id
    )
