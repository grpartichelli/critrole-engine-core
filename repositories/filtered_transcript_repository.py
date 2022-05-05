from models.transcript_model import Transcript
from mongo import mongo_connector

collection = mongo_connector.get_collection('FILTERED_TRANSCRIPTS')


def drop():
    collection.drop()


def insert_one(transcript):
    collection.insert_one(transcript.__dict__)


def find_one(params):
    return convert_mongo_to_transcript(collection.find_one(params))


def most_common_strings(params):
    return convert_mongo_to_dictionary(collection.aggregate(
        [{
            "$match": params
        },
            {
                '$addFields': {
                    'words': {
                        '$map': {
                            'input': {'$split': ['$text', ' ']},
                            'as': 'str',
                            'in': {
                                '$trim': {
                                    'input': {'$toLower': ['$$str']},
                                    'chars': " ,|(){}[]-<>.:;"
                                }
                            }
                        }
                    }
                }
            },
            {'$unwind': '$words'},
            {
                '$match': {
                    'words': {
                        '$nin': [""]
                    }
                }
            },
            {"$group": {
                "_id": "$words",
                "count": {"$sum": 1},
            }}]
    ))


def most_common_strings_by_timestamps(before, after):
    return most_common_strings({"timestamp": {"$gte": before, "$lt": after}})


def convert_mongo_to_dictionary(mongo_cursor):
    dictionary = dict()
    for i in list(mongo_cursor):
        dictionary[i["_id"]] = i["count"]
    return dictionary


def convert_mongo_to_transcript(mongo_transcript):
    del mongo_transcript['_id']
    return Transcript(**mongo_transcript)
