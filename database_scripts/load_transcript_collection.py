from models.transcript_model import Transcript
from repositories import transcript_repository
from bs4 import BeautifulSoup
from mongo import mongo_utils
import os


def run():
    transcript_repository.drop()

    i = 0

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
                # print(mongo_utils.to_json(transcript))
        i += 1
        if i == 1:
            break


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
    print(tag.get('id'))
    return tag.id


def calculate_youtube_link(tag):
    return tag.a.get('href')


def calculate_actor_nickname(tag):
    return tag.strong.string


def calculate_episode_number(soup):
    data = soup.main.h3.string
    return int(data.split().pop())
