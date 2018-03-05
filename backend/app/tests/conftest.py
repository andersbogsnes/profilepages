import pytest
from app.extensions import db
from app.create_app import create_app
from app.config import configs
from app.model import Params, Profiles, Question


@pytest.fixture(scope='session')
def app():
    config = configs['test']
    app = create_app(config)
    ctx = app.app_context()
    ctx.push()
    yield app
    ctx.pop()


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def db(app):
    db.create_all()
    Question.seed_data()
    Profiles.seed_data()
    Params.seed_data()
    yield db
    db.drop_all()


@pytest.fixture(scope='function')
def session(db):
    conn = db.engine.connect()
    transaction = conn.begin()
    yield session
    transaction.rollback()
    conn.close()
    session.remove()
