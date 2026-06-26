from src.vector_store import vector_store

def retrieve(query, selected_document=None, top_k=3):

    if selected_document and selected_document != "All Documents":

        docs = vector_store.similarity_search(
            query=query,
            k=top_k,
            filter={
                "document_name": selected_document
            }
        )

    else:

        docs = vector_store.similarity_search(
            query=query,
            k=top_k
        )

    return docs
