from flask import Blueprint, jsonify, request
from app.api.v2.models.auth.auth_model import AuthModel

auth_view = Blueprint("auth_view", __name__)


@auth_view.route("/signup", methods=["POST"])
def createUser():
    response = AuthModel(request.get_json(force=True)).createUser()
    return jsonify(response), response["status"]
