from flask import Blueprint, request, jsonify

from controller.position_controller import set_position, get_all_positions

api_route = Blueprint('api', __name__)
API_VERSION = '/v1.0'


@api_route.route(f'{API_VERSION}/positions', methods=['POST'])
def post_position():
    in_data = request.get_json()
    position = set_position(in_data)
    return jsonify(position)


@api_route.route(f'{API_VERSION}/positions', methods=['GET'])
def get_position():
    positions = get_all_positions()
    return jsonify(positions)