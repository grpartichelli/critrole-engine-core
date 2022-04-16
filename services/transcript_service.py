from repositories import transcript_repository
import re
import matplotlib.pyplot as plt
import io

def search_transcripts(text, episode_number, actor_nickname):
    regx = re.compile(".*"+text+".*", re.IGNORECASE)
    par_dictionary = dict()
    par_dictionary['text'] = regx
    if episode_number: par_dictionary['episode_number'] = int(episode_number)
    if actor_nickname: par_dictionary['actor_nickname'] = actor_nickname
    transcripts = transcript_repository.find_all(par_dictionary)

    return transcripts


def search_per_episode(text, actor_nickname):
    regx = re.compile(".*"+text+".*", re.IGNORECASE)
    par_dictionary = dict()
    par_dictionary['text'] = regx
    if actor_nickname: par_dictionary['actor_nickname'] = actor_nickname
    transcripts = transcript_repository.count_string_per_episode(par_dictionary)
    x_vals,y_vals = zip(*[(float(i.episode_number),float(i.count)) for i in transcripts])
    plt.clf()
    plt.bar(x_vals,y_vals)
    plt.xlabel('Episodes')
    plt.ylabel('Occurrences')
    bytIO = io.BytesIO()
    plt.savefig(bytIO)
    bytIO.seek(0)
    return bytIO
