from models.transcript_model import Transcript
from models.count_string_occurrences import CntStringOccurrences
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


def count_string_per_episode(params):
    return convert_mongo_to_cnt_string_occurrences_list(collection.aggregate([   
        { 
            "$match": params
        } ,
        { "$group": {
            "_id": "$episode_number",
            "count": { "$sum": 1 },
        } }
    ]))


def convert_mongo_to_transcript(mongo_transcript):
    del mongo_transcript['_id']
    return Transcript(**mongo_transcript)


def convert_mongo_to_transcript_list(mongo_transcript_list):
    transcript_list=[]
    for i in mongo_transcript_list:
        transcript_list.append(convert_mongo_to_transcript(i))
    return transcript_list


def convert_mongo_to_cnt_string_occurrences(mongo_cnt_string_occurrences):
    return CntStringOccurrences(**mongo_cnt_string_occurrences)


def convert_mongo_to_cnt_string_occurrences_list(mongo_cnt_string_occurrences_list):
    cnt_string_occurrences_list=[]
    for i in mongo_cnt_string_occurrences_list:
        cnt_string_occurrences_list.append(convert_mongo_to_cnt_string_occurrences(i))
    return cnt_string_occurrences_list