from decouple import config
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = config('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(basedir, 'chat_application.db')
    DEBUG = config('DEBUG', cast=bool)
