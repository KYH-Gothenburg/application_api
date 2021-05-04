from flask import Flask
from api.api import api_route
from data.db import db
from web.web import web_route


def register_extensions(app):
    db.init_app(app)


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///geo.db'
    app.register_blueprint(api_route, url_prefix='/api')
    app.register_blueprint(web_route)
    register_extensions(app)

    return app


app = create_app()


if __name__ == '__main__':
    app.run(port=5001)