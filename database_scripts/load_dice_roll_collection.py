from repositories import dice_roll_repository
from models.dice_roll_model import DiceRoll
from mongo import mongo_utils
import pandas as pd
from datetime import datetime


def run():
    # dice_roll_repository.drop()
    data = pd.read_excel(r'data/all-rolls.xlsx', sheet_name='All Episodes')

    for index, row in data.iterrows():
        dice_roll = create_dice_roll_from_data_row(row)
        break
        dice_roll_repository.insert_one(dice_roll)


def create_dice_roll_from_data_row(row):
    # row['Time']
    dice_roll = DiceRoll(
        row['Natural Value'],
        row['Total Value'],
        row['Character'],
        row['# Kills'],
        row['Episode'],
        mongo_utils.timestamp_to_date(row['Time']),
        row['Type of Roll'])
    # dice_roll_repository.insert_one(dice_roll)
    return dice_roll

def convert_kills_to_was