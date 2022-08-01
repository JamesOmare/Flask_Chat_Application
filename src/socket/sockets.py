from .. import socketio
from flask_socketio import send



# def task(sid):
#     socketio.sleep(5)
#     result = socketio.call()

@socketio.on('connect', namespace='/chat')
def connect():
    print(f'Client succesfully connected')
    # socketio.start_background_task(task, sid)

@socketio.on('message')
def message(data):
    print(f'\n\n{data}\n\n')
    send(data)

# @socketio._handle_event
# def sum(sid, data):
#     result = data['numbers'][0] + data['numbers'][1]
#     socketio.emit('sum_result', {'results': result}, to=sid)

@socketio.on('disconnect')
def disconnect(sid):
    print(sid, 'disconnected')