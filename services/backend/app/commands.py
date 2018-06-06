import click
from flask.cli import with_appcontext

from app.config import current_config
from app.extensions import db
from app.blueprints.survey.model import Question, Answers, Result, Profiles, Params
from app.blueprints.user.model import User


@click.command()
def test():
    import pytest
    rv = pytest.main([current_config.BASE_PATH.parent.joinpath('tests'), '--verbose'])
    exit(rv)


@click.command()
@with_appcontext
def init_db():
    db.drop_all()
    db.create_all()
    Profiles.seed_data()
    Question.seed_data()
    Params.seed_data()
    click.echo("Database Initialized")