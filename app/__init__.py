from flask import Flask, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from instance.config import appConfig
from app.api.v1.views.view import view
from app.api.v2.views.offices.offices_view import office_view
from app.api.v2.views.parties.parties_view import party_view
from app.api.v2.views.auth.auth_view import auth_view
from app.api.v2.views.votes.user_votes_view import user_votes_view
from app.api.v2.views.petitions.petitions_view import petition_view


def pageNotFound(error):
    return jsonify({
        "status": 404,
        "error": "404 (Not Found), The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again."
    }), 404


def badRequest(error):
    return jsonify({
        "status": 400,
        "error": "400 (Bad Request), Please make sure you have valid syntax"
    }), 400


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
    CORS(app)
    app.config.from_object(appConfig[configName])
    app.config.from_pyfile('config.py')
    app.config['JWT_SECRET_KEY'] = 'secret_key'
    jwt = JWTManager(app)
    app.register_error_handler(404, pageNotFound)
    app.register_error_handler(405, methodNotAllowed)
    app.register_error_handler(400, badRequest)
    app.register_error_handler(500, serverError)
    app.register_blueprint(view, url_prefix="/api/v1")
    app.register_blueprint(office_view, url_prefix="/api/v2/offices")
    app.register_blueprint(party_view, url_prefix="/api/v2/parties")
    app.register_blueprint(auth_view, url_prefix="/api/v2/auth")
    app.register_blueprint(user_votes_view, url_prefix="/api/v2/votes")
    app.register_blueprint(petition_view, url_prefix="/api/v2/petitions")
    return app
