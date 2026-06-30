from langchain_chroma import Chroma

from src.ingestion.embedding import embeddings
from src.storage.document_registry import remove_document

VECTOR_DB_PATH = "vector_db"

vector_store = Chroma(
    collection_name = "automotive_docs",
    embedding_function = embeddings,
    persist_directory = VECTOR_DB_PATH
)

retriever = vector_store.as_retriever(
    search_kwargs={"k": 3}
)

def document_exists(document_name):
    results = vector_store.get(
        where={"document_name": document_name},
        include = []
    )

    return len(results["ids"]) > 0

def delete_document(document_name):
    
    result = vector_store.get(
        where = {"document_name": document_name},
        include = []
    )

    if len(result["ids"]) == 0:
        return False
    
    vector_store.delete(ids=result["ids"])

    remove_document(document_name)

    return True

def get_document_names():

    docs = vector_store.get(
        include=["metadatas"])

    names = set()

    for metadata in docs["metadatas"]:
        if metadata:
            names.add(metadata.get("document_name"))

    return sorted(names)
