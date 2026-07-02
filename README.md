# 🚗 Automotive Document Intelligence Platform

> An AI-powered multimodal document intelligence platform that combines Retrieval-Augmented Generation (RAG), GraphRAG, Knowledge Graphs, and Vision Language Models to enable intelligent interaction with automotive technical documents.

---

# 📖 Overview

The Automotive Document Intelligence Platform is designed to simplify the analysis of complex automotive documentation by allowing users to upload PDF files and interact with them using natural language.

Unlike traditional document chatbots that rely solely on vector similarity search, this platform combines semantic retrieval, graph-based retrieval, and image understanding to generate more accurate, grounded, and context-aware responses.

The system extracts knowledge from both textual and visual information, builds a knowledge graph of entities and their relationships, and retrieves relevant information from multiple retrieval pipelines before generating a final response using Azure OpenAI.

---

# ✨ Key Features

## 📄 Intelligent PDF Processing

- Upload one or multiple PDF documents
- Automatic document chunking
- Metadata extraction
- Page-level indexing
- Duplicate document detection
- Document registry management

---

## 🤖 AI-Powered Question Answering

- Natural language interaction
- Context-aware answers
- Grounded responses
- Hallucination reduction
- Source citations
- Page references

---

## 🔍 Vector-Based Retrieval (RAG)

- Semantic similarity search
- Chroma Vector Database
- Context retrieval
- Fast document lookup
- Relevant chunk ranking

---

## 🕸️ GraphRAG using Memgraph

The platform constructs a Knowledge Graph from every uploaded document.

Features include:

- Automatic entity extraction
- Entity relationships
- Graph traversal
- Graph-based retrieval
- Context enrichment
- Hybrid retrieval

GraphRAG enables the assistant to retrieve information based on semantic relationships rather than only vector similarity.

---

## 👁️ Multimodal Image Understanding

The platform processes images embedded inside PDF documents.

Features:

- Image extraction
- Azure OpenAI Vision integration
- Automatic image description generation
- Image entity extraction
- Image indexing
- Image retrieval

Image descriptions become searchable alongside textual content.

---

## 🧠 Entity Extraction

Entities are extracted from:

- Document text
- Image descriptions
- User questions

These entities are stored inside the Knowledge Graph and used during retrieval.

---

## 💬 Persistent Chat History

Supports:

- Multiple chat sessions
- Conversation persistence
- Automatic session creation
- Chat renaming
- Chat clearing
- Context preservation

---

## 📚 Document Management

- Upload documents
- Process documents
- Delete documents
- Prevent duplicate uploads
- View available documents
- Switch between documents

---

## 🎯 Source Attribution

Every answer includes:

- Source document
- Page number
- Retrieved context

This makes responses transparent and verifiable.

---

# 🏗️ System Architecture

```
                     User Uploads PDF
                             │
                             ▼
                  Document Processing Pipeline
                             │
        ┌────────────────────┴────────────────────┐
        │                                         │
        ▼                                         ▼
 Text Extraction                           Image Extraction
        │                                         │
        ▼                                         ▼
 Document Chunking                 Azure OpenAI Vision Model
        │                                         │
        ▼                                         ▼
 Entity Extraction                 Image Description Generation
        │                                         │
        ▼                                         ▼
 Memgraph Knowledge Graph             Chroma Image Index
        │                                         │
        └────────────────────┬────────────────────┘
                             │
                             ▼
                    Chroma Vector Database
                             │
                             ▼
                      User asks Question
                             │
                             ▼
                  Question Entity Extraction
                             │
               ┌─────────────┴─────────────┐
               ▼                           ▼
       Vector Retrieval             Graph Retrieval
               │                           │
               └─────────────┬─────────────┘
                             ▼
                  Context Combination Layer
                             ▼
                  Azure OpenAI GPT Model
                             ▼
             Final Response + Source References
```

---

# 📂 Project Structure

