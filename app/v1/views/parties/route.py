from flask import Blueprint, jsonify, request
from app.v1.models.parties.model import Parties

parties = Blueprint("parties", __name__, url_prefix="/v1")


@parties.route("/parties", methods=["POST"])
def createParty():
    obj = Parties(request.get_json(force=True))
    return jsonify(obj.createParty())


@parties.route("/parties", methods=["GET"])
def getAllParties():
    return jsonify(Parties().getAllParties())


@parties.route("/parties/<partyID>", methods=["GET"])
def getSpecificParty(partyID):
    return jsonify(Parties().getSpecificParty(partyID))


@parties.route("/parties/<partyID>", methods=["PATCH"])
def editSpecificParty(partyID):
    return jsonify(Parties(request.get_json(force=True)).editSpecificParty(partyID))


@parties.route("/parties/<partyID>", methods=["DELETE"])
def deleteSpecificParty(partyID):
    return "Your are tring to DELETE party with id "+partyID
