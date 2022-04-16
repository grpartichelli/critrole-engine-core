from models.transcript_model import Transcript
from mongo import mongo_connector

collection = mongo_connector.get_collection('TRANSCRIPTS')


def drop():
    collection.drop()


def insert_one(transcript):
    collection.insert_one(transcript.__dict__)


def find_one(params):
    return convert_mongo_to_transcript(collection.find_one(params))


def find_all(params):
    return convert_mongo_to_transcript_list(collection.find(params))


def convert_mongo_to_transcript(mongo_transcript):
    del mongo_transcript['_id']
    return Transcript(**mongo_transcript)


def convert_mongo_to_transcript_list(mongo_transcript_list):
    transcript_list=[]
    for i in mongo_transcript_list:
        transcript_list.append(convert_mongo_to_transcript(i))
    return transcript_list
