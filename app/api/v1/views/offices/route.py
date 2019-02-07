from flask import Blueprint, request, jsonify
from app.api.v1.models.offices.model import Offices

offices = Blueprint("offices", __name__, url_prefix="/api/v1")


@offices.route("/offices", methods=["POST"])
def createOffices():
    response = Offices(request.get_json(force=True)).creatOffice()
    return jsonify(response), response["status"]


@offices.route("/offices", methods=["GET"])
def getAlloffices():
    response = Offices().getAllOffices()
    return jsonify(response), response["status"]


@offices.route("/offices/<officeID>", methods=["GET"])
def getSpecificoffice(officeID):
    response = Offices().getSpecificOffice(officeID)
    return jsonify(response), response["status"]
