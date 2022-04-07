from bson import ObjectId
from flask import Flask
from flask_cors import CORS

from mongo.mongo_connector import get_collection
from mongo.mongo_utils import parse_json

app = Flask(__name__)


def main():
    CORS(app)
    app.run()


@app.route('/api/test')
def test():
    collection = get_collection('launches')
    # collection.drop()
    # collection.insert_one({"test": "Hello world from the Api and Mongo :)"})
    return parse_json(collection.find_one({'_id': ObjectId('6249ef70adb5c258563fbc0a')}))['test']


if __name__ == '__main__':
    main()
