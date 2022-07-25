from ...src import socketio, send



# def task(sid):
#     socketio.sleep(5)
#     result = socketio.call()

@socketio.on('connect')
def connect(sid, environ):
    print(sid, 'connected')
    # socketio.start_background_task(task, sid)
    

@socketio._handle_event
def sum(sid, data):
    result = data['numbers'][0] + data['numbers'][1]
    socketio.emit('sum_result', {'results': result}, to=sid)

@socketio.on('disconnect')
def disconnect(sid):
    print(sid, 'disconnected')