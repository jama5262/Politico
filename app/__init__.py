from flask import Flask
from instance.config import appConfig
from app.v1.views.parties.route import parties
from app.v1.views.offices.route import offices


def createApp(configName):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(appConfig[configName])
    app.register_blueprint(parties)
    app.register_blueprint(offices)
    app.config.from_pyfile('config.py')
    return app
