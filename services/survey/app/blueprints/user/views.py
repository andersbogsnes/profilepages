from flask import request, jsonify, Blueprint
from marshmallow import ValidationError

from app.blueprints.user.model import User, user_schema, login_schema
from app.blueprints.auth.utils import authenticate
from app.extensions import db

users = Blueprint('users', __name__)


@users.route('/user/ping')
def ping():
    return "pong"


@users.route('/user', methods=['POST'])
def create_user():
    message = {
        "status": "error",
        "message": "User already exists",
        "data": {}
    }

    user_data = request.get_json()
    try:
        new_user = user_schema.load(user_data)
    except ValidationError as err:
        message["data"] = err.messages
        return jsonify(message), 403

    existing_user = User.query.filter_by(email=new_user['email']).first()

    if existing_user is None:
        new_user = User.create_user(**new_user)
        db.session.add(new_user)
        db.session.commit()
        message["status"] = "success"
        message["message"] = "User created"
        message["data"]["user"] = user_schema.dumps(new_user)
        message["data"]["auth"] = new_user.generate_token().decode()
        return jsonify(message), 200

    return jsonify(message), 403


@users.route('/user', methods=['GET'])
@authenticate
def get_user(resp):
    message = {
        "status": "error",
        "message": "User not found",
        "data": {}
    }
    if isinstance(resp, str):
        message["message"] = resp
        return jsonify(message), 401

    user_id = resp

    user = User.query.get(user_id)
    if user:
        message["status"] = "success"
        message["message"] = "User found"
        message['data'] = user.to_json()
        return jsonify(message), 200
    else:
        return jsonify(message), 404
