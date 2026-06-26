from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["automotive_rag"]

collection = db["documents"]


def get_collection():
    return collection


def store_chunks(chunks, vectors, document_name):

    docs = []

    for chunk, vector in zip(chunks, vectors):

        docs.append(
            {
                "document": document_name,
                "text": chunk.page_content,
                "embedding": vector,
                "metadata": chunk.metadata
            }
        )

    collection.insert_many(docs)

    print(f"Stored {len(docs)} chunks")

def get_document_names():

    docs = collection.distinct("document")
    return sorted(docs)
