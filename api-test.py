import pymongo
from bson.objectid import ObjectId
from flask import Flask
from flask_cors import CORS

from mongo.mongo_utils import parse_json

app = Flask(__name__)
CORS(app)

DATABASE_URL = 'mongodb+srv://mayallengabs:trabpdb2022@critical-role-engine.2rrfv.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'

client = pymongo.MongoClient(DATABASE_URL)
mongo_db = client.db

collection = mongo_db['launches']


# collection.drop()
# collection.insert_one({"test": "Hello world from the Api and Mongo :)"})

@app.route('/api/test')
def sample():
    return parse_json(collection.find_one({'_id': ObjectId('6249ef70adb5c258563fbc0a')}))['test']


if __name__ == '__main__':
    app.run()
