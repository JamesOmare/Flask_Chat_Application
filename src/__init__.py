from flask import Flask
from .config.config import Config
from .auth.views import auth
from.utils import db, migrate
from flask_migrate import Migrate
from werkzeug.exceptions import NotFound, MethodNotAllowed


def create_app(config = Config):
    # instance_relative_config states that the 
    # config files are relative to the instance folder
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config)

    db.init_app(app)
    migrate.init_app(app, db)

    #register blueprints
    app.register_blueprint(auth)


    @app.errorhandler(NotFound)
    def not_found(error):
        return {'error': 'Not Found'}, 404

    @app.errorhandler(MethodNotAllowed)
    def method_not_allowed(error):
        return {'error': 'Method Not Allowed'}, 405


    @app.shell_context_processor
    def make_shell_context():
        return {
            'db': db
        }

    

    return app


