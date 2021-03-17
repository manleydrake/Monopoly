from flask import Flask, render_template
from flask_socketio import emit, SocketIO

server = Flask(__name__)
server.config['SECRET KEY'] = 'svonwoudnwvob1235#'
socketio = SocketIO(server)
players = [False, False, False, False, False, False]
colors = ['#0000FF', '#FFA500', '#FF6347', '#FFFF00', '#228C22', '#800080']


@server.route('/')
def sessions():
    return render_template('index.html')


@socketio.on('connect')
def connect():
    print('User connected')
    player_number = players.index(False)
    players[player_number] = True
    player_name = 'Player'+str(player_number+1)
    player_color = colors[player_number]
    emit(
        'user connect',
        {
            'user_name': 'ANNOUNCEMENT',
            'message': player_name+' connected',
            'player_name': player_name,
            'player_color': player_color
        },
        broadcast=True
    )


@socketio.on('disconnect')
def disconnect():
    print('User disconnected')
    emit('new chat', {'user_name': 'ANNOUNCEMENT', 'message': 'User disconnected'})


def message_received():
    print('message received')


@socketio.on('new chat')
def handle_chat(json):
    print('received event: ' + str(json))
    emit('new chat', json, callback=message_received, broadcast=True)


if __name__ == '__main__':
    socketio.run(server, host="0.0.0.0", port=8080, debug=True)
