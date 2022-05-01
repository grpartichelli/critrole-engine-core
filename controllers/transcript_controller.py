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

@transcript_controller.route('/api/transcripts/character_interactions/<first_actor>/<second_actor>')
@cross_origin()
def character_interactions(first_actor,second_actor):
    return send_file(transcript_service.character_interactions(first_actor,second_actor), mimetype='image/png')

@transcript_controller.route('/api/transcripts/wordcloud/')
@cross_origin()
def wordcloud():
    return send_file(transcript_service.wordcloud(request.args.get('actor_nickname'), request.args.get('episode_number')), mimetype='image/png')

@transcript_controller.route('/api/transcripts/rank/<words>')
@cross_origin()
def rank_actors_by_words(words):
    return mongo_utils.to_json(transcript_service.rank_actors_by_words(words))

@transcript_controller.route('/api/transcripts/in_combat/<episode_number>')
@cross_origin()
def transcripts_in_combat(episode_number):
    return mongo_utils.to_json(transcript_service.get_transcripts_in_combat(episode_number))