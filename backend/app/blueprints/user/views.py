from flask import request, jsonify, Blueprint

from app.blueprints.user.model import User
from app.blueprints.auth.utils import authenticate

users = Blueprint('users', __name__)


@users.route('/user', methods=['POST'])
def create_user():
    message = {
        "status": "error",
        "message": "User already exists",
        "data": {}
    }

    user_data = request.get_json()
    user = User.new_user(user_data)
    if user:
        message["status"] = "success"
        message["message"] = "User created"
        message["data"] = user.to_json()
        message["data"]["auth"] = user.generate_token().decode()
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
