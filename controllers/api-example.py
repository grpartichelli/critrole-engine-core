from bson.objectid import ObjectId
from flask_cors import cross_origin

from mongo.mongo_connector import get_collection
from mongo.mongo_utils import parse_json


@cross_origin()
@app.route('/api/test')
def test():
    collection = get_collection('launches')
    # collection.drop()
    # collection.insert_one({"test": "Hello world from the Api and Mongo :)"})
    result = collection.find_one({'_id': ObjectId('6249ef70adb5c258563fbc0a')})
    return parse_json(result)['test']
