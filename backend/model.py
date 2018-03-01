from backend.app import db
import datetime


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)


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

