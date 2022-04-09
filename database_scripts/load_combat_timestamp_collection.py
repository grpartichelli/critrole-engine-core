import math
import time

import pandas as pd
from mongo import mongo_utils
from models.combat_timestamp_model import CombatTimestamp
from repositories import combat_timestamp_repository

TOTAL_ROWS = 139


def run():
    start = time.time()
    print("Loading Combat Times")
    combat_timestamp_repository.drop()
    data = pd.read_excel(r'data/combat-times.xlsx', sheet_name='WM Combat Times')

    i = 0
    last_percent = 0
    for index, row in data.iterrows():
        combat_timestamp = create_combat_timestamp_from_data_row(row)
        combat_timestamp_repository.insert_one(combat_timestamp)

        i += 1
        percent = 100 * i / TOTAL_ROWS
        if percent > last_percent:
            print("Loading Combat Timestamps: " + str(math.ceil(percent)) + "%")
            last_percent = math.ceil(percent)
    print("Finish Loading Combat Timestamps")
    end = time.time()
    print("Execution Time: " + str(round(end - start, 2)) + " seconds")


def create_combat_timestamp_from_data_row(row):
    return CombatTimestamp(
        row['Encounter'].strip(),
        convert_to_episode_number(row['Episode']),
        mongo_utils.timestamp_to_date(row['Start Time']),
        mongo_utils.timestamp_to_date(row['End Time']),
        int(row['Rounds'])
    )


def convert_to_episode_number(value):
    if isinstance(value, str):
        value.strip()
        value = value.removeprefix("C2E")
        return int(value)
    return None
