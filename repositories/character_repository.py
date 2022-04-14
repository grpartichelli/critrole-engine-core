from models.character_model import Character
from mongo import mongo_connector

collection = mongo_connector.get_collection('CHARACTERS')


def drop():
    collection.drop()


def insert_one(character):
    collection.insert_one(character.__dict__)


def find_one(params):
    return convert_mongo_to_character(collection.find_one(params))


def find_all(params):
    return convert_mongo_to_character_list(collection.find(params))


def convert_mongo_to_character(mongo_character):
    del mongo_character['_id']
    return Character(**mongo_character)


def convert_mongo_to_character_list(mongo_character_list):
    character_list=[]
    for i in mongo_character_list:
        character_list.append(convert_mongo_to_character(i))
    return character_list