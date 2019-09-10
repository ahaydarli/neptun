import os


class Config:
    DEBUG = False
    DEVELOPMENT = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or "i\x8fV\xfbU\xd2\xde9\x0b\xb3{i\xa7+\xfe="


class DevelopmentConfig(Config):
    DEBUG = True
    DEVELOPMENT = True
    SQLALCHEMY_DATABASE_URI = "postgresql://localhost/6second-dev"
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql://localhost/6second-prod"


class TestingConfig(Config):
    TESTING = True


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig
}



