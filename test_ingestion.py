from src.loader import load_pdf
from src.splitter import split_documents

docs = load_pdf("data/sample.pdf")

print(f"Pages loaded: {len(docs)}")

chunks = split_documents(docs)

print(f"Chunks created: {len(chunks)}")

print("\nFirst Chunk:\n")
print(chunks[0].page_content)