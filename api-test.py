import json

import pymongo
from bson import json_util
from bson.objectid import ObjectId
from flask import Flask

app = Flask(__name__)

DATABASE_URL = 'mongodb+srv://mayallengabs:trabpdb2022@critical-role-engine.2rrfv.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'

client = pymongo.MongoClient(DATABASE_URL)
mongo_db = client.db

collection = mongo_db['launches']


# collection.drop()
# collection.insert_one({"test": "Hello world from the Api and Mongo :)"})


@app.route('/test/')
def sample():
    return parse_json(collection.find_one({'_id': ObjectId('6249ef70adb5c258563fbc0a')}))['test']


def parse_json(data):
    return json.loads(json_util.dumps(data))


if __name__ == '__main__':
    app.run()
