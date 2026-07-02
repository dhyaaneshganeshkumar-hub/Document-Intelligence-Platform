# 🚗 Automotive Document Intelligence Platform

An AI-powered document intelligence platform built for automotive engineering workflows. The application enables users to upload technical PDF documents, generate semantic embeddings, build a lightweight knowledge graph, and chat with documents using Retrieval-Augmented Generation (RAG).

Developed as part of an AI R&D Internship at ZF Group.

---

## ✨ Features

- 📄 Upload and process PDF documents
- 🔍 Semantic search using ChromaDB
- 🤖 Chat with documents using Azure OpenAI
- 🧠 Hybrid Retrieval (Vector Search + Knowledge Graph)
- 🌐 Knowledge Graph built using Memgraph
- 🏷️ Automatic entity extraction from documents
- 💬 Persistent chat history with session management
- 📂 Search across all documents or a selected document
- 🗑️ Delete unwanted documents
- 🚫 Duplicate document detection
- 📚 Document registry management
- 🎨 Interactive Streamlit interface

---

## 🏗️ Architecture

```
                Upload PDF
                     │
                     ▼
              Document Loader
                     │
                     ▼
             Text Splitter
                     │
         ┌───────────┴───────────┐
         ▼                       ▼
  Generate Embeddings     Extract Entities
         │                       │
         ▼                       ▼
     ChromaDB             Memgraph Database
         │                       │
         └───────────┬───────────┘
                     ▼
              Hybrid Retrieval
                     │
                     ▼
              Azure OpenAI LLM
                     │
                     ▼
              Streamlit Interface
```

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Azure OpenAI
- LangChain
- ChromaDB
- Memgraph
- MongoDB
- PyPDF
- Sentence Transformers

---

## 📁 Project Structure

```
Automotive-Assistant
│
├── app.py
├── requirements.txt
├── README.md
│
├── src
│   ├── graph
│   │   ├── entity_extractor.py
│   │   ├── graph_builder.py
│   │   └── memgraph_client.py
│   │
│   ├── ingestion
│   │   ├── loader.py
│   │   ├── splitter.py
│   │   └── ingest.py
│   │
│   ├── retrieval
│   │   ├── retriever.py
│   │   ├── graph_retriever.py
│   │   └── rag_chain.py
│   │
│   ├── memory
│   │   ├── session_manager.py
│   │   ├── history_store.py
│   │   └── chat_history.py
│   │
│   ├── storage
│   │   ├── vector_store.py
│   │   ├── mongo_store.py
│   │   └── document_registry.py
│   │
│   ├── llm
│   │   └── llm.py
│   │
│   └── tests
│
├── uploads
├── vector_db
└── data
```

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/<your-username>/Automotive-Assistant.git
```

Navigate into the project

```bash
cd Automotive-Assistant
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## 🔑 Environment Variables

Create a `.env` file in the root directory and configure the following:

```env
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_VERSION=
AZURE_OPENAI_DEPLOYMENT_NAME=

MONGODB_URI=

MEMGRAPH_HOST=localhost
MEMGRAPH_PORT=7687
```

---

## 📷 Application

The application supports:

- Upload PDF documents
- Automatic embedding generation
- Knowledge graph construction
- Chat with uploaded documents
- Session-based conversation history
- Search within selected documents
- Document management

---

## 🧠 Retrieval Pipeline

```
User Question
      │
      ▼
Entity Extraction
      │
      ▼
Knowledge Graph Retrieval
      │
      ▼
Vector Similarity Search
      │
      ▼
Merge Context
      │
      ▼
Azure OpenAI
      │
      ▼
Generated Response + Sources
```

---

## 🎯 Future Improvements

- Full GraphRAG implementation
- Automotive domain ontology
- Graph visualization
- OCR support for scanned PDFs
- Support for DOCX, PPTX and Excel
- Multi-user authentication
- Docker deployment
- Cloud deployment
- Source highlighting inside documents

---

## 👨‍💻 Author

**Dhyaanesh G**

AI R&D Intern – ZF Group

National Institute of Technology Tiruchirappalli (NIT Trichy)

---

## 📄 License

This project is intended for educational and research purposes.
