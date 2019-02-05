from flask import Blueprint, jsonify, request
from app.v1.models.parties.model import Parties

parties = Blueprint("parties", __name__, url_prefix="/v1")


@parties.route("/parties", methods=["POST"])
def createParty():
    obj = Parties(request.get_json())
    return jsonify(obj.createParty())


@parties.route("/parties", methods=["GET"])
def getAllParties():
    return "Your are tring to GET all party"


@parties.route("/parties/<partyID>", methods=["GET"])
def getSpecificParty(partyID):
    return "Your are tring to GET party with id "+partyID


@parties.route("/parties/<partyID>", methods=["PUT"])
def editSpecificParty(partyID):
    return "Your are tring to EDIT party with id "+partyID


@parties.route("/parties/<partyID>", methods=["DELETE"])
def deleteSpecificParty(partyID):
    return "Your are tring to DELETE party with id "+partyID
