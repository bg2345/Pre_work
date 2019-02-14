import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'random-word-random-word'


    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABSE_URL') or \
        'sqlite:///' + os.path.join(BASEDIR, 'app.db')

    SQLALCHEMY_TRACK_MODIFICATIONS = False
