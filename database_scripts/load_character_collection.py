from repositories import character_repository
from models.character_model import Character


def run():
    character_repository.drop()
    character = Character('Name', 'ActorName', 'ActorNickname', 20, 'he/him', 'CreatureType', 'Race2', 'DndClass')

    print(character)

    # character_repository.insert_one(character)
