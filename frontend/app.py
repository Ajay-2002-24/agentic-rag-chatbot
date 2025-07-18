import streamlit as st
import uuid
from agents.ingestion_agent import IngestionAgent
from agents.retrieval_agent import RetrievalAgent
from agents.llm_response_agent import LLMResponseAgent

st.set_page_config(page_title="📚 Agentic RAG Chatbot")
st.title("📚 Agentic RAG Chatbot")

uploaded_files = st.file_uploader("Upload your documents", accept_multiple_files=True)
query = st.text_input("Ask a question")

if uploaded_files and query:
    trace_id = str(uuid.uuid4())

    ingestion_agent = IngestionAgent()
    ingest_msg = ingestion_agent.ingest(uploaded_files, trace_id)

    retrieval_agent = RetrievalAgent()
    retrieval_agent.build_vectorstore(ingest_msg["payload"]["documents"])
    retrieval_msg = retrieval_agent.retrieve(query, trace_id)

    llm_agent = LLMResponseAgent(openai_key="YOUR_OPENAI_API_KEY")
    response = llm_agent.generate_answer(retrieval_msg)

    st.subheader("Answer:")
    st.success(response)

    st.subheader("Source Context:")
    for chunk in retrieval_msg["payload"]["retrieved_context"]:
        st.code(chunk)
