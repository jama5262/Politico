from flask import Blueprint, jsonify, request
from app.api.v1.models.model import Models

view = Blueprint("view", __name__)


@view.route("/<tableName>", methods=["POST"])
def createData(tableName):
    response = Models(tableName, request.get_json(force=True)).createData()
    return jsonify(response), response["status"]


@view.route("/<tableName>", methods=["GET"])
def getAllData(tableName):
    response = Models(tableName, None).getAllData()
    return jsonify(response), response["status"]


@view.route("/<tableName>/<id>", methods=["GET", "DELETE"])
def getSpecificData(tableName, id):
    if request.method == "GET":
        response = Models(tableName, None).getSpecificData(id)
    else:
        response = Models(tableName, None).deleteSpecificData(id)
    return jsonify(response), response["status"]


@view.route("/<tableName>/<id>", methods=["PATCH"])
def editSpecificData(tableName, id):
    response = Models(tableName, request.get_json(force=True)).editSpecificData(id)
    return jsonify(response), response["status"]
