from models.transcript_model import Transcript
from repositories import transcript_repository, filtered_transcript_repository
from bs4 import BeautifulSoup
from mongo import mongo_utils
import datetime
import os
import math
import time

FILE_COUNT = 141


def run():
    start = time.time()
    print("Loading Transcripts")
    transcript_repository.drop()
    # filtered_transcript_repository.drop()
    filter_words = load_common_words()

    i = 0
    last_percent = 0
    for file in os.listdir('data/transcripts/'):
        transcripts = []
        f = open(f'data/transcripts/{os.fsdecode(file)}', 'r', encoding='utf8')
        print(os.fsdecode(file))
        soup = BeautifulSoup(f.read(), 'html.parser')

        episode_number = calculate_episode_number(soup)
        actor_nickname = ''
        for tag in soup.find_all(['dt', 'dd']):
            if tag.name == "dt":
                actor_nickname = calculate_actor_nickname(tag)
            if tag.name == "dd":
                transcript = create_transcript_from_tag(tag, episode_number, actor_nickname)
                transcript_repository.insert_one(transcript)

                transcript.text = filter_text(transcript.text, filter_words)
                filtered_transcript_repository.insert_one(transcript)
        transcript_repository.insert_many(transcripts)
        arr = []
        for t in transcripts:
            t.text = filter_text(t.text, filter_words)
            arr.append(t)
        filtered_transcript_repository.insert_many(transcripts)
        i += 1
        percent = 100 * i / FILE_COUNT
        if percent > last_percent:
            print("Loading Transcripts: " + str(math.ceil(percent)) + "%")
            last_percent = math.ceil(percent)

    print("Finish Loading Transcripts")
    end = time.time()
    print("Execution Time: " + str(round(end - start, 2)) + " seconds")


def create_transcript_from_tag(tag, episode_number, actor_nickname):
    transcript = Transcript(
        actor_nickname,
        calculate_timestamp(tag),
        calculate_text(tag),
        calculate_youtube_link(tag),
        episode_number
    )
    return transcript


def filter_text(text, filter_words):
    filtered = [word for word in text.split(" ") if word.lower() not in filter_words]
    return " ".join(filtered)


def load_common_words():
    f = open('data/100-oxford-common-words.txt')
    words = set()
    for word in f:
        words.add(word.strip())

    f2 = open('data/200-selected-words.txt')
    for word in f2:
        words.add(word.strip())
    return words


def calculate_text(tag):
    return tag.text.replace('→', '').strip()


def calculate_timestamp(tag):
    times = tag.get('id').replace('l', '').replace('h', '-').replace('m', '-').replace('s', '').split('-')
    timestamp = datetime.time(int(times[0]), int(times[1]), int(times[2]), 0)
    return mongo_utils.timestamp_to_date(timestamp)


def calculate_youtube_link(tag):
    return tag.a.get('href')


def calculate_actor_nickname(tag):
    return tag.strong.string


def calculate_episode_number(soup):
    data = soup.main.h3.string
    return int(data.split().pop())
