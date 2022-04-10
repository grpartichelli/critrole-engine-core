from repositories import character_repository, dice_roll_repository, combat_timestamp_repository, transcript_repository, \
    filtered_transcript_repository


def get_one_of_each():
    character = character_repository.find_one({})
    dice_roll = dice_roll_repository.find_one({})
    combat_timestamp = combat_timestamp_repository.find_one({})
    transcript = transcript_repository.find_one({})
    filtered_transcript = filtered_transcript_repository.find_one({})

    return [character, dice_roll, combat_timestamp, transcript, filtered_transcript]
