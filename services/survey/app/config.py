import datetime
import os

import pathlib


class Config:
    BASE_PATH = pathlib.Path(__file__).parent
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_EXPIRY = datetime.timedelta(days=5)
    BCRYPT_LOG_ROUNDS = 12


class DevConfig(Config):
    DEBUG = True
    SECRET_KEY = 'mysupersecretkey'
    BCRYPT_LOG_ROUNDS = 4


class ProdConfig(Config):
    DEBUG = False
    TESTING = False
    BCRYPT_LOG_ROUNDS = 12
    SECRET_KEY = os.getenv('SECRET_KEY')


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_TEST_URL')
    SECRET_KEY = 'mysupersecretkey'
    BCRYPT_LOG_ROUNDS = 4


configs = {
    'prod': ProdConfig,
    'dev': DevConfig,
    'test': TestConfig
}

current_config = configs[os.getenv('CONFIG', 'prod')]
