import json

from flask import Blueprint, jsonify, request
from app.model import Question, Answers, User, Params, Result, Profiles
from app.extensions import db
from app.utils import authenticate

question = Blueprint('questions', __name__)


@question.route('/questions')
def get_questions():
    message = {
        "status": "error",
        "message": "Questions not found",
        "data": {}
    }
    response = [{'id': row.id, 'text': row.text} for row in Question.query.all()]
    if response:
        message["status"] = "success"
        message["message"] = "Questions loaded successfully"
        message["data"] = response
        return jsonify(message), 200

    return jsonify(message), 404


@question.route('/result')
@authenticate
def get_result(user_id):
    message = {
        "status": "error",
        "message": "User doesn't exist",
        "data": {}
    }

    result = Result.get_results(user_id)

    if result:
        message["status"] = "success"
        message["message"] = "Result found"
        message["data"] = json.loads(result)
        return jsonify(message), 200

    return jsonify(message), 404


@question.route('/answer', methods=['POST'])
@authenticate
def save_answers(user_id):
    message = {
        "status": "error",
        "message": "An error occurred",
    }
    data = request.get_json(cache=False)

    if isinstance(user_id, str):
        message["message"] = user_id
        return jsonify(message), 403
    version = Answers.get_max_version(user_id)

    if version is None:
        version = 0
    else:
        version += 1

    for answer in data['responses']:
        question_nr = answer['questionNr']
        score = answer['value']
        new_score = Answers(question_nr=question_nr,
                            user_id=user_id,
                            answer=score,
                            version=version)
        db.session.add(new_score)

    db.session.commit()

    scores = Answers.calculate_score(user_id, version)
    Result.save_results(scores)

    message["status"] = "success"
    message["message"] = "Answers Saved"
    return jsonify(message), 200
