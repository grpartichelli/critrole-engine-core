import json
import pymongo

DATABASE_URL = 'mongodb+srv://mayallengabs:trabpdb2022@critical-role-engine.2rrfv.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'

client = pymongo.MongoClient(DATABASE_URL)
mongo_db = client.db
mongo_db.launches.drop()

with open('static/data/launches.json') as file:
    file_data = json.load(file)

if isinstance(file_data, list):
    mongo_db.launches.insert_many(file_data)
else:
    mongo_db.launches.insert_one(file_data)
