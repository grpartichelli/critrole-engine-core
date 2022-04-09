from database_scripts import load_character_collection, load_dice_roll_collection, load_combat_timestamp_collection, \
    load_transcript_collection


def load_database():
    text = input(
        'Are you SURE you want to run this script?\n It will drop all tables and it may take hours to run.\n If you are sure type YES I\'M SURE\n')

    if text == "YES I'M SURE":
        load_character_collection.run()
        load_combat_timestamp_collection.run()
        load_transcript_collection.run()
        load_dice_roll_collection.run()


load_database()
