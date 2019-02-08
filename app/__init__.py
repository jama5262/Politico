from flask import Flask, jsonify
from instance.config import appConfig
from app.api.v1.views.parties.route import parties
from app.api.v1.views.offices.route import offices


def pageNotFound(error):
    return jsonify({
        "status": 404,
        "error": str(error)
    }), 404


def methodNotAllowed(error):
    return jsonify({
      "status": 405,
      "error": str(error)
    })


def serverError(error):
    return jsonify({
      "status": 500,
      "error": str(error)
    })


def createApp(configName):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(appConfig[configName])
    app.register_blueprint(parties, url_prefix="/api/v1")
    app.register_blueprint(offices, url_prefix="/api/v1")
    app.register_error_handler(404, pageNotFound)
    app.register_error_handler(405, methodNotAllowed)
    app.register_error_handler(500, serverError)
    app.config.from_pyfile('config.py')
    return app
