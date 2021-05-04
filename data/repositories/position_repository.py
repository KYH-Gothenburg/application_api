from data.db import db
from data.models.position import Position


def set_position(pos_data):
    timestamp = pos_data['timestamp']
    client_id = pos_data['client_id']
    lng = pos_data['position']['long']
    lat = pos_data['position']['lat']

    position = Position(timestamp=timestamp, client_id=client_id, longitude=lng, latitude=lat)
    db.session.add(position)
    db.session.commit()
    return position


def get_all_positions():
    return Position.query.all()
