import os


class Config(object):
    DEBUG=False
    TESTING = False
    CSRF_ENABLED=False
    MAIL_SERVER = os.environ.get("MAIL_SERVER")
    MAIL_PORT = os.environ.get('MAIL_PORT')
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS')
    MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL')
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class DevelopmentConfig(Config):
    DEBUG=True
    ENV='development'
    SECRET_KEY='secret_for_test_development'


class ProductionConfig(Config):
    SECRET_KEY = os.environ.get("SECRET_KEY")