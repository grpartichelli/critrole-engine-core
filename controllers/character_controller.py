from flask import Blueprint, request
from flask_cors import cross_origin
from mongo import mongo_utils
from services import character_service

character_controller = Blueprint('character_controller', __name__)


@character_controller.route('/api/character/')
@cross_origin()
def get_character():
    return mongo_utils.to_json(character_service.get_character(request.args.get('name'), request.args.get('actor_name'), request.args.get('actor_nickname'), request.args.get('age'), request.args.get('pronouns'), request.args.get('creature_type'), request.args.get('race'), request.args.get('dnd_class')))