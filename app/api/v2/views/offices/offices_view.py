from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app.api.v2.models.offices.office_model import OfficeModel

office_view = Blueprint("office_view", __name__)


@office_view.route("", methods=["POST"])
@jwt_required
def createOffice():
    response = OfficeModel(request.get_json(force=True)).createOffice()
    return jsonify(response), response["status"]


@office_view.route("", methods=["GET"])
@jwt_required
def getAllOffices():
    response = OfficeModel(None).getAllOffices()
    return jsonify(response), response["status"]


@office_view.route("/<id>", methods=["GET"])
@jwt_required
def getSpecificOffice(id):
    response = OfficeModel(None, id).getSpecificOffice()
    return jsonify(response), response["status"]


@office_view.route("/<id>", methods=["PATCH"])
@jwt_required
def editSpecificOffice(id):
    response = OfficeModel(request.get_json(force=True), id).editSpecificOffice()
    return jsonify(response), response["status"]


@office_view.route("/<id>", methods=["DELETE"])
@jwt_required
def deleteSpecificOffice(id):
    response = OfficeModel(None, id).deleteSpecificOffice()
    return jsonify(response), response["status"]


@office_view.route("/<id>/register", methods=["POST"])
@jwt_required
def userRegisterToOffice(id):
    response = OfficeModel(request.get_json(force=True), id).userRegisterToOffice()
    return jsonify(response), response["status"]


@office_view.route("/<id>/result", methods=["GET"])
@jwt_required
def officeResults(id):
    response = OfficeModel(None, id).officeResults()
    return jsonify(response), response["status"]
