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
                'input': { '$split': ['$text', ' '] },
                'as': 'str',
                'in': {
                    '$trim': {
                    'input': { '$toLower': ['$$str'] },
                    'chars': " ,|(){}[]-<>.:;"
                    }
                }
                }
            }
            }
        },
        { '$unwind': '$words' },
        {
            '$match': {
                'words': {
                    '$nin': ["", "also", "i", "me", "my", "myself", "we", "us",
                        "our", "ours", "ourselves", "you", "your", "yours",
                        "yourself", "yourselves", "he", "him", "his",
                        "himself", "she", "her", "hers", "herself", "it",
                        "its", "itself", "they", "them", "their", "theirs",
                        "themselves", "what", "which", "who", "whom", "whose",
                        "this", "that", "these", "those", "am", "is", "are",
                        "was", "were", "be", "been", "being", "have", "has",
                        "had", "having", "do", "does", "did", "doing", "will",
                        "would", "should", "can", "could", "ought", "i'm",
                        "you're", "he's", "she's", "it's", "we're", "they're",
                        "i've", "you've", "we've", "they've", "i'd", "you'd",
                        "he'd", "she'd", "we'd", "they'd", "i'll", "you'll",
                        "he'll", "she'll", "we'll", "they'll", "isn't",
                        "aren't", "wasn't", "weren't", "hasn't", "haven't",
                        "hadn't", "doesn't", "don't", "didn't", "won't",
                        "wouldn't", "shan't", "shouldn't", "can't", "cannot",
                        "couldn't", "mustn't", "let's", "that's", "who's",
                        "what's", "here's", "there's", "when's", "where's",
                        "why's", "how's", "a", "an", "the", "and", "but",
                        "if", "or", "because", "as", "until", "while", "of",
                        "at", "by", "for", "with", "about", "against",
                        "between", "into", "through", "during", "before",
                        "after", "above", "below", "to", "from", "up", "upon",
                        "down", "in", "out", "on", "off", "over", "under",
                        "again", "further", "then", "once", "here", "there", "when",
                        "where", "why", "how", "all", "any", "both", "each",
                        "few", "more", "most", "other", "some", "such", "no",
                        "nor", "not", "only", "own", "same", "so", "than",
                        "too", "very", "say", "says", "said", "shall", "okay",
                        "yeah", "going", "got", "right", "well", "really", "guys", "oh", "laughter", "little"]
                }
            }
        },
        { "$group": {
            "_id": "$words",
            "count": { "$sum": 1 },
        } }]
  ))


def convert_mongo_to_dictionary(mongo_cursor):
    dictionary = dict()
    for i in list(mongo_cursor):
        dictionary[i["_id"]] = i["count"]
    return dictionary


def convert_mongo_to_transcript(mongo_transcript):
    del mongo_transcript['_id']
    return Transcript(**mongo_transcript)
