from flask import Flask, render_template
from flask_socketio import emit, SocketIO

server = Flask(__name__)
server.config['SECRET KEY'] = 'svonwoudnwvob1235#'
socketio = SocketIO(server)


@server.route('/')
def sessions():
    return render_template('index.html')


@socketio.on('connect')
def connect():
    print('User connected')
    emit('my response', {'user_name': 'ANNOUNCEMENT', 'message': 'User connected'})


@socketio.on('disconnect')
def disconnect():
    print('User disconnected')
    emit('my response', {'user_name': 'ANNOUNCEMENT', 'message': 'User disconnected'})


def message_received():
    print('message received')


@socketio.on('my event')
def handle_custom_event(json):
    print('received event: ' + str(json))
    socketio.emit('my response', json, callback=message_received)


if __name__ == '__main__':
    socketio.run(server, host="0.0.0.0", port=8080, debug=True)
