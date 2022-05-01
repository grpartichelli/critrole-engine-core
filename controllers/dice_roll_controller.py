from flask import Blueprint, send_file
from flask_cors import cross_origin
from mongo import mongo_utils
from services import dice_roll_service

dice_roll_controller = Blueprint('dice_roll_controller', __name__)


@dice_roll_controller.route('/api/dice_roll/avgchar')
@cross_origin()
def average_by_character():
    return mongo_utils.to_json(dice_roll_service.get_average_by_character())

@dice_roll_controller.route('/api/dice_roll/words/<roll>')
@cross_origin()
def most_used_words_by_roll(roll):
    return send_file(dice_roll_service.most_used_words_by_roll(roll), mimetype='image/png')