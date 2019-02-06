from flask import Blueprint, request, jsonify
from app.v1.models.offices.model import Offices

offices = Blueprint("offices", __name__, url_prefix="/v1")


@offices.route("/offices", methods=["POST"])
def createOffices():
    return jsonify(Offices(request.get_json(force=True)).creatOffice())


@offices.route("/offices", methods=["GET"])
def getAlloffices():
    return jsonify(Offices().getAllOffices())


@offices.route("/offices/<officeID>", methods=["GET"])
def getSpecificoffice(officeID):
    return jsonify(Offices().getSpecificOffice(officeID))
