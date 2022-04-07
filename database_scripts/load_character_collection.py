from repositories import character_repository
from models.character_model import Character


def run():
    character_repository.drop()
    character = Character('Name', 'ActorName', 'ActorNickname', 20, 'he/him', 'CreatureType', 'Race2', 'DndClass')
    character_repository.insert_one(character)
    character = character_repository.find_one({'name': 'Name'})
    print(character.actor_nickname)
