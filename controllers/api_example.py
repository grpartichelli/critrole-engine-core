from bson.objectid import ObjectId
from flask_cors import cross_origin
from flask import Blueprint

from repositories import character_repository
from mongo.mongo_connector import get_collection

app_example = Blueprint('app_example', __name__)


@cross_origin()
@app_example.route('/api/test')
def test():
    character = character_repository.find_one({"name": "Name"})
    return character.to_json()
