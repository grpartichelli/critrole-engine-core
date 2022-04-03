import pymongo

DATABASE_URL = 'mongodb+srv://mayallengabs:trabpdb2022@critical-role-engine.2rrfv.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'

client = pymongo.MongoClient(DATABASE_URL)
mongo_db = client.db
mongo_db.launches.drop()

mongo_db.launches.insert_one({"test": "hello-world2"})
