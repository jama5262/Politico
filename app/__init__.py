from flask import Flask, jsonify
from instance.config import appConfig
from app.api.v1.views.view import view


def pageNotFound(error):
    return jsonify({
        "status": 404,
        "error": "404 (Not Found), The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again."
    }), 404


def methodNotAllowed(error):
    return jsonify({
      "status": 405,
      "error": "405 (Method Not Allowed), The method is not allowed for the requested URL"
    })


def serverError(error):
    return jsonify({
      "status": 500,
      "error": "500 (Internal Server Error), There was a server error, please try agin later"
    })


def createApp(configName):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(appConfig[configName])
    app.register_blueprint(view, url_prefix="/api/v1")
    app.register_error_handler(404, pageNotFound)
    app.register_error_handler(405, methodNotAllowed)
    app.register_error_handler(500, serverError)
    app.config.from_pyfile('config.py')
    return app
