from flask import request, redirect, url_for, jsonify
from functools import wraps
from app.blueprints.user.model import User


def authenticate(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        message = {
            "status": "error",
            "message": "Must be logged in"
        }

        auth_header = request.headers.get('Authorization')
        if auth_header:
            auth_token = auth_header.split(" ")[1]
            resp = User.decode_token(auth_token)

            if isinstance(resp, int):
                return f(resp, *args, **kwargs)
            else:
                message["message"] = resp
        return jsonify(message), 401
    return decorated
