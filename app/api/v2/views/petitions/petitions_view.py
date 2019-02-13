from flask import Blueprint, jsonify, request
from app.api.v2.models.petitions.petitions_model import PetitionModel

petition_view = Blueprint("petition_view", __name__)


@petition_view.route("", methods=["POST"])
def createPetition():
    response = PetitionModel(request.get_json(force=True)).createPetition()
    return jsonify(response), response["status"]


@petition_view.route("", methods=["GET"])
def getAllPetitions():
    response = PetitionModel(None).getAllPetitions()
    return jsonify(response), response["status"]
