import pytest
from app.extensions import db as _db
from app.create_app import create_app
from app.config import configs
from app.blueprints.survey.model import Question, Profiles, Params


@pytest.fixture(name="app", scope="session")
def _app():
    config = configs['test']
    app = create_app(config)
    ctx = app.app_context()
    ctx.push()
    yield app
    ctx.pop()


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture(name="db")
def database():
    _db.create_all()
    Question.seed_data()
    Profiles.seed_data()
    Params.seed_data()
    yield _db
    _db.drop_all()


@pytest.fixture(scope='function')
def session(db):
    conn = db.engine.connect()
    transaction = conn.begin()
    yield db.session
    transaction.rollback()
    conn.close()
    db.session.remove()
