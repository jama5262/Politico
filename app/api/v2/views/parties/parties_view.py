from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app.api.v2.models.parties.parties_model import PartyModel

party_view = Blueprint("party_view", __name__)


@party_view.route("", methods=["POST"])
@jwt_required
def createParty():
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
    response = PartyModel(request.get_json(force=True), id).editSpecificParty()
    return jsonify(response), response["status"]


@party_view.route("/<id>", methods=["DELETE"])
@jwt_required
def deleteSpecificParty(id):
    response = PartyModel(None, id).deleteSpecificParty()
    return jsonify(response), response["status"]
