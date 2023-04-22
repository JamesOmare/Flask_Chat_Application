from decouple import config
import os

basedir = os.path.abspath(os.path.dirname(__file__))

# local development
# class Config(object):
#     SECRET_KEY = config('SECRET_KEY')
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(basedir, 'chat_application.db')
#     DEBUG = config('DEBUG', cast=bool)

# heroku deploy
class Config(object):
    SECRET_KEY = config('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = config('DATABASE_URL').replace('postgres://', 'postgresql://')
    DEBUG = config('DEBUG', cast=bool)