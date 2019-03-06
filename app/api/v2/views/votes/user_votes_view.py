from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app.api.v2.models.votes.user_votes_model import VoteModel

user_votes_view = Blueprint("user_votes_view", __name__)


@user_votes_view.route("", methods=["POST"])
@jwt_required
def createVote():
    response = VoteModel(request.get_json(force=True)).createVote()
    return jsonify(response), response["status"]


@user_votes_view.route("", methods=["GET"])
@jwt_required
def getAllVotes():
    response = VoteModel(None).getAllVotes()
    return jsonify(response), response["status"]


@user_votes_view.route("/<id>", methods=["GET"])
@jwt_required
def getSpecificVote(id):
    response = VoteModel(None, id).getSpecificVote()
    return jsonify(response), response["status"]
