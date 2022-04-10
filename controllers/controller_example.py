from flask import Blueprint
from flask_cors import cross_origin

from mongo import mongo_utils
from services import service_example

app_example = Blueprint('app_example', __name__)


@app_example.route('/api/test')
@cross_origin()
def test():
    return mongo_utils.to_json(service_example.get_one_of_each())
