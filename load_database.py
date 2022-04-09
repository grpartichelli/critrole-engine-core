from database_scripts import load_character_collection, load_dice_roll_collection, load_combat_timestamp_collection, \
    load_transcript_collection


def load_database():
    load_character_collection.run()
    load_combat_timestamp_collection.run()
    load_transcript_collection.run()
    load_dice_roll_collection.run()


load_database()
