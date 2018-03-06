import click
from app.config import current_config
from flask.cli import with_appcontext
from app.extensions import db
from app.model import Question, Result, Profiles, Params, Answers, User


@click.command()
def test():
    import pytest
    rv = pytest.main([current_config.BASE_PATH.joinpath('tests'), '--verbose'])
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