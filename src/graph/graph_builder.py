from src.graph.memgraph_client import get_memgraph

db = get_memgraph()


def add_graph_document(document_name):
    query = """
    MERGE (d:Document {name:$name})
    """
    db.execute(query, {"name": document_name})


def add_chunk(chunk_id, text, document_name):
    query = """
    MERGE (c:Chunk {id:$id})
    SET c.text=$text

    MERGE (d:Document {name:$doc})

    MERGE (d)-[:HAS_CHUNK]->(c)
    """

    db.execute(
        query,
        {
            "id": chunk_id,
            "text": text,
            "doc": document_name,
        },
    )

def add_entity(entity_name):
    query = """
    MERGE (e:Entity {name:$name})
    """

    db.execute(query, {
        "name": entity_name
    })


def link_chunk_entity(chunk_id, entity_name):
    query = """
    MATCH (c:Chunk {id:$chunk})
    MATCH (e:Entity {name:$entity})

    MERGE (c)-[:MENTIONS]->(e)
    """

    db.execute(
        query,
        {
            "chunk": chunk_id,
            "entity": entity_name,
        },
    )

def add_image(image_id, image_path, description, document_name):
    query = """
    MERGE (i:Image {id:$id})
    SET i.path = $path,
        i.description = $description

    MERGE (d:Document {name:$doc})
    MERGE (d)-[:HAS_IMAGE]->(i)
    """

    db.execute(
        query,
        {
            "id": image_id,
            "path": image_path,
            "description": description,
            "doc": document_name,
        },
    )

def link_image_entity(image_id, entity_name):
    query = """
    MATCH (i:Image {id:$image})
    MATCH (e:Entity {name:$entity})

    MERGE (i)-[:MENTIONS]->(e)
    """

    db.execute(
        query,
        {
            "image": image_id,
            "entity": entity_name,
        },
    )

