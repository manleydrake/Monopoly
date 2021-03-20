from flask import Flask, render_template, request
from flask_socketio import emit, SocketIO

server = Flask(__name__)
server.config['SECRET KEY'] = 'svonwoudnwvob1235#'
socketio = SocketIO(server)
players = []
colors = ['#0000FF', '#FFA500', '#FF6347', '#FFF000', '#228C22', '#800080']


@server.route('/')
def sessions():
    return render_template('index.html')


@socketio.on('connect')
def connect():
    # This if block is a placeholder for now, as we are only implementing one game at a time.
    # This can be used to manage multiple game sessions in the future if that is desired.
    if len(players) == 6:
        emit('session full', broadcast=True)
        return
    print('User connected')
    player_number_base = players.index(None) if None in players else len(players)
    players[player_number_base] = request.sid
    player_name = 'Player'+str(player_number_base+1)
    player_color = colors[player_number_base]
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
    print('disconnect confirmed')


@socketio.on('bye')
def signoff(msg):
    user = msg['user_name']
    print(user+' disconnected')
    emit('new chat', {'user_name': 'ANNOUNCEMENT', 'message': user+' disconnected'}, broadcast=True)
    player_number = players.index(request.sid)
    players[player_number] = None


def message_received():
    print('message received')


@socketio.on('new chat')
def handle_chat(json):
    print('received event: ' + str(json))
    emit('new chat', json, callback=message_received, broadcast=True)


if __name__ == '__main__':
    socketio.run(server, host="0.0.0.0", port=8080, debug=True)
