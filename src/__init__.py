from distutils.command.config import config
import imp
from mimetypes import MimeTypes
from flask import Flask
from .config.config import config_dict
from.utils import db, migrate
from flask_migrate import Migrate

from werkzeug.exceptions import NotFound, MethodNotAllowed


def create_app(config = config_dict['dev']):
    app = Flask(__name__)
    app.config.from_object(config)

    #register blueprints


    db.init_app(app)
    migrate = Migrate(app, db)

    @app.errorhandler(NotFound)
    def not_found(error):
        return {'error': 'Not Found'}, 404

    @app.errorhandler(MethodNotAllowed)
    def method_not_allowed(error):
        return {'error': 'Method Not Allowed'}, 405

    

    return app


