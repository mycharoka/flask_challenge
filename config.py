import os

# default config


class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = 'kesayangan'
    # SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:trebomb@localhost/delameta-db // postgresql://localhost/delameta-db'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(BaseConfig):
    DEBUG = False


class StagingConfig(BaseConfig):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(BaseConfig):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(BaseConfig):
    TESTING = True
