from flask import Blueprint, jsonify, request
from app.api.v2.models.auth.auth_model import AuthModel

auth_view = Blueprint("auth_view", __name__)


@auth_view.route("/signup", methods=["POST"])
def registerUser():
    response = AuthModel(request.get_json(force=True)).registerUser()
    return jsonify(response), response["status"]


@auth_view.route("/login", methods=["POST"])
def loginUser():
    response = AuthModel(request.get_json(force=True)).loginUser()
    return jsonify(response), response["status"]
