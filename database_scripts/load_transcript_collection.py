from models.transcript_model import Transcript
from repositories import transcript_repository
from bs4 import BeautifulSoup
import os


def run():
    transcript_repository.drop()

    i = 0

    for file in os.listdir('data/transcripts/'):
        f = open(f'data/transcripts/{os.fsdecode(file)}', 'r')
        soup = BeautifulSoup(f.read(), 'html.parser')
        i += 1
        if i == 3:
            break
