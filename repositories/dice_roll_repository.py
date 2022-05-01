from models.dice_roll_model import DiceRoll
from models.avg_dice_roll_model import AvgDiceRoll
from mongo import mongo_connector

collection = mongo_connector.get_collection('DICE_ROLLS')


def drop():
    collection.drop()


def insert_one(dice_roll):
    collection.insert_one(dice_roll.__dict__)


def find_one(params):
    return convert_mongo_to_dice_roll(collection.find_one(params))


def find_all(params):
    return convert_mongo_to_dice_roll_list(collection.find(params))


def average_by_character():
    return convert_mongo_to_avg_dice_roll_list(collection.aggregate([
        {
            "$unwind": "$character_name"
        },   
        { 
            "$match": 
            {
                "total_value": { 
                    "$exists": True, 
                    "$ne": float("nan") 
                }
            }
        } ,
        { "$group": {
            "_id": { 
                "character_name": "$character_name"
            },
            "average": { "$avg": "$total_value" },
        } }
    ]))


def convert_mongo_to_dice_roll(mongo_dice_roll):
    del mongo_dice_roll['_id']
    return DiceRoll(**mongo_dice_roll)


def convert_mongo_to_dice_roll_list(mongo_dice_roll_list):
    dice_roll_list=[]
    for i in mongo_dice_roll_list:
        dice_roll_list.append(convert_mongo_to_dice_roll(i))
    return dice_roll_list


def convert_mongo_to_avg_dice_roll(mongo_avg_dice_roll):
    return AvgDiceRoll(**mongo_avg_dice_roll)


def convert_mongo_to_avg_dice_roll_list(mongo_avg_dice_roll_list):
    avg_dice_roll_list=[]
    for i in mongo_avg_dice_roll_list:
        avg_dice_roll_list.append(convert_mongo_to_avg_dice_roll(i))
    return avg_dice_roll_list