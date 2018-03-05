from sqlalchemy.exc import IntegrityError

from app.extensions import db, bcrypt
import datetime
import csv
from app.config import current_config
import jwt
import pandas as pd
import numpy as np


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)

    def __init__(self, id, text):
        self.id = id
        self.text = text

    @classmethod
    def seed_data(cls):
        with open(current_config.BASE_PATH.joinpath('data', 'questions.csv')) as f:
            reader = csv.DictReader(f, skipinitialspace=True)
            for line in reader:
                new_line = cls(line['ID'], line['Text'])
                db.session.add(new_line)
        db.session.commit()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.Text, unique=True)
    email = db.Column(db.Text, unique=True)
    initials = db.Column(db.Text, unique=True)
    password = db.Column(db.Binary(128))

    answers = db.relationship('Answers', backref='user', cascade="all, delete-orphan")
    profile = db.relationship('Result', backref='user', cascade="all, delete-orphan")

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


class Answers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_nr = db.Column(db.Integer, db.ForeignKey('question.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    answer = db.Column(db.Integer)
    version = db.Column(db.Integer, default=0)
    date_answered = db.Column(db.DateTime, default=datetime.datetime.now())

    @classmethod
    def calculate_score(cls, user_id, version):
        results = (db.session.query(Answers.user_id,
                                    Params.profile,
                                    db.func.sum(Params.coef).label('coef'))
                   .join(Params,
                         db.and_(
                             Answers.question_nr == Params.question_nr,
                             Answers.answer == Params.answer))
                   .filter(Answers.user_id == user_id)
                   .filter(Answers.version == version)
                   .group_by(Answers.user_id, Params.profile)
                   ).cte()

        return (db.session.query(results.c.user_id,
                                 results.c.profile,
                                 (results.c.coef + Profiles.intercept).label('coef'))
                .join(Profiles, results.c.profile == Profiles.id)).all()

    @classmethod
    def get_max_version(cls, user_id):
        return db.session.query(db.func.max(cls.version)).filter(cls.user_id == user_id).scalar()


class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    profile_id = db.Column(db.Integer, db.ForeignKey('profiles.id'))
    percent_score = db.Column(db.Float)

    @classmethod
    def save_results(cls, results):
        for result in results:
            existing_result = (
                cls.query.filter_by(user_id=result.user_id)
                    .filter_by(profile_id=result.profile)
                    .first())

            if existing_result:
                existing_result.percent_score = result.coef
                db.session.add(existing_result)

            else:
                new_result = cls(user_id=result.user_id,
                                 profile_id=result.profile,
                                 percent_score=result.coef
                                 )
                db.session.add(new_result)
        db.session.commit()

    @classmethod
    def get_results(cls, user_id):
        query = (db.session.query(Profiles.type_name,
                                  Result.percent_score)
                 .join(Result, Result.profile_id == Profiles.id)
                 .filter(Result.user_id == user_id))
        df = pd.read_sql(query.statement, query.session.bind)
        df['percent_score'] = df.percent_score.apply(np.exp).transform(lambda x: x / x.sum()).multiply(100)
        return df.to_json(force_ascii=False, orient='records')


class Profiles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type_name = db.Column(db.Text)
    intercept = db.Column(db.Float)

    def __init__(self, type_name, intercept):
        self.type_name = type_name
        self.intercept = intercept

    @classmethod
    def seed_data(cls):
        with open(current_config.BASE_PATH.joinpath('data', 'profiles.csv'), encoding='utf-8') as f:
            reader = csv.DictReader(f, skipinitialspace=True)
            for line in reader:
                new_profile = cls(type_name=line['name'],
                                  intercept=line['intercept'])
                db.session.add(new_profile)
        db.session.commit()


class Params(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_nr = db.Column(db.Integer)
    profile = db.Column(db.Integer, db.ForeignKey('profiles.id'))
    answer = db.Column(db.Integer)
    coef = db.Column(db.Float)

    @classmethod
    def seed_data(cls):
        with open(current_config.BASE_PATH.joinpath('data', 'params.csv')) as f:
            reader = csv.DictReader(f, skipinitialspace=True)
            for line in reader:
                new_param = cls(question_nr=int(line['question_nr']),
                                profile=int(line['profile']),
                                answer=int(line['answer']),
                                coef=float(line['param']))
                db.session.add(new_param)
        db.session.commit()
