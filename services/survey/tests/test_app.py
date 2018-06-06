from app.config import configs


def test_homepage_loads(client):
    resp = client.get('/')
    assert 200 == resp.status_code
    assert b'<div id="app">' in resp.data


def test_config_is_test():
    config = configs['test']
    assert 'mysupersecretkey' == config.SECRET_KEY
    assert 'profilepage_test' in config.SQLALCHEMY_DATABASE_URI
    assert 4 == config.BCRYPT_LOG_ROUNDS


def test_config_is_dev():
    config = configs['dev']
    assert 'mysupersecretkey' == config.SECRET_KEY
    assert 'profilepage' in config.SQLALCHEMY_DATABASE_URI
    assert 'profielpage_test' not in config.SQLALCHEMY_DATABASE_URI
    assert 4 == config.BCRYPT_LOG_ROUNDS


def test_config_is_prod():
    config = configs['prod']
    assert 'mysupersecretkey' != config.SECRET_KEY
    assert 'profilepage' in config.SQLALCHEMY_DATABASE_URI
    assert 'profilepage_test' not in config.SQLALCHEMY_DATABASE_URI