```
Automotive-Assistant/

│
├── app.py
├── requirements.txt
├── README.md
│
├── uploads/
│
├── src/
│
│   ├── graph/
│   │     ├── graph_builder.py
│   │     ├── entity_extractor.py
│   │     └── memgraph_client.py
│   │
│   ├── ingestion/
│   │     ├── loader.py
│   │     ├── splitter.py
│   │     ├── ingest.py
│   │     └── image_ingestion.py
│   │
│   ├── retrieval/
│   │     ├── retriever.py
│   │     ├── graph_retriever.py
│   │     └── rag_chain.py
│   │
│   ├── llm/
│   │     ├── llm.py
│   │     └── multimodal.py
│   │
│   ├── memory/
│   │     ├── session_manager.py
│   │     ├── chat_history.py
│   │     └── history_store.py
│   │
│   ├── storage/
│   │     ├── vector_store.py
│   │     └── document_registry.py
│   │
│   └── vision/
│         └── vision_processor.py
│
└── tests/
```

---

# ⚙️ Technology Stack

## Programming Language

- Python

---

## Frontend

- Streamlit

---

## LLM

- Azure OpenAI GPT

---

## Vision Model

- Azure OpenAI Vision

---

## Retrieval

- LangChain
- ChromaDB
- GraphRAG

---

## Knowledge Graph

- Memgraph

---

## Vector Database

- ChromaDB

---

## NLP

- Entity Extraction
- Prompt Engineering
- Semantic Search

---

# 🔄 Complete Workflow

### Step 1

Upload a PDF document.

↓

### Step 2

Extract document text.

↓

### Step 3

Split into semantic chunks.

↓

### Step 4

Extract entities from chunks.

↓

### Step 5

Store entities inside Memgraph.

↓

### Step 6

Generate embeddings.

↓

### Step 7

Store embeddings inside ChromaDB.

↓

### Step 8

Extract images.

↓

### Step 9

Generate image descriptions using Azure OpenAI Vision.

↓

### Step 10

Store image descriptions and entities.

↓

### Step 11

User asks a question.

↓

### Step 12

Extract entities from the question.

↓

### Step 13

Retrieve:

- Vector Context
- Graph Context

↓

### Step 14

Merge contexts.

↓

### Step 15

Generate answer using Azure OpenAI GPT.

↓

### Step 16

Display answer with source references.

---

# 🧪 Testing

The project includes tests for:

- Document ingestion
- Graph creation
- Graph retrieval
- Vector retrieval
- Embedding generation
- Image ingestion
- Vision processing
- Chat history
- Session management
- MongoDB utilities

---

# 🚀 Future Enhancements

- LangGraph agent workflows
- LightRAG integration
- Hybrid Search (BM25 + Vector Search)
- OCR for scanned PDFs
- Table extraction
- Image-grounded answering
- Cross-document reasoning
- Knowledge graph visualization
- Authentication & user management
- REST API deployment
- Docker containerization
- Kubernetes deployment
- Azure Blob Storage integration
- Citation highlighting inside PDFs

---

# 📸 Screenshots

Include screenshots of:

- Home Page
- Upload Screen
- Chat Interface
- Source References
- GraphRAG Workflow
- Knowledge Graph
- Chat History
- Document Management

---

# 📈 Project Highlights

✅ Retrieval-Augmented Generation (RAG)

✅ GraphRAG using Memgraph

✅ Multimodal AI (Text + Images)

✅ Azure OpenAI GPT

✅ Azure OpenAI Vision

✅ Knowledge Graph Construction

✅ Semantic Search

✅ Entity Extraction

✅ Persistent Chat History

✅ Multi-document Support

✅ Source Attribution

✅ Streamlit Interface

---

# 👨‍💻 Author

**Dhyaanesh Ganeshkumar**

Built during an AI internship to explore advanced document intelligence using Retrieval-Augmented Generation (RAG), GraphRAG, Knowledge Graphs, Vision Language Models, and Azure OpenAI.

This project demonstrates how modern AI systems can combine vector search, graph databases, and multimodal understanding to create intelligent assistants capable of reasoning over complex technical documentation.


AI R&D Intern – ZF Group

National Institute of Technology Tiruchirappalli (NIT Trichy)
