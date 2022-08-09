import datetime
from flask import Flask
from os import path

from flask_login import current_user
from .config.config import Config
from .models.user import User
from .auth.views import auth
from .chat.views import chat
from.utils import db, migrate, login_manager
from flask_migrate import Migrate
from flask_socketio import send, emit, join_room, leave_room

from flask_socketio import SocketIO

socketio = SocketIO()
ROOMS = ['gaming', 'movies', 'music', 'sports', 'education']
DB_NAME = 'chat_application.db'

def create_app(config = Config):
    # instance_relative_config states that the 
    # config files are relative to the instance folder
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config)


    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    socketio.init_app(app, cors_allowed_origins=["http://127.0.0.1:5000"])

    #register blueprints
    app.register_blueprint(auth)
    app.register_blueprint(chat)

    create_database(app)

    login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def load_user(id):
       return User.query.get(int(id))

    @socketio.on('connect')
    def connect(data):
        print(f'Client succesfully connected')

    @socketio.on('message')
    def message(data):
        msg = data.get('msg')
        username = data.get('username')
        chatroom = data.get("room")
        
        #Set timestamp
        time = datetime.datetime.now()
        timestamp = time.strftime("%I:%M:%S %p (%a, %b %d, %Y)")
        
        send({'username': username, 'msg': msg, 'timestamp': timestamp }, room = chatroom)
        
        emit('calling', 'This is a custom event message')

    @socketio.on('join')
    def join_chatroom(data):
        join_room(data['room'])
        username = data['username']
        room = data['room']
        send({'msg': f'{username} has joined the {room} room.'}, room = data['room'])
        

    @socketio.on('leave')
    def leave_chatroom(data):
        leave_room(data['room'])
        username = data['username']
        room = data['room']
        send({'msg': f'{username} has left the {room} room.'}, room = data['room'])
    
    
    return app

def create_database(app):
    if not path.exists('src/config/'+DB_NAME):
        db.create_all(app = app)
        print('created database')

