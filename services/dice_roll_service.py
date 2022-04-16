from repositories import dice_roll_repository


def get_average_by_character():
    return sorted(dice_roll_repository.average_by_character(),key=lambda x: x.average)