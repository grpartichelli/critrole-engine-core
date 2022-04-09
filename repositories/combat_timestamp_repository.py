from models.combat_timestamp_model import CombatTimestamp
from mongo import mongo_connector

collection = mongo_connector.get_collection('COMBAT_TIMESTAMPS')


def drop():
    collection.drop()


def insert_one(combat_timestamp):
    collection.insert_one(combat_timestamp.__dict__)


def find_one(params):
    return convert_mongo_to_combat_timestamp(collection.find_one(params))


def convert_mongo_to_combat_timestamp(mongo_combat_timestamp):
    del mongo_combat_timestamp['_id']
    return CombatTimestamp(**mongo_combat_timestamp)
