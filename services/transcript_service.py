from repositories import transcript_repository, character_repository, filtered_transcript_repository, \
    combat_timestamp_repository
import re
import matplotlib.pyplot as plt
import io
from wordcloud import WordCloud
import collections, functools, operator


def search_transcripts(text, episode_number, actor_nickname):
    regx = re.compile(".*" + text + ".*", re.IGNORECASE)
    par_dictionary = dict()
    par_dictionary['text'] = regx
    if episode_number: par_dictionary['episode_number'] = int(episode_number)
    if actor_nickname: par_dictionary['actor_nickname'] = actor_nickname
    transcripts = transcript_repository.find_all(par_dictionary)

    return transcripts


def search_per_episode(text, actor_nickname):
    regx = re.compile(".*" + text + ".*", re.IGNORECASE)
    par_dictionary = dict()
    par_dictionary['text'] = regx
    if actor_nickname: par_dictionary['actor_nickname'] = actor_nickname
    transcripts = transcript_repository.count_string_per_episode(par_dictionary)
    x_vals, y_vals = zip(*[(float(i.episode_number), float(i.count)) for i in transcripts])
    plt.clf()
    plt.bar(x_vals, y_vals)
    plt.xlabel('Episodes')
    plt.ylabel('Times word was used')
    bytIO = io.BytesIO()
    plt.savefig(bytIO, dpi=100)
    bytIO.seek(0)
    return bytIO


def character_interactions(actor_one, actor_two):
    characters_one = character_repository.find_all({"actor_nickname": actor_one})
    characters_two = character_repository.find_all({"actor_nickname": actor_two})

    two_to_one = 0
    one_to_two = 0

    for character in characters_one:
        for name in character.name.split(" "):
            regx = re.compile(".*" + name + ".*", re.IGNORECASE)
            par_dictionary = dict()
            par_dictionary['text'] = regx
            par_dictionary['actor_nickname'] = actor_two
            two_to_one = two_to_one + transcript_repository.count_string(par_dictionary)

    for character in characters_two:
        for name in character.name.split(" "):
            regx = re.compile(".*" + name + ".*", re.IGNORECASE)
            par_dictionary = dict()
            par_dictionary['text'] = regx
            par_dictionary['actor_nickname'] = actor_one
            one_to_two = one_to_two + transcript_repository.count_string(par_dictionary)

    x_vals = [actor_one + " about " + actor_two, actor_two + " about " + actor_one]
    y_vals = [one_to_two, two_to_one]
    plt.clf()
    plt.bar(x_vals, y_vals)
    plt.ylabel('Times referenced other character')
    bytIO = io.BytesIO()
    plt.savefig(bytIO, dpi=100)
    bytIO.seek(0)
    return bytIO


def wordcloud(actor_nickname, episode_number):
    par_dictionary = dict()
    if actor_nickname: par_dictionary['actor_nickname'] = actor_nickname
    if episode_number: par_dictionary['episode_number'] = int(episode_number)

    words_dict = filtered_transcript_repository.most_common_strings(par_dictionary)
    wordcloud = WordCloud(width=1920, height=1080, background_color='white', colormap="cool").generate_from_frequencies(
        words_dict)
    plt.clf()
    plt.figure(figsize=(20, 8))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    bytIO = io.BytesIO()
    plt.savefig(bytIO, bbox_inches='tight')
    bytIO.seek(0)
    return bytIO


def rank_actors_by_words(words):
    list_words = words.split(',')
    result = dict(sorted(transcript_repository.rank_by_words(list_words).items(), key=lambda x: x[1], reverse=False))

    x_vals = list(result.keys())
    y_vals = list(result.values())

    plt.clf()
    plt.barh(x_vals, y_vals)
    plt.xlabel('Times the words were used')
    bytIO = io.BytesIO()
    plt.savefig(bytIO, dpi=100)
    bytIO.seek(0)
    return bytIO


def get_transcripts_in_combat(episode_number):
    list_of_combats = combat_timestamp_repository.find_all({"episode_number": int(episode_number)})
    transcripts_in_combat = []

    for combat in list_of_combats:
        before = combat.start_timestamp
        after = combat.end_timestamp
        transcripts_in_combat.append(transcript_repository.find_all(
            {"timestamp": {"$gte": before, "$lt": after}, "episode_number": int(episode_number)}))

    return transcripts_in_combat
