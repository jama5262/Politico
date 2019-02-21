from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.api.v2.models.offices.office_model import OfficeModel

office_view = Blueprint("office_view", __name__)


def checkIfAuthorized():
    user = get_jwt_identity()
    if user["role"] == "False":
        return False
    return True


@office_view.route("", methods=["POST"])
@jwt_required
def createOffice():
    if checkIfAuthorized() is False:
        return jsonify({
            "error": "You are not authorized to create an office",
            "status": 403
        }), 403
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
    if checkIfAuthorized() is False:
        return jsonify({
            "error": "You are not authorized to edit an office",
            "status": 403
        }), 403
    response = OfficeModel(request.get_json(force=True), id).editSpecificOffice()
    return jsonify(response), response["status"]


@office_view.route("/<id>", methods=["DELETE"])
@jwt_required
def deleteSpecificOffice(id):
    if checkIfAuthorized() is False:
        return jsonify({
            "error": "You are not authorized to delete an office",
            "status": 403
        }), 403
    response = OfficeModel(None, id).deleteSpecificOffice()
    return jsonify(response), response["status"]


@office_view.route("/register", methods=["POST"])
@jwt_required
def userRegisterToOffice():
    if checkIfAuthorized() is False:
        return jsonify({
            "error": "You are not authorized to register a user to office",
            "status": 403
        }), 403
    response = OfficeModel(request.get_json(force=True)).userRegisterToOffice()
    return jsonify(response), response["status"]


@office_view.route("/<id>/result", methods=["GET"])
@jwt_required
def officeResults(id):
    response = OfficeModel(None, id).officeResults()
    return jsonify(response), response["status"]
