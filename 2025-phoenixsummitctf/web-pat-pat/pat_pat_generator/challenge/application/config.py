from application.util import generate
import os

class Config(object):
    print(os.getcwd(), flush=True)
    SECRET_KEY = generate(50)
    UPLOAD_FOLDER = os.getcwd() + '/application/static/patpats'
    MAX_CONTENT_LENGTH = 2.5 * 1000 * 1000

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True