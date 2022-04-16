from flask import Blueprint, request
from flask_cors import cross_origin
from mongo import mongo_utils
from services import dice_roll_service

dice_roll_controller = Blueprint('dice_roll_controller', __name__)


@dice_roll_controller.route('/api/dice_roll/avgchar')
@cross_origin()
def average_by_character():
    return mongo_utils.to_json(dice_roll_service.get_average_by_character())