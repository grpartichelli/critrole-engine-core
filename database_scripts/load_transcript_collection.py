from models.transcript_model import Transcript
from repositories import transcript_repository
from bs4 import BeautifulSoup
from mongo import mongo_utils
from datetime import time
import os


def run():
    transcript_repository.drop()
    for file in os.listdir('data/transcripts/'):
        f = open(f'data/transcripts/{os.fsdecode(file)}', 'r')
        soup = BeautifulSoup(f.read(), 'html.parser')

        episode_number = calculate_episode_number(soup)
        actor_nickname = ''
        for tag in soup.find_all(['dt', 'dd']):
            if tag.name == "dt":
                actor_nickname = calculate_actor_nickname(tag)
            if tag.name == "dd":
                transcript = create_transcript_from_tag(tag, episode_number, actor_nickname)
                transcript_repository.insert_one(transcript)


def create_transcript_from_tag(tag, episode_number, actor_nickname):
    transcript = Transcript(
        actor_nickname,
        calculate_timestamp(tag),
        calculate_text(tag),
        calculate_youtube_link(tag),
        episode_number
    )
    return transcript


def calculate_text(tag):
    return tag.text.replace('→', '').strip()


def calculate_timestamp(tag):
    times = tag.get('id').replace('l', '').replace('h', '-').replace('m', '-').replace('s', '').split('-')
    timestamp = time(int(times[0]), int(times[1]), int(times[2]), 0)
    return mongo_utils.timestamp_to_date(timestamp)


def calculate_youtube_link(tag):
    return tag.a.get('href')


def calculate_actor_nickname(tag):
    return tag.strong.string


def calculate_episode_number(soup):
    data = soup.main.h3.string
    return int(data.split().pop())
