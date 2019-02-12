from flask import Blueprint, jsonify, request
from app.api.v2.models.parties.parties_model import PartyModel

party_view = Blueprint("party_view", __name__)


@party_view.route("", methods=["POST"])
def createOffice():
    response = PartyModel(request.get_json(force=True)).createParty()
    return jsonify(response), response["status"]


@party_view.route("", methods=["GET"])
def getAllOffices():
    response = PartyModel(None).getAllParties()
    return jsonify(response), response["status"]


@party_view.route("/<id>", methods=["GET", "DELETE"])
def getSpecificParty(id):
    response = PartyModel(None, id).getAllParties()
    return jsonify(response), response["status"]


@party_view.route("/<id>", methods=["PATCH"])
def editSpecificParty(id):
    response = PartyModel(request.get_json(force=True), id).editSpecificParty()
    return jsonify(response), response["status"]


@party_view.route("/<id>", methods=["PATCH"])
def deleteSpecificParty(id):
    response = PartyModel(None, id).deleteSpecificParty()
    return jsonify(response), response["status"]