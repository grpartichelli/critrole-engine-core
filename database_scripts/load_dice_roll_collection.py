from repositories import dice_roll_repository
from models.dice_roll_model import DiceRoll
from mongo import mongo_utils
import pandas as pd
import math
from datetime import datetime


def run():
    # dice_roll_repository.drop()
    data = pd.read_excel(r'data/all-rolls.xlsx', sheet_name='All Episodes')

    for index, row in data.iterrows():
        dice_roll = create_dice_roll_from_data_row(row)

        # dice_roll_repository.insert_one(dice_roll)


def create_dice_roll_from_data_row(row):
    # row['Time']
    dice_roll = DiceRoll(
        convert_to_natural_value(row['Natural Value']),
        row['Total Value'],
        convert_character_name(row['Character']),
        convert_to_was_enemy_killed(row['# Kills']),
        row['Episode'],
        mongo_utils.timestamp_to_date(row['Time']),
        row['Type of Roll'].strip())
    # dice_roll_repository.insert_one(dice_roll)
    return dice_roll


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
