from src.loader import load_pdf
from src.splitter import split_documents
from src.embedding import embeddings
from src.mongo_store import store_chunks

docs = load_pdf("data/sample.pdf")

chunks = split_documents(docs)

texts = [chunk.page_content for chunk in chunks]

vectors = embeddings.embed_documents(texts)

store_chunks(chunks, vectors)
