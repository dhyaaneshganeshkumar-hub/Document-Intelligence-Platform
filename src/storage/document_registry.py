import json
import os

REGISTRY_FILE = "documents.json"


def load_documents():

    if not os.path.exists(REGISTRY_FILE):
        return []

    with open(REGISTRY_FILE, "r") as f:
        return json.load(f)


def save_documents(documents):

    with open(REGISTRY_FILE, "w") as f:
        json.dump(sorted(documents), f, indent=4)


def add_document(document_name):

    documents = load_documents()

    if document_name not in documents:
        documents.append(document_name)

    print("Registry:", documents)

    save_documents(documents)


def remove_document(document_name):

    documents = load_documents()

    if document_name in documents:
        documents.remove(document_name)

    save_documents(documents)


def get_document_names():

    return load_documents()
