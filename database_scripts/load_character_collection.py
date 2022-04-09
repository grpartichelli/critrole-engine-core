from repositories import character_repository
from models.character_model import Character
import pandas as pd

TOTAL_ROWS = 9


def run():
    character_repository.drop()
    data = pd.read_excel(r'data/characters.xlsx')

    i = 0
    last_percent = 0
    for index, row in data.iterrows():
        character = create_character_from_data_row(row)
        character_repository.insert_one(character)

        i += 1
        percent = 100 * i / TOTAL_ROWS
        if percent > last_percent:
            print("Loading Characters: " + str(math.ceil(percent)) + "%")
            last_percent = math.ceil(percent)


print("Finish Loading Characters")


def create_character_from_data_row(row):
    return Character(row['name'].strip(),
                     row['actorName'].strip(),
                     row['actorNickname'].strip(),
                     int(row['age']),
                     [row['pronouns'].strip()],
                     row['creatureType'].strip(),
                     row['race'].strip(),
                     row['class'].strip())
