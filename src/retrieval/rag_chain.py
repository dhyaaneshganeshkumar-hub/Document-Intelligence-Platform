from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import AzureChatOpenAI

from src.retrieval.retriever import retrieve

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

    print("Retrieved", len(docs), "documents")

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

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
