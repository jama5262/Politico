from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.api.v2.models.users.user_model import Users

users_view = Blueprint("users_view", __name__)


@users_view.route("/<id>", methods=["GET"])
@jwt_required
def getSpecificUser(id):
    response = Users(id).getSpecificUser()
    return jsonify(response), response["status"]


@users_view.route("", methods=["GET"])
@jwt_required
def getAllUsers():
    response = Users().getAllUsers()
    return jsonify(response), response["status"]


@users_view.route("/candidate/<tableName>/<id>", methods=["GET"])
@jwt_required
def getSpecificCandidate(id, tableName):
    response = Users(id, tableName).getSpecificCandidate()
    return jsonify(response), response["status"]
