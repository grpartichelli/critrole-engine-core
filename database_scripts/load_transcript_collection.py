from models.transcript_model import Transcript
from repositories import transcript_repository


def run():
    transcript_repository.drop()
