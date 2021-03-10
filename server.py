from flask import Flask, render_template
from flask_socketio import emit, SocketIO

server = Flask(__name__)
server.config['SECRET KEY'] = 'svonwoudnwvob1235#'
socketio = SocketIO(server)
players = []


@server.route('/')
def sessions():
    return render_template('index.html')


@socketio.on('connect')
def connect():
    print('User connected')
    player_name = 'Player'+str(len(players)+1)
    players.append(player_name)
    emit(
        'user connect',
        {'user_name': 'ANNOUNCEMENT', 'message': player_name+' connected', 'player_name': player_name},
        broadcast=True
    )


@socketio.on('disconnect')
def disconnect():
    print('User disconnected')
    emit('my response', {'user_name': 'ANNOUNCEMENT', 'message': 'User disconnected'})


def message_received():
    print('message received')


@socketio.on('new chat')
def handle_chat(json):
    print('received event: ' + str(json))
    socketio.emit('new chat', json, callback=message_received)


if __name__ == '__main__':
    socketio.run(server, host="0.0.0.0", port=8080, debug=True)
