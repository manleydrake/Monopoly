from random import randint
from spaces_info import get_spaces_info
from cards_info import get_chance
from cards_info import get_community_chest


class Space:
    def __init__(self, name, house_multipliers, mortgage, build_cost):
        self.name = name
        self.house_multipliers = house_multipliers
        self.num_houses = 0
        self.mortgage = mortgage
        self.is_mortgaged = False
        self.build_cost = build_cost
        self.owner = None


class Player:
    def __init__(self, name):
        self.name = name
        self.money = 1500
        self.properties = []
        self.space_index = 0

class Game:
    BOARD = []
    PLAYERS = []

    turn_stage = None
    current_player = None

    def init_board(self):
        for space in get_spaces_info():
            self.BOARD.append(Space(space[0], space[1], space[2], space[3]))

    def init_players(self, players):
        for player in players:
            self.PLAYERS.append(Player(player))

    def start_game(self, players):
        """ TODO build out a function to initialize the game on the server and send initial game data to the users """
        self.init_board()
        self.init_players(players)
        self.current_player = 0
        self.turn_stage = 'move'
        return

    def roll_dice(self):
        die1 = randint(1, 6)
        die2 = randint(1, 6)
        die_file_1 = '/static/Images/dice_'+str(die1)+'.png'
        die_file_2 = '/static/Images/dice_'+str(die2)+'.png'
        is_movement = self.turn_stage == 'move'
        if is_movement:
            self.PLAYERS[self.current_player].space_index += die1+die2
            if self.PLAYERS[self.current_player].space_index > 39:
                self.PLAYERS[self.current_player].space_index = self.PLAYERS[self.current_player].space_index - 40
        return die1+die2, die_file_1, die_file_2, is_movement, self.PLAYERS[self.current_player].space_index

    def chance(self):
        chance_list = get_chance()
        card = chance_list[randint(1,17) - 1]
        return card

    def community_chest(self):
        """ TODO create Card class and an initializer for the community_chest cards """
        """ TODO create a result that this function can return to the server """
        comchest_list = get_community_chest()
        card = comchest_list[randint(1,17) - 1]
        return card

    def pay(self, amount, payer, recipient):
        """ TODO build out this function so that the amount goes from the payer to the recipient """
        """ TODO return the result to the players """
        return