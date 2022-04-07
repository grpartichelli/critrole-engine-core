from mongo.mongo_connector import get_collection

collection = get_collection('character')


def insert_one(character):
    collection.insert_one(character.__dict__)
