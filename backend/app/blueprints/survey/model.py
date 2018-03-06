import csv
import datetime

import numpy as np
import pandas as pd

from app.config import current_config
from app.extensions import db


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

    @classmethod
    def count(cls):
        return len(cls.query.all())


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