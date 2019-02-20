from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app.api.v2.models.petitions.petitions_model import PetitionModel

petition_view = Blueprint("petition_view", __name__)


@petition_view.route("", methods=["POST"])
@jwt_required
def createPetition():
    response = PetitionModel(request.get_json(force=True)).createPetition()
    return jsonify(response), response["status"]


@petition_view.route("", methods=["GET"])
@jwt_required
def getAllPetitions():
    response = PetitionModel(None).getAllPetitions()
    return jsonify(response), response["status"]
