from flask import Blueprint, request, jsonify
from app.model import User

users = Blueprint('users', __name__)


@users.route('/user', methods=['POST'])
def create_user():
    if request.method == 'POST':
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


@users.route('/login', methods=['POST'])
def login():
    message = {
        "status": "error",
        "message": "Failed login",
        "data": {}
    }

    data = request.get_json()
    email = data['email']
    password = data['password']
    user = User.query.filter_by(email=email).first()

    if user and user.check_password(password):
        auth_token = user.generate_token()
        if auth_token:
            message["status"] = "success"
            message["message"] = "Logged in successfully"
            message["data"] = user.to_json()
            message["data"]["auth"] = auth_token.decode()
            return jsonify(message), 200
    else:
        message["message"] = "User doesn't exist"
        return jsonify(message), 404


@users.route('/user/<int:user_id>')
def get_user(user_id):
    message = {
        "status": "error",
        "message": "User not found",
        "data": {}
    }

    user = User.query.get(user_id)
    if user:
        message["status"] = "success"
        message["message"] = "User found"
        message['data'] = user.to_json()
        return jsonify(message), 200
    else:
        return jsonify(message), 404


@users.route('/users')
def get_all_users():
    message = {
        "status": "error",
        "message": "Users not found",
        "data": {}
    }
    try:
        users_list = [user.to_json() for user in User.query.all()]
    except AttributeError:
        users_list = None

    if users_list:
        message["status"] = "success"
        message["message"] = "Users found"
        message["data"] = users_list
        return jsonify(message), 200

    return jsonify(message), 404
