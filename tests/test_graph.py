from src.graph.memgraph_client import get_memgraph

db = get_memgraph()

query = """
CREATE (n:Test {name: 'Dhyaanesh'})
"""

db.execute(query)

print("✅ Connected Successfully!")