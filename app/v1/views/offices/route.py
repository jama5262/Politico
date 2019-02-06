from flask import Blueprint, request, jsonify
from app.v1.models.offices.model import Offices

offices = Blueprint("offices", __name__, url_prefix="/v1")


@offices.route("/offices", methods=["POST"])
def createOffices():
    return jsonify(Offices(request.get_json(force=True)).creatOffice())


@offices.route("/offices", methods=["GET"])
def getAlloffices():
    return "Your are tring to GET all offices"


@offices.route("/offices/<officeID>", methods=["GET"])
def getSpecificoffice(officeID):
    return "Your are tring to GET office with id "+officeID


@offices.route("/offices/<officeID>", methods=["PUT"])
def editSpecificoffice(officeID):
    return "Your are tring to EDIT office with id "+officeID


@offices.route("/offices/<officeID>", methods=["DELETE"])
def deleteSpecificoffice(officeID):
    return "Your are tring to DELETE office with id "+officeID
