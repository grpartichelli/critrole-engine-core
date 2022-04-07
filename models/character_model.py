import json


class Character:
    def __init__(self, name, actor_name, actor_nickname, age, pronouns, creature_type, race, dnd_class):
        self.name = name
        self.actor_name = actor_name
        self.actor_nickname = actor_nickname
        self.age = age
        self.pronouns = pronouns
        self.creature_type = creature_type
        self.race = race
        self.dnd_class = dnd_class

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
