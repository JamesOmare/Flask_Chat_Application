from flask import Flask
from os import path
from .config.config import Config
from .models.user import User
from .auth.views import auth
from.utils import db, migrate, login_manager
from flask_migrate import Migrate
from werkzeug.exceptions import NotFound, MethodNotAllowed

DB_NAME = 'chat_application.db'

def create_app(config = Config):
    # instance_relative_config states that the 
    # config files are relative to the instance folder
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    #register blueprints
    app.register_blueprint(auth)

    create_database(app)

    login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def load_user(id):
       return User.query.get(int(id))

    
    
    return app

def create_database(app):
    if not path.exists('src/config/'+DB_NAME):
        db.create_all(app = app)
        print('created database')

