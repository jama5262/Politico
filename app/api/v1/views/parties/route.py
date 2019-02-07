from flask import Blueprint, jsonify, request
from app.api.v1.models.parties.model import Parties

parties = Blueprint("parties", __name__, url_prefix="/api/v1")


@parties.route("/parties", methods=["POST"])
def createParty():
    response = Parties(request.get_json(force=True)).createParty()
    return jsonify(response), response["status"]


@parties.route("/parties", methods=["GET"])
def getAllParties():
    response = Parties().getAllParties()
    return jsonify(response), response["status"]


@parties.route("/parties/<partyID>", methods=["GET"])
def getSpecificParty(partyID):
    response = Parties().getSpecificParty(partyID)
    return jsonify(response), response["status"]


@parties.route("/parties/<partyID>", methods=["PATCH"])
def editSpecificParty(partyID):
    response = Parties(request.get_json(force=True)).editSpecificParty(partyID)
    return jsonify(response), response["status"]


@parties.route("/parties/<partyID>", methods=["DELETE"])
def deleteSpecificParty(partyID):
    response = Parties().deleteSpecificParty(partyID)
    return jsonify(response), response["status"]
