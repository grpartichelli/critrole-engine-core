from flask import Blueprint
from flask_cors import cross_origin

from mongo import mongo_utils
from repositories import character_repository, dice_roll_repository

app_example = Blueprint('app_example', __name__)


@app_example.route('/api/test')
@cross_origin()
def test():
    character = character_repository.find_one({})
    dice_roll = dice_roll_repository.find_one({})
    return mongo_utils.to_json([character, dice_roll])
