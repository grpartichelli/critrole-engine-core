from models.dice_rolls_model import DiceRoll
from mongo.mongo_connector import get_collection

collection = get_collection('DICE_ROLLS')


def drop():
    collection.drop()


def insert_one(dice_roll):
    collection.insert_one(dice_roll.__dict__)


def find_one(params):
    return convert_mongo_to_dice_roll(collection.find_one(params))


def convert_mongo_to_dice_roll(mongo_dice_roll):
    del mongo_dice_roll['_id']
    return DiceRoll(**mongo_dice_roll)
