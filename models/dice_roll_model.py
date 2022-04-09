import json
from datetime import datetime
from mongo import mongo_utils


class DiceRoll:
    def __init__(self, natural_value, total_value, character_name, was_enemy_killed, episode_number, timestamp, type):
        self.natural_value = natural_value
        self.total_value = total_value
        self.character_name = character_name
        self.was_enemy_killed = was_enemy_killed
        self.episode_number = episode_number
        self.timestamp = timestamp
        self.type = type

    def to_json(self):
        return json.dumps(self, default=mongo_utils.json_default,
                          sort_keys=True, indent=4)
