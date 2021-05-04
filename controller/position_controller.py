from data.repositories import position_repository


def set_position(pos_data):
    return position_repository.set_position(pos_data).to_dict()


def get_all_positions():
    return [position.to_dict() for position in position_repository.get_all_positions()]