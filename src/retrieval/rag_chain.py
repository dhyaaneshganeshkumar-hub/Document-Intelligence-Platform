from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import AzureChatOpenAI

from src.retrieval.retriever import retrieve
from src.retrieval.graph_retriever import search_entity
from src.graph.entity_extractor import extract_entities

import os

from dotenv import load_dotenv

load_dotenv()

llm = AzureChatOpenAI(
    api_key = os.getenv("AZURE_OPENAI_API_KEY"),
    azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_version = os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
)

prompt = ChatPromptTemplate.from_template(
"""
You are an automotive assistant

Use ONLY context below

Context:{context}
Question:{question}
"""
)

def ask(question, selected_document):

    print("=" * 50)
    print("Question:", question)

    print("Calling retriever...")
    docs = retrieve(question, selected_document)

    entities = extract_entities(question)

    print("=" * 60)
    print("Extracted Entities:", entities)
    print("=" * 60)

    graph_context = []

    for entity in entities:
        graph_context.extend(search_entity(entity))

    print("Entities:", entities)
    print("Graph Context:", len(graph_context))

    print("Retrieved", len(docs), "documents")

    chroma_context = "\n\n".join(
        doc.page_content for doc in docs
    )

    graph_text = "\n\n".join(graph_context)

    context_parts = [part for part in [graph_text, chroma_context] if part]
    context = "\n\n".join(context_parts)

    sources = []
    for doc in docs:
        metadata = doc.metadata
        page = metadata.get("page")

        try:
            page = int(page) + 1
        except:
            page = str(page)

        sources.append({
            "document": metadata.get("document_name"),
            "page": page
        })

    print("Context length:", len(context))

    print("Calling Azure OpenAI...")

    chain = prompt | llm

    response = chain.invoke({
        "context": context,
        "question": question
    })

    print("Azure response received!")

    from pprint import pprint
    pprint(sources)

    return{
        "answer": response.content,
        "sources": sources
    }
