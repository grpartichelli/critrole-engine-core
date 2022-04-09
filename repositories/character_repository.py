from models.character_model import Character
from mongo import mongo_connector

collection = mongo_connector.get_collection('CHARACTERS')


def drop():
    collection.drop()


def insert_one(character):
    collection.insert_one(character.__dict__)


def find_one(params):
    return convert_mongo_to_character(collection.find_one(params))


def convert_mongo_to_character(mongo_character):
    del mongo_character['_id']
    return Character(**mongo_character)
