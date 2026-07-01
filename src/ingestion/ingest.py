import os

from src.ingestion.loader import load_pdf
from src.ingestion.splitter import split_documents
from src.storage.vector_store import vector_store, document_exists
from src.storage.document_registry import add_document
from src.graph.graph_builder import add_graph_document, add_chunk, add_entity, link_chunk_entity
from src.graph.entity_extractor import extract_entities


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

    add_graph_document(document_name)

    for i, chunk in enumerate(chunks):
        chunk_id = f"{document_name}_{i}"

        add_chunk(
            chunk_id=chunk_id,
            text=chunk.page_content,
            document_name=document_name,
        )

        entities = extract_entities(chunk.page_content)
        print("Entities:", entities)

        for entity in entities:
            add_entity(entity)
            link_chunk_entity(chunk_id, entity)

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

    add_document(document_name)

    print("Done!")

    return{
        "status" : "processed",
        "document" : document_name,
        "chunks" : len(chunks)
    }