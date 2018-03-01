from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from backend.config import Config


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/questions')
def question():
    from backend.model import Question
    response = [{'id':row.id, 'text': row.text} for row in Question.query.all()]
    return jsonify(response)


@app.cli.command()
def init_db():
    from backend.model import User, Question, Scores
    db.drop_all()
    db.create_all()
    Question.seed_data()
    print("Database created")


if __name__ == '__main__':
    app.run()
