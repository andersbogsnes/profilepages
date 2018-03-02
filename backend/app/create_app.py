from flask import Flask, render_template
from app.config import ProdConfig
from app.model import User, Question, Answers, Params, Profiles, Result
from app.blueprints.questions import question
from app.blueprints.user import users
from app.extensions import db, cors, bcrypt


def create_app(config=ProdConfig):
    app = Flask(__name__)

    app.config.from_object(config)
    db.init_app(app)
    cors.init_app(app)
    bcrypt.init_app(app)

    app.register_blueprint(question)
    app.register_blueprint(users)

    register_shell_context(app)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.cli.command()
    def init_db():
        db.drop_all()
        db.create_all()
        Question.seed_data()
        Profiles.seed_data()
        Params.seed_data()
        print("Database created")

    return app


def register_shell_context(app):
    def shell_context():
        return {
            'db': db,
            'User': User,
            'Answers': Answers,
            'Params': Params,
            'Question': Question,
            'Result': Result

        }
    app.shell_context_processor(shell_context)