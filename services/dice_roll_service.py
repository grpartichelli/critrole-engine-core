from repositories import dice_roll_repository, filtered_transcript_repository
from datetime import timedelta
import collections, functools, operator
import matplotlib.pyplot as plt
import io
from wordcloud import WordCloud
import random


def get_average_by_character():
    return sorted(dice_roll_repository.average_by_character(), key=lambda x: x.average)


def most_used_words_by_roll(roll):
    par_dictionary = dict()
    par_dictionary["natural_value"] = int(roll)

    list_of_rolls = dice_roll_repository.find_all(par_dictionary)
    list_of_dicts = []
    list_of_rolls = random.sample(list_of_rolls, 25)

    for roll in list_of_rolls:
        before = roll.timestamp
        after = roll.timestamp + timedelta(seconds=5)
        list_of_dicts.append(filtered_transcript_repository.most_common_strings_by_timestamps(before, after))

    words_dict = dict(functools.reduce(operator.add,
                                       map(collections.Counter, list_of_dicts)))

    wordcloud = WordCloud(background_color='white', colormap="cool").generate_from_frequencies(words_dict)
    plt.clf()
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    bytIO = io.BytesIO()
    plt.savefig(bytIO)
    bytIO.seek(0)
    return bytIO
