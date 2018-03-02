from flask import Blueprint, jsonify, request
from app.model import Question, Answers, User, Params, Result
from app.extensions import db

question = Blueprint('questions', __name__)


@question.route('/questions')
def get_questions():
    response = [{'id': row.id, 'text': row.text} for row in Question.query.all()]
    return jsonify(response)


@question.route('/answer', methods=['POST'])
def save_answers():
    message = {
        "status": "error",
        "message": "An error occurred",
    }
    data = request.get_json(cache=False)

    user_id = User.decode_token(data['token'])

    if isinstance(user_id, str):
        message["message"] = user_id
        return jsonify(message), 403

    version = get_max_version(user_id)

    if version:
        version += 1
    else:
        version = 0

    for answer in data['responses']:
        question_nr = answer['questionNr']
        score = answer['value']
        new_score = Answers(question_nr=question_nr,
                            user_id=user_id,
                            answer=score,
                            version=version)
        db.session.add(new_score)

    db.session.commit()
    message["status"] = "success"
    message["message"] = "Answers Saved"
    return jsonify(message), 200


def get_max_version(user_id):
    return db.session.query(db.func.max(Answers.version)).filter(Answers.user_id == user_id).scalar()


def calculate_score(user_id):
    version = get_max_version(user_id)
    if version is None:
        return None
    results = db.session.query(Answers).filter(Answers.user_id == user_id).filter(Answers.version == version)

    for result in results:
        score = Params.query.filter(Params.question_nr == result.question_nr).filter(Params.answer == result.answer)
        for value in score:
            profile_score = Result(user_id=user_id,
                                   profile_id=value.profile,
                                   percent_score=value.coef)
            db.session.add(profile_score)
    db.session.commit()
    return (db.session.query(Result.profile_id,
                             db.func.sum(Result.percent_score))
            .filter_by(user_id=user_id)
            .group_by(Result.profile_id)
            .all())
