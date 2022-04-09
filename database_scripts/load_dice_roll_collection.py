import math
import time
import pandas as pd

from models.dice_roll_model import DiceRoll
from mongo import mongo_utils
from repositories import dice_roll_repository

TOTAL_ROWS = 15364


def run():
    start = time.time()
    print("Loading Dice Rolls")
    dice_roll_repository.drop()
    data = pd.read_excel(r'data/all-rolls.xlsx', sheet_name='All Episodes')

    i = 0
    last_percent = 0
    for index, row in data.iterrows():
        dice_roll = create_dice_roll_from_data_row(row)
        dice_roll_repository.insert_one(dice_roll)

        i += 1
        percent = 100 * i / TOTAL_ROWS
        if percent > last_percent:
            print("Loading Dice Rolls: " + str(math.ceil(percent)) + "%")
            last_percent = math.ceil(percent)

    print("Finish Loading Dice Rolls")
    end = time.time()
    print("Execution Time: " + str(round(end - start, 2)) + " seconds")


def create_dice_roll_from_data_row(row):
    return DiceRoll(
        convert_to_natural_value(row['Natural Value']),
        convert_to_total_value(row['Total Value']),
        convert_character_name(row['Character']),
        convert_to_was_enemy_killed(row['# Kills']),
        convert_to_episode_number(row['Episode']),
        mongo_utils.timestamp_to_date(row['Time']),
        row['Type of Roll'].strip())


def convert_to_episode_number(value):
    if isinstance(value, str):
        value.strip()
        value = value.removeprefix("C2E")
        return int(value)
    return None


def convert_to_total_value(value):
    if isinstance(value, float) or isinstance(value, int):
        return value
    if isinstance(value, str):
        value.strip()
        if value.startswith("Nat"):
            return int(value.removeprefix("Nat"))
    return None


def convert_to_natural_value(value):
    if isinstance(value, float) or isinstance(value, int):
        return value
    return None


def convert_to_was_enemy_killed(value):
    if isinstance(value, int) or isinstance(value, float):
        return not math.isnan(value)
    return False


def convert_character_name(value):
    value.strip()
    if value == "Jester":
        return "Jester Lavorre"
    if value == "Molly":
        return "Mollymauk Tealeaf"
    if value == "Caduceus":
        return "Caduceus Clay"
    if value == "Yasha":
        return "Yasha Nydoorin"
    if value == "Caleb":
        return "Caleb Widogast"
    if value == "Beau":
        return "Beauregard Lionett"
    return value
