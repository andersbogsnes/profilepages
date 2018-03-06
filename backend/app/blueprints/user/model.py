import datetime

import jwt
from sqlalchemy.exc import IntegrityError

from app.config import current_config
from app.extensions import db, bcrypt


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.Text, unique=True)
    email = db.Column(db.Text, unique=True)
    initials = db.Column(db.Text, unique=True)
    password = db.Column(db.Binary(128))

    answers = db.relationship('Answers', backref='user', cascade="all")
    result = db.relationship('Result', backref='user', cascade="all")

    def __init__(self, user_name, email, initials, password):
        self.user_name = user_name
        self.email = email
        self.initials = initials
        self.set_password(password)

    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password)

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

    def generate_token(self):
        payload = {
            'exp': datetime.datetime.utcnow() + current_config.JWT_EXPIRY,
            'iat': datetime.datetime.utcnow(),
            'sub': self.id
        }
        return jwt.encode(
            payload,
            current_config.SECRET_KEY,
            algorithm='HS256'
        )

    @staticmethod
    def decode_token(token):
        try:
            payload = jwt.decode(token, current_config.SECRET_KEY)
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please try again'

    @classmethod
    def new_user(cls, data):
        user = User(**data)
        try:
            db.session.add(user)
            db.session.commit()
            return user
        except IntegrityError as e:
            return None

    def to_json(self):
        return {
            "id": self.id,
            "user_name": self.user_name,
            "email": self.email,
            "initials": self.initials
        }