from src.graph.graph_builder import add_graph_document, add_chunk, add_entity, link_chunk_entity
from src.graph.memgraph_client import get_memgraph

db = get_memgraph()

add_graph_document("sample.pdf")
add_chunk(
    "chunk_1",
    "Automotive AI is awesome.",
    "sample.pdf"
)

add_entity("Automotive AI")
link_chunk_entity("chunk_1", "Automotive AI")

print("Nodes in graph:")

results = db.execute_and_fetch("""
MATCH (n)
RETURN n
""")

for row in results:
    print(row)