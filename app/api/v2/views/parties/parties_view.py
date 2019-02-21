from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.api.v2.models.parties.parties_model import PartyModel

party_view = Blueprint("party_view", __name__)


def checkIfAuthorized():
    user = get_jwt_identity()
    if user["role"] == "False":
        return False
    return True


@party_view.route("", methods=["POST"])
@jwt_required
def createParty():
    if checkIfAuthorized() is False:
        return jsonify({
            "error": "You are not authorized to create a party",
            "status": 403
        }), 403
    response = PartyModel(request.get_json(force=True)).createParty()
    return jsonify(response), response["status"]


@party_view.route("", methods=["GET"])
@jwt_required
def getAllParties():
    response = PartyModel(None).getAllParties()
    return jsonify(response), response["status"]


@party_view.route("/<id>", methods=["GET"])
@jwt_required
def getSpecificParty(id):
    response = PartyModel(None, id).getSpecificParty()
    return jsonify(response), response["status"]


@party_view.route("/<id>", methods=["PATCH"])
@jwt_required
def editSpecificParty(id):
    if checkIfAuthorized() is False:
        return jsonify({
            "error": "You are not authorized to edit a party",
            "status": 403
        }), 403
    response = PartyModel(request.get_json(force=True), id).editSpecificParty()
    return jsonify(response), response["status"]


@party_view.route("/<id>", methods=["DELETE"])
@jwt_required
def deleteSpecificParty(id):
    if checkIfAuthorized() is False:
        return jsonify({
            "error": "You are not authorized to delete a party",
            "status": 403
        }), 403
    response = PartyModel(None, id).deleteSpecificParty()
    return jsonify(response), response["status"]
