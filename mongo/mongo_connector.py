import pymongo

DATABASE_URL = 'mongodb+srv://mayallengabs:trabpdb2022@critical-role-engine.2rrfv.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
client = pymongo.MongoClient(DATABASE_URL)
mongo_db = client.db


def get_collection(collection):
    return mongo_db[collection]
