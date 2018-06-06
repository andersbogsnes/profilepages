from flask import Flask, render_template
from app.config import ProdConfig
from app.blueprints.survey.model import Question, Answers, Result, Profiles, Params
from app.blueprints.user.model import User
from app.blueprints.user.views import users
from app.blueprints.survey.views import survey
from app.blueprints.auth.views import auth
from app.extensions import db, cors, bcrypt
from app.commands import init_db, test


def create_app(config=ProdConfig):
    app = Flask(__name__)

    app.config.from_object(config)
    db.init_app(app)
    cors.init_app(app)
    bcrypt.init_app(app)

    app.register_blueprint(survey)
    app.register_blueprint(users)
    app.register_blueprint(auth)

    register_shell_context(app)
    register_commands(app)

    @app.route('/')
    def index():
        return render_template('index.html')

    return app


def register_shell_context(app):
    def shell_context():
        return {
            'db': db,
            'User': User,
            'Answers': Answers,
            'Params': Params,
            'Question': Question,
            'Result': Result,
            'Profiles': Profiles,
        }

    app.shell_context_processor(shell_context)


def register_commands(app):
    app.cli.add_command(init_db)
    app.cli.add_command(test)
