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
    is_movement = GAME.turn_stage == 'move'
    roll_int, die_file_1, die_file_2, space, in_jail = GAME.roll_dice()
    message = player+' rolled '+str(roll_int)
    emit('roll result', {'user_name': ANNOUNCEMENT, 'message': message,
                         'die_file_1': die_file_1, 'die_file_2': die_file_2, 'roll_int': roll_int}, broadcast=True)
    if is_movement:
        move_piece(request.sid, space, in_jail)


def move_piece(user_id, space, in_jail):
    player = 'Player'+str(players.index(user_id)+1)
    color = COLORS[players.index(user_id)]
    location = GAME.BOARD[space].name
    if in_jail:
        message = player+' is In Jail!'
    else:
        message = player+' landed on '+location
    emit('move piece', {'player': player, 'space': space, 'color': color, 'in_jail': in_jail}, broadcast=True)
    emit('new chat', {'user_name': ANNOUNCEMENT, 'message': message}, broadcast=True)
    update_money()


def update_money():
    user_names = []
    money = []
    for i in range(len(GAME.PLAYERS)):
        user_names.append('Player'+str(i+1))
        money.append(GAME.PLAYERS[i].money)
    emit('update money', {'players': user_names, 'money': money})


@SOCKETIO.on('chance')
def chance():
    if players.index(request.sid) != GAME.current_player or GAME.turn_stage != 'chance':
        return
    chance_card, player_position, in_jail = GAME.chance()
    emit('chance result', {'card_content': chance_card[0]}, broadcast=True)
    if chance_card[1] in ['go to space', 'go to jail', 'movement']:
        move_piece(request.sid, player_position, in_jail)
    else:
        update_money()


@SOCKETIO.on('community chest')
def community_chest():
    if players.index(request.sid) != GAME.current_player or GAME.turn_stage != 'community chest':
        return
    comchest_card, player_position, in_jail = GAME.community_chest()
    emit('community chest result', {'card_content': comchest_card[0]}, broadcast=True)
    if comchest_card[1] in ['go to space', 'go to jail']:
        move_piece(request.sid, player_position, in_jail)
    else:
        update_money()


@SOCKETIO.on('pay')
def pay(data):
    some_result = monopoly_game.pay(data.amount, data.payer, data.recipient)
    """ TODO emit the result to the users """
    return some_result


if __name__ == '__main__':
    SOCKETIO.run(SERVER, host="0.0.0.0", port=8080, debug=True)
