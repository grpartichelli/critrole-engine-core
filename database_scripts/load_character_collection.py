from models.character_model import Character
from repositories import character_repository


def run():
    character = Character('Name', 'ActorName', 'ActorNickname', 20, 'he/him', 'CreatureType', 'Race', 'DndClass')
    character_repository.insert_one(character)
