from src.retrieval.retriever import retrieve

docs = retrieve("CAN FD communications")

print(f"Retrived {len(docs)} documents")

for doc in docs:
    print("-"*50)
    print("Metadata", doc.metadata)
    print()
    print(doc.page_content[:300])
    