from src.embedding import embeddings

vector = embeddings.embed_query("CAN FD communication")

print(type(vector))
print(len(vector))
