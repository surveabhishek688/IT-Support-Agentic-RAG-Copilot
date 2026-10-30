# IT Support Agentic RAG Copilot 🤖

An AI-powered IT support assistant that uses **Retrieval-Augmented Generation (RAG)** and agentic workflows to answer IT-related questions using internal knowledge bases and web search.

## 🚀 Features
- **Knowledge Base Retrieval:** Retrieves relevant information from internal IT documentation.
- **Agentic Workflow:** Routes queries based on their requirements.
- **Web Search Fallback:** Uses web search when internal knowledge is insufficient.
- **Audit Logging:** Stores user queries, sources, and execution traces in SQLite.
- **Document Ingestion:** Processes knowledge base documents for retrieval.

## 🛠️ Tech Stack
- Python
- LangChain
- RAG
- SQLite
- Large Language Models (LLMs)
- Web Search

## 📁 Project Structure
```text
IT-Support-Agentic-RAG-Copilot/
├── app/
│   ├── core/
│   ├── rag/
│   └── services/
├── data/
│   └── sample_kb/
├── static/
├── templates/
├── tests/
├── run.py
├── requirements.txt
└── README.md
```

## ⚙️ Setup

```bash
git clone <your-repository-url>
cd IT-Support-Agentic-RAG-Copilot

conda create -n project python=3.11
conda activate project

pip install -r requirements.txt
```

Configure your environment variables in a `.env` file, then run:

```bash
python run.py
```

## 📊 Audit Logging

The application uses SQLite to store audit records, including:
- Timestamp
- User question
- Response source
- Agent execution trace

The database is initialized through `app/services/audit.py`.

## 🎯 Goal

To build a reliable IT support assistant that combines internal documentation, intelligent query routing, web search, and auditability.