from flask import Blueprint, jsonify, request
from app.api.v2.models.auth.auth_model import AuthModel
from flask_jwt_extended import create_access_token, jwt_required

auth_view = Blueprint("auth_view", __name__)


def createToken(email, isAdmin="False"):
    return create_access_token(identity={
        "email": email,
        "role": isAdmin
    })


@auth_view.route("/signup", methods=["POST"])
def registerUser():
    response = AuthModel(request.get_json(force=True)).registerUser()
    if "data" in response:
        token = createToken(response["data"]["user"]["email"])
        response["data"]["token"] = token
    return jsonify(response), response["status"]


@auth_view.route("/login", methods=["POST"])
def loginUser():
    response = AuthModel(request.get_json(force=True)).loginUser()
    if "data" in response:
        token = createToken(response["data"]["user"]["email"], str(response["data"]["user"]["is_admin"]))
        response["data"]["token"] = token
        print(response["data"]["user"]["is_admin"])
    return jsonify(response), response["status"]


@auth_view.route("/<email>", methods=["GET"])
def getSpecificUser(email):
    response = AuthModel(None, email, createToken(email)).getSpecificUser()
    return jsonify(response), response["status"]
