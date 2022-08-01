from flask_socketio import emit, join_room, leave_room
from . import socketio


@socketio.on('connect', namespace='/chat')
def connect():
    print('Client connected successfully')