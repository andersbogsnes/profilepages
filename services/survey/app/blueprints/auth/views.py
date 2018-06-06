from flask import request, jsonify, Blueprint
from app.blueprints.user.model import User

auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.route('/login', methods=['POST'])
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
