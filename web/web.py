from flask import Blueprint, render_template

from controller.position_controller import get_all_positions

web_route = Blueprint('web', __name__, template_folder='templates')


@web_route.route('/')
def index():
    positions = get_all_positions()
    return render_template('index.html', positions=positions)