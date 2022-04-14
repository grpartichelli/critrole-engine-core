from repositories import character_repository


def get_character(name, actor_name, actor_nickname, age, pronouns, creature_type, race, dnd_class):
    par_dictionary = dict()
    if name : par_dictionary['name'] = name
    if actor_name : par_dictionary['actor_name'] = actor_name
    if actor_nickname : par_dictionary['actor_nickname'] = actor_nickname
    if age : par_dictionary['age'] = age
    if pronouns : par_dictionary['pronouns'] = pronouns
    if creature_type : par_dictionary['creature_type'] = creature_type
    if race : par_dictionary['race'] = race
    if dnd_class : par_dictionary['dnd_class'] = dnd_class
    character = character_repository.find_all(par_dictionary)

    return [character]
