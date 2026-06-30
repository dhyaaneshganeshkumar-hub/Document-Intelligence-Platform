from src.storage.mongo_store import collection 

sample_doc = {
    "test" : "CAN FD support payloadsup to 64 bytes",
    "sources" : "sample.pdf"
}

collection.insert_one(sample_doc)

print("inserted sucessfully")
