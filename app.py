# app.py
import streamlit as st
import uuid
from agents.ingestion_agent import ingestion_agent
from agents.retrieval_agent import retrieval_agent
from agents.llm_response_agent import llm_response_agent

st.set_page_config(page_title="Agentic RAG Chatbot", layout="wide")
st.title("Agentic RAG Chatbot")
st.write("Upload your documents and ask questions!")

uploaded_files = st.file_uploader(
    "Upload files", type=["pdf", "txt", "docx", "pptx", "csv"], accept_multiple_files=True
)

query = st.text_input("Ask a question")

if st.button("Submit") and uploaded_files and query:
    trace_id = str(uuid.uuid4())

    # Step 1: Ingestion
    ingestion_msg = ingestion_agent(uploaded_files, trace_id)

    # Step 2: Retrieval
    retrieval_msg = retrieval_agent(ingestion_msg["payload"]["documents"], query, trace_id)

    # Step 3: LLM Response
    answer = llm_response_agent(retrieval_msg)

    st.markdown("### ✅ Answer:")
    st.write(answer)

    st.markdown("### 📄 Source Context:")
    for chunk in retrieval_msg["payload"]["retrieved_context"]:
        st.markdown(f"- {chunk}")


