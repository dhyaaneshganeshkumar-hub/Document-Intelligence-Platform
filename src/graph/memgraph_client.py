from gqlalchemy import Memgraph

db = Memgraph(
    host="localhost",
    port=7687
)

def get_memgraph():
    return db