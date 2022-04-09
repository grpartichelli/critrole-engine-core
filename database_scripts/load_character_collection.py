from repositories import character_repository
from models.character_model import Character
import pandas as pd


def run():
    character_repository.drop()
    character = Character('Name', 'ActorName', 'ActorNickname', 20, 'he/him', 'CreatureType', 'Race2', 'DndClass')
    data = pd.read_excel(r'data/characters.xlsx')
    print(data)
    print(character)

    # character_repository.insert_one(character)
