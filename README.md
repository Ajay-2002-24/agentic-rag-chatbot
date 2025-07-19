# Agentic RAG Chatbot for Multi-Format Document QA using Model Context Protocol (MCP)

This is an agent-based chatbot that allows users to upload and ask questions across multiple document formats (PDF, DOCX, TXT, CSV, PPTX, HTML) using Retrieval-Augmented Generation (RAG). It integrates the **Model Context Protocol (MCP)** to improve the precision of responses.

---

##  Features

-  Upload multiple document formats (PDF, DOCX, TXT, CSV, PPTX, HTML)
-  Ask questions and get smart responses from the content
-  File chunking + vector database + LangChain retrieval
-  Model Context Protocol (MCP) for agentic flow control
-  Embedding + RAG pipeline with LLM (OpenAI / GPT-4)
-  Streamlit-based intuitive UI

---

##  Technology

| Area          | Technology                           |
|---------------|---------------------------------------|
| Frontend      | Streamlit                            |
| Backend       | Python, LangChain, OpenAI, FAISS     |
| Embeddings    | `text-embedding-ada-002`             |
| Agent Protocol| Model Context Protocol (MCP)         |
| File Support  | PyMuPDF, Pandas, python-docx, etc.   |

##  Setup Instructions

```bash
git clone https://github.com/your-username/agentic-rag-chatbot.git
cd agentic-rag-chatbot
pip install -r requirements.txt
streamlit run app.py
```

Before running: Add your OpenAI API key in `.env` file like:

```env
OPENAI_API_KEY=your_api_key_here
```
##  Folder Structure

```
├── app.py
├── modules/
│   ├── mcp_agent.py
│   ├── file_parser.py
│   ├── rag_pipeline.py
├── utils/
│   └── helpers.py
├── .env
├── requirements.txt
└── README.md
```

## Example Usage

> **Upload:** Resume.pdf, CourseNotes.docx  
> **Ask:** "What is the candidate's most recent project?"  
> **Response:** "The most recent project described is 'Secure AI Resume Scanner'..."

## MCP Flow

```
flowchart TD
    A[User Uploads Files] --> B[File Chunking + Embedding]
    B --> C[LangChain Retriever]
    C --> D[Agent via MCP]
    D --> E[LLM (GPT-4) Response]
```

##  UI Preview

![Image](https://github.com/user-attachments/assets/592dea95-312b-48ae-b6af-f299837a10ff)


