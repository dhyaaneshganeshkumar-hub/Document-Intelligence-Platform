import os

from src.loader import load_pdf
from src.splitter import split_documents
from src.vector_store import vector_store, document_exists
from src.document_registry import add_document


def ingest_pdf(filepath):

    document_name = os.path.basename(filepath)

    if document_exists(document_name):

        print(f"{document_name} already exists. Skipping...")

        return {
            "status": "skipped",
            "document": document_name,
            "chunks": 0
        }

    print("Loading PDF...")
    docs = load_pdf(filepath)

    print("Splitting...")
    chunks = split_documents(docs)

    print("Chunks:", len(chunks))

    # Add metadata to every chunk
    for chunk in chunks:

        chunk.metadata["document_name"] = document_name

        if "page_label" in chunk.metadata:
            try:
                chunk.metadata["page"] = int(chunk.metadata["page_label"]) - 1
            except ValueError:
                chunk.metadata["page"] = chunk.metadata["page_label"]

    print("Adding to Chroma...")
    vector_store.add_documents(chunks)

    # Register document
    add_document(document_name)

    print("Done!")

    return {
        "status": "processed",
        "document": document_name,
        "chunks": len(chunks)
    }