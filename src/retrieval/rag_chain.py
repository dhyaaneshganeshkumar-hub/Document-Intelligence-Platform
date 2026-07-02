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
    docs, image_docs = retrieve(
        question,
        selected_document
        )

    image_docs = [doc for doc in docs if doc.metadata.get("type") == "image"]

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

    text_docs = [
        doc for doc in docs
        if doc.metadata.get("type") != "image"
        ]

    chroma_context = "\n\n".join(
        doc.page_content
        for doc in text_docs
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

    show_images = False

    if image_docs:

        image_pages = {
            img.metadata.get("page")
            for img in image_docs
        }

        text_pages = {
            doc.metadata.get("page")
            for doc in text_docs
        }

        if image_pages.intersection(text_pages):
           show_images = True

    return{
        "answer": response.content,
        "sources": sources
    }
