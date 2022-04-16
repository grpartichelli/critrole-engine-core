from flask import Blueprint, request, send_file
from flask_cors import cross_origin
from mongo import mongo_utils
from services import transcript_service

transcript_controller = Blueprint('transcript_controller', __name__)

@transcript_controller.route('/api/transcripts/search/<text>')
@cross_origin()
def search_transcripts(text):
    return mongo_utils.to_json(transcript_service.search_transcripts(text, request.args.get('episode_number'), request.args.get('actor_nickname')))

@transcript_controller.route('/api/transcripts/search_per_episode/<text>')
@cross_origin()
def search_transcripts_per_episode(text):
    return send_file(transcript_service.search_per_episode(text, request.args.get('actor_nickname')), mimetype='image/png')

