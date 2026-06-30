from src.storage.vector_store import vector_store

docs = vector_store.get(
    include = ["documents", "metadatas"],
    limit = 10
    )

print("=" * 60)
print("CHROMA DATABASE")
print("=" * 60)

print(f"Total Chunks: {len(docs['documents'])}")

print("\nStored Documents:\n")

for i in range(len(docs["documents"])):

    print("-" * 60)

    metadata = docs["metadatas"][i]

    print("Document :", metadata.get("document_name"))
    print("Page     :", metadata.get("page"))
    print("Source   :", metadata.get("source"))

    print("\nChunk Preview:\n")

    print(docs["documents"][i][:250])

    print()
    