from random import randint, shuffle
from spaces_info import get_spaces_info
from cards_info import get_chance
from cards_info import get_community_chest


class Space:
    def __init__(self, name, buy_price, house_multipliers, mortgage, build_cost):
        self.name = name
        self.buy_price = buy_price
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
        self.in_jail = False
        self.jail_cards = 0
        self.jail_rolls = 0


def pay(amount, payer, recipient):
    payer.money -= amount
    recipient.money += amount
    print(amount)
    print(payer.name, payer.money)
    print(recipient.name, recipient.money)


class Game:
    BOARD = []
    PLAYERS = []
    CHANCE = []
    COM_CHEST = []

    turn_stage = None
    current_player = None
    latest_roll = 0
    doubles = False

    def init_board(self):
        for space in get_spaces_info():
            self.BOARD.append(Space(space[0], space[1], space[2], space[3], space[4]))

    def init_players(self, players):
        for player in players:
            self.PLAYERS.append(Player(player))

    def set_chance(self):
        self.CHANCE = get_chance()
        shuffle(self.CHANCE)

    def set_com_chest(self):
        self.COM_CHEST = get_community_chest()
        shuffle(self.COM_CHEST)

    def start_game(self, players):
        self.init_board()
        self.init_players(players)
        self.set_chance()
        self.set_com_chest()
        self.current_player = 0
        self.turn_stage = 'move'

    def next_player(self):
        self.current_player += 1
        if self.current_player == len(self.PLAYERS):
            self.current_player = 0

    def roll_dice(self):
        player = self.PLAYERS[self.current_player]
        die1 = randint(1, 6)
        die2 = randint(1, 6)
        self.latest_roll = die1 + die2
        die_file_1 = '/static/Images/dice_'+str(die1)+'.png'
        die_file_2 = '/static/Images/dice_'+str(die2)+'.png'
        self.doubles = False
        if self.turn_stage == 'move':
            if player.in_jail:
                if player.jail_cards > 0:
                    player.jail_rolls = 0
                    player.in_jail = False
                    player.jail_cards -= 1
                elif player.jail_rolls < 2:
                    if die1 == die2:
                        player.jail_rolls = 0
                        player.in_jail = False
                    else:
                        player.jail_rolls += 1
                        self.next_player()
                        return self.latest_roll, die_file_1, die_file_2, player.space_index, player.in_jail
                else:
                    pay(50, player, Player('bank'))
                    player.in_jail = False
                    player.jail_rolls = 0
            elif die1 == die2:
                self.doubles = True
            self.move_player(player)
            if player.in_jail:
                self.doubles = False
        elif self.turn_stage == 'utility roll':
            pay(10*self.latest_roll, player, self.PLAYERS[self.BOARD[player.space_index].owner])
            self.turn_stage = 'move'
        if self.turn_stage == 'move' and not self.doubles:
            self.next_player()
        return self.latest_roll, die_file_1, die_file_2, player.space_index, player.in_jail

    def move_player(self, player):
        player.space_index += self.latest_roll
        if player.space_index > 39:
            player.space_index = player.space_index - 40
            pay(200, Player('bank'), player)
        elif player.space_index < 0:
            player.space_index = player.space_index + 40
        if player.space_index in [2, 17, 33]:
            self.turn_stage = 'community chest'
        elif player.space_index in [7, 22, 36]:
            self.turn_stage = 'chance'
        elif player.space_index == 30:
            player.space_index = 10
            player.in_jail = True
        else:
            self.landed_on_space(player)

    def chance(self):
        card = self.CHANCE.pop()
        if len(self.CHANCE) == 0:
            self.set_chance()
        player_position, in_jail = self.enact_card(card)
        return card, player_position, in_jail

    def community_chest(self):
        card = self.COM_CHEST.pop()
        if len(self.COM_CHEST) == 0:
            self.set_com_chest()
        player_position, in_jail = self.enact_card(card)
        return card, player_position, in_jail

    def enact_card(self, card):
        player = self.PLAYERS[self.current_player]
        if card[1] == 'go to space':
            if isinstance(card[2], int):
                if card[2] <= player.space_index:
                    pay(200, Player('bank'), player)
                player.space_index = card[2]
                self.landed_on_space(player)
            else:
                if card[2] == 'utility':
                    if player.space_index < 12:
                        player.space_index = 12
                    elif player.space_index < 28:
                        player.space_index = 28
                    else:
                        pay(200, Player('bank'), player)
                        player.space_index = 12
                else:
                    if player.space_index < 15:
                        player.space_index = 15
                    elif player.space_index < 25:
                        player.space_index = 25
                    elif player.space_index < 35:
                        player.space_index = 35
                    else:
                        pay(200, Player('bank'), player)
                        player.space_index = 5
                space = self.BOARD[player.space_index]
                if space.owner is None and player.money >= space.buy_price:
                    space.owner = self.current_player
                    pay(space.buy_price, player, Player('bank'))
                    player.properties.append(player.space_index)
                elif space.owner != self.current_player:
                    if player.space_index in [12, 28]:
                        self.turn_stage = 'utility roll'
                    else:
                        self.landed_on_space(player)
                        self.landed_on_space(player)
        elif card[1] == 'go to jail':
            player.space_index = card[2]
            player.in_jail = True
        elif card[1] == 'money':
            pay(card[2], Player('bank'), player)
        elif card[1] == 'get out of jail free':
            player.jail_cards += 1
        elif card[1] == 'movement':
            self.latest_roll = card[2]
            self.move_player(player)
        elif card[1] == 'repairs':
            for index in player.properties:
                space = self.BOARD[index]
                if space.num_houses < 5:
                    pay(card[2][0]*space.num_houses, player, Player('bank'))
                else:
                    pay(card[2][1], player, Player('bank'))
        elif card[1] == 'pay players':
            for opponent in self.PLAYERS:
                if opponent.name != player.name:
                    pay(card[2], player, opponent)

        if self.turn_stage != 'utility roll':
            self.turn_stage = 'move'
            if not self.doubles:
                self.next_player()
        return player.space_index, player.in_jail

    def landed_on_space(self, player):
        if player.space_index in player.properties or \
                player.space_index in [0, 10, 20]:
            return
        space = self.BOARD[player.space_index]
        tax_spaces = ['Luxury Tax', 'Income Tax']
        if space.is_mortgaged:
            return
        elif space.owner is None and space.name not in tax_spaces:
            if player.money >= space.buy_price:
                space.owner = self.current_player
                pay(space.buy_price, player, Player('bank'))
                player.properties.append(player.space_index)
                if player.space_index in [5, 15, 25, 35]:
                    railroads = -1
                    for index in player.properties:
                        if index in [5, 15, 25, 35]:
                            railroads += 1
                    for index in [5, 15, 25, 35]:
                        if index in player.properties:
                            self.BOARD[index].num_houses = railroads
        elif space.name in tax_spaces:
            pay(space.house_multipliers[space.num_houses], player, Player('bank'))
        else:
            owner = self.PLAYERS[space.owner]
            if player.space_index in [12, 28]:
                if 12 in owner.properties and 28 in owner.properties:
                    pay(10*self.latest_roll, player, owner)
                else:
                    pay(4*self.latest_roll, player, owner)
            else:
                cost = space.house_multipliers[space.num_houses]
                pay(cost, player, owner)
