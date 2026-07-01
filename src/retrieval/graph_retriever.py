from src.graph.memgraph_client import get_memgraph

db = get_memgraph()


def search_entity(entity_name):
    print("=" * 50)
    print("Searching:", entity_name)

    query = """
    MATCH (c:Chunk)-[:MENTIONS]->(e:Entity)
    WHERE toLower(e.name) CONTAINS toLower($entity)
       OR toLower($entity) CONTAINS toLower(e.name)
    RETURN c.text AS text
    LIMIT 5
    """

    results = list(
        db.execute_and_fetch(
            query,
            {"entity": entity_name}
        )
    )

    print("Results:", results)

    return [row["text"] for row in results]