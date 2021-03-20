from flask import Flask, render_template, request
from flask_socketio import emit, SocketIO

SERVER = Flask(__name__)
SERVER.config['SECRET KEY'] = 'svonwoudnwvob1235#'
SOCKETIO = SocketIO(SERVER)
ANNOUNCEMENT = 'ANNOUNCEMENT'
COLORS = ['#0000FF', '#FFA500', '#FF6347', '#FFF000', '#228C22', '#800080']

players = [None, None, None, None, None, None]


@SERVER.route('/')
def sessions():
    return render_template('index.html')


@SOCKETIO.on('connect')
def connect():
    # This if block is a placeholder for now, as we are only implementing one game at a time.
    # This can be used to manage multiple game sessions in the future if that is desired.
    if None not in players:
        emit('session full')
        return
    else:
        print('User connected')
        player_number_base = players.index(None)
        players[player_number_base] = request.sid
    player_name = 'Player'+str(player_number_base+1)
    player_color = COLORS[player_number_base]
    emit(
        'user connect',
        {
            'user_name': ANNOUNCEMENT,
            'message': player_name+' connected',
            'player_name': player_name,
            'player_color': player_color
        },
        broadcast=True
    )


@SOCKETIO.on('disconnect')
def disconnect():
    if request.sid in players:
        user_number = players.index(request.sid)
        user = 'Player'+str(user_number+1)
        print(user+' disconnected')
        emit('new chat', {'user_name': ANNOUNCEMENT, 'message': user+' disconnected'}, broadcast=True)
        players[user_number] = None
    print('disconnect confirmed')


@SOCKETIO.on('new chat')
def handle_chat(json):
    print('received event: ' + str(json))
    emit('new chat', json, broadcast=True)


if __name__ == '__main__':
    SOCKETIO.run(SERVER, host="0.0.0.0", port=8080, debug=True)
