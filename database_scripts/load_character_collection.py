from repositories import character_repository
from models.character_model import Character
import pandas as pd


def run():
    character_repository.drop()
    data = pd.read_excel(r'data/characters.xlsx')

    for index, row in data.iterrows():
        character = create_character_from_data_row(row)
        character_repository.insert_one(character)


def create_character_from_data_row(row):
    character = Character(row['name'].strip(),
                          row['actorName'].strip(),
                          row['actorNickname'].strip(),
                          int(row['age']),
                          [row['pronouns'].strip()],
                          row['creatureType'].strip(),
                          row['race'].strip(),
                          row['class'].strip())
    return character
