from backend.app import db
import datetime
from sqlalchemy.ext.hybrid import hybrid_property
import csv


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)

    def __init__(self, id, text):
        self.id = id
        self.text = text

    @classmethod
    def seed_data(cls):
        with open('data/questions.csv') as f:
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

    questionnaire = db.relationship('Scores', backref='user')


class Scores(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_nr = db.Column(db.Integer, db.ForeignKey('question.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    score = db.Column(db.Integer)
    date_answered = db.Column(db.DateTime, default=datetime.datetime.now())


class Profiles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type_name = db.Column(db.Text)
    intercept = db.Column(db.Float)


class Params(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_nr = db.Column(db.Integer)
    profile = db.Column(db.Integer, db.ForeignKey('profiles.id'))
    answer = db.Column(db.Integer)
    coef = db.Column(db.Float)

    @hybrid_property
    def score(self):
        return self.answer * self.coef
