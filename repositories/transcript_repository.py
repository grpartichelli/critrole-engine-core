from models.transcript_model import Transcript
from mongo import mongo_connector

collection = mongo_connector.get_collection('TRANSCRIPTS')


def drop():
    collection.drop()


def insert_one(transcript):
    collection.insert_one(transcript.__dict__)


def find_one(params):
    return convert_mongo_to_transcript(collection.find_one(params))


def convert_mongo_to_transcript(mongo_transcript):
    del mongo_transcript['_id']
    return Transcript(**mongo_transcript)
