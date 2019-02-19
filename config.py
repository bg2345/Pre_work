import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'random-word-random-word'


    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:BRUINS4@localhost:5432/portfolio'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
