from flask import Blueprint, jsonify, request
from app.api.v2.models.offices.office_model import OfficeModel

office_view = Blueprint("office_view", __name__)


@office_view.route("", methods=["POST"])
def createOffice():
    response = OfficeModel(request.get_json(force=True)).createOffice()
    return jsonify(response), response["status"]


@office_view.route("", methods=["GET"])
def getAllOffices():
    response = OfficeModel(None).getAllOffices()
    return jsonify(response), response["status"]


@office_view.route("/<id>", methods=["GET", "DELETE"])
def getSpecificOffice(id):
    response = OfficeModel(None, id).getSpecificOffice()
    return jsonify(response), response["status"]


@office_view.route("/<id>", methods=["PATCH"])
def editSpecificOffice(id):
    response = OfficeModel(request.get_json(force=True)).editSpecificData(id)
    return jsonify(response), response["status"]


@office_view.route("/<id>", methods=["PATCH"])
def deleteSpecificOffice(id):
    response = PartyModel(None, id).deleteSpecificOffice()
    return jsonify(response), response["status"]


@office_view.route("/<id>/register", methods=["POST"])
def userRegisterToOffice(id):
    response = OfficeModel(request.get_json(force=True), id).userRegisterToOffice()
    return jsonify(response), response["status"]
