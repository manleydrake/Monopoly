from flask import Flask, render_template, request
from flask_socketio import emit, SocketIO
import monopoly_game

SERVER = Flask(__name__)
SERVER.config['SECRET KEY'] = 'svonwoudnwvob1235#'
SOCKETIO = SocketIO(SERVER)
ANNOUNCEMENT = 'ANNOUNCEMENT'
COLORS = ['#0000FF', '#FFA500', '#FF6347', '#FFF000', '#228C22', '#800080']
GAME = monopoly_game.Game()

players = [None, None, None, None, None, None]


@SERVER.route('/')
def sessions():
    # Method to handle the default initial connection by a user over HTTP
    return render_template('index.html')


@SOCKETIO.on('connect')
def connect():
    # Method to handle the socket connection from a user after the user has rendered the index.html

    # This if block is a placeholder for now, as we are only implementing one game at a time.
    # This can be used to manage multiple game sessions in the future if that is desired.
    if None not in players:
        emit('session full')
        return
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
    # Method to handle disconnect events
    # Frees up a space in the game and removes the old user from the list of players
    if request.sid in players:
        user_number = players.index(request.sid)
        user = 'Player'+str(user_number+1)
        print(user+' disconnected')
        emit('new chat', {'user_name': ANNOUNCEMENT, 'message': user+' disconnected'}, broadcast=True)
        players[user_number] = None
    print('disconnect confirmed')


@SOCKETIO.on('new chat')
def handle_chat(json):
    # Method used to send events to and from each player in the chat. Also a framework for the rest of the user actions
    print('received event: ' + str(json))
    emit('new chat', json, broadcast=True)


@SOCKETIO.on('start game')
def start():
    """ TODO build out the start_game function in monopoly_game and send data to users """
    playing_players = []
    for player in players:
        if player is not None:
            playing_players.append(player)
    GAME.start_game(playing_players)
    user_names = []
    for i in range(len(playing_players)):
        user_names.append('Player'+str(i+1))
    emit('start game', {'players': user_names, 'colors': COLORS}, broadcast=True)


@SOCKETIO.on('roll dice')
def roll():
    if players.index(request.sid) != GAME.current_player:
        return
    player = 'Player'+str(players.index(request.sid)+1)
    color = COLORS[players.index(request.sid)]
    roll_int, die_file_1, die_file_2, is_movement, space = GAME.roll_dice()
    if GAME.turn_stage == 'move':
        if GAME.current_player == len(GAME.PLAYERS)-1:
            GAME.current_player = 0
        else:
            GAME.current_player += 1
    message = player+' rolled '+str(roll_int)
    emit('roll result', {'user_name': ANNOUNCEMENT, 'message': message,
                         'is_movement': is_movement, 'player': player, 'space': space, 'color': color,
                         'die_file_1': die_file_1, 'die_file_2': die_file_2, 'roll_int': roll_int}, broadcast=True)


@SOCKETIO.on('chance')
def chance():
    """ TODO build out the chance function in monopoly_game """
    """ TODO get the returned values from the chance function in monopoly_game and send result to users """
    chance_card = GAME.chance()
    emit('chance result', {'card_content': chance_card}, broadcast=True)



@SOCKETIO.on('community chest')
def community_chest():
    """ TODO build out the community_chest function in monopoly_game """
    """ TODO get the returned values and send result to users """
    comchest_card = GAME.community_chest()
    emit('community chest result', {'card_content': comchest_card}, broadcast=True)


@SOCKETIO.on('pay')
def pay(data):
    """ TODO build out the pay function in monopoly_game """
    """ TODO fix the below line so that the correct information is received from monopoly_game.pay() """
    some_result = GAME.pay(data.amount, data.payer, data.recipient)
    """ TODO emit the result to the users """
    return some_result


if __name__ == '__main__':
    SOCKETIO.run(SERVER, host="0.0.0.0", port=8080, debug=True)
