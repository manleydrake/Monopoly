from random import randint
from spaces_info import get_spaces_info
from cards_info import get_chance
from cards_info import get_community_chest


class Space:
    def __init__(self, name, base_rent, house_multipliers, mortgage, build_cost):
        self.name = name
        self.base_rent = base_rent
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


BOARD = []
PLAYERS = []


def init_board():
    for space in get_spaces_info():
        BOARD.append(Space(space[0], space[1], space[2], space[3], space[4]))


def init_players(players):
    for player in players:
        PLAYERS.append(Player(player))


def start_game(players):
    """ TODO build out a function to initialize the game on the server and send initial game data to the users """
    init_board()
    init_players(players)
    return


def roll_dice():
    die1 = randint(1, 6)
    die2 = randint(1, 6)
    die_file_1 = '/static/Images/dice_'+str(die1)+'.png'
    die_file_2 = '/static/Images/dice_'+str(die2)+'.png'
    return die1+die2, die_file_1, die_file_2


def chance():
    """ TODO create Card class and an initializer for the chance cards """
    """ TODO create a result that this function can return to the server """
    chance_list = cards_info.get_chance()
    card = chance_list[randint(1,17) - 1]
    return card


def community_chest():
    """ TODO create Card class and an initializer for the community_chest cards """
    """ TODO create a result that this function can return to the server """
    return


def pay(amount, payer, recipient):
    """ TODO build out this function so that the amount goes from the payer to the recipient """
    """ TODO return the result to the players """
    return
