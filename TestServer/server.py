from enum import Enum
from flask import Flask, render_template
from flask_socketio import SocketIO

server = Flask(__name__)
server.config['SECRET KEY'] = 'svonwoudnwvob1235#'
socketio = SocketIO(server)


class Methods(Enum):
    GET = 'GET'
    POST = 'POST'


@server.route('/')
def sessions():
    return render_template('index.html')


def message_received(methods=Methods):
    print('message received')


@socketio.on('my event')
def handle_custom_event(json, methods=Methods):
    print('received event: ' + str(json))
    socketio.emit('my response', json, callback=message_received)


if __name__ == '__main__':
    socketio.run(server, host="0.0.0.0", port=8080, debug=True)
