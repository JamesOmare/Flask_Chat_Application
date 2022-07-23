from ...src import socketio, send


@socketio.on('message')
def message(data):
    print(f'\n\n{data}\n\n')
    send(data)