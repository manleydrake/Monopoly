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
        for i in range(len(players)):
            self.PLAYERS.append(Player('Player'+str(i+1)))

    def set_chance(self):
        self.CHANCE = list(get_chance())
        shuffle(self.CHANCE)

    def set_com_chest(self):
        self.COM_CHEST = list(get_community_chest())
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
        return '-----Player'+str(self.current_player+1)+'\'s Turn!-----~'

    @staticmethod
    def pay(amount, payer, recipient):
        payer.money -= amount
        recipient.money += amount
        if amount > 0:
            message = payer.name+' payed $'+str(amount)+' to '+recipient.name
        else:
            message = recipient.name+' payed $'+str(-amount)+' to '+payer.name
        return message

    def roll_dice(self):
        player = self.PLAYERS[self.current_player]
        die1 = randint(1, 6)
        die2 = randint(1, 6)
        self.latest_roll = die1 + die2
        die_file_1 = '/static/Images/dice_'+str(die1)+'.png'
        die_file_2 = '/static/Images/dice_'+str(die2)+'.png'
        self.doubles = False
        purchased_space = False
        messages = [player.name+' rolled '+str(self.latest_roll)]
        if self.turn_stage == 'move':
            if player.in_jail:
                if player.jail_cards > 0:
                    player.jail_rolls = 0
                    player.in_jail = False
                    player.jail_cards -= 1
                    messages.append(player.name+' used a "Get out of jail free" card')
                elif player.jail_rolls < 2:
                    if die1 == die2:
                        player.jail_rolls = 0
                        player.in_jail = False
                        messages.append(player.name+' rolled doubles and is out of jail')
                    else:
                        player.jail_rolls += 1
                        messages.append(player.name+' did not roll doubles and is still in jail')
                        messages.append(self.next_player())
                        return self.latest_roll, die_file_1, die_file_2, player.space_index, player.in_jail, \
                            purchased_space, messages
                else:
                    messages.append(player.name+' has rolled from jail for the third time and has posted bail')
                    messages.append(self.pay(50, player, Player('Bank')))
                    player.in_jail = False
                    player.jail_rolls = 0
            elif die1 == die2:
                self.doubles = True
                messages[0] = messages[0]+'   **DOUBLES**'
            purchased_space, movement_messages = self.move_player(player)
            for message in movement_messages:
                messages.append(message)
            if player.in_jail:
                self.doubles = False
        elif self.turn_stage == 'utility roll':
            messages.append(self.pay(10*self.latest_roll, player, self.PLAYERS[self.BOARD[player.space_index].owner]))
            self.turn_stage = 'move'
        if self.turn_stage == 'move' and not self.doubles:
            messages.append(self.next_player())
        return self.latest_roll, die_file_1, die_file_2, player.space_index, player.in_jail, purchased_space, messages

    def move_player(self, player):
        purchased_space = False
        messages = []
        player.space_index += self.latest_roll
        if player.space_index > 39:
            player.space_index = player.space_index - 40
            messages.append(player.name+' passed GO')
            messages.append(self.pay(200, Player('Bank'), player))
        elif player.space_index < 0:
            player.space_index = player.space_index + 40
        if player.space_index in [2, 17, 33]:
            messages.append(player.name+' landed on Community Chest')
            self.turn_stage = 'community chest'
        elif player.space_index in [7, 22, 36]:
            messages.append(player.name+' landed on Chance')
            self.turn_stage = 'chance'
        elif player.space_index == 30:
            messages.append(player.name+' landed on Go to Jail')
            player.space_index = 10
            player.in_jail = True
        elif player.space_index == 0:
            messages[0] = player.name+' landed on GO'
        elif player.space_index == 10:
            messages.append(player.name+' landed on Just Visiting')
        elif player.space_index == 20:
            messages.append(player.name+' landed on Free Parking')
        else:
            purchased_space, landed_messages = self.landed_on_space(player)
            for message in landed_messages:
                messages.append(message)
        return purchased_space, messages

    def chance(self):
        card = self.CHANCE.pop()
        if not self.CHANCE:
            self.set_chance()
        player_position, in_jail, purchased_space, messages = self.enact_card(card)
        return card, player_position, in_jail, purchased_space, messages

    def community_chest(self):
        card = self.COM_CHEST.pop()
        if not self.COM_CHEST:
            self.set_com_chest()
        player_position, in_jail, purchased_space, messages = self.enact_card(card)
        return card, player_position, in_jail, purchased_space, messages

    def enact_card(self, card):
        player = self.PLAYERS[self.current_player]
        purchased_space = False
        messages = []
        if card[1] == 'go to space':
            if isinstance(card[2], int):
                if card[2] == 0:
                    player.space_index = card[2]
                    messages.append(player.name+' was sent to GO')
                    messages.append(self.pay(200, Player('Bank'), player))
                else:
                    if card[2] <= player.space_index:
                        messages.append(player.name+' passed GO')
                        messages.append(self.pay(200, Player('Bank'), player))
                    player.space_index = card[2]
                    purchased_space, landed_messages = self.landed_on_space(player)
                    for message in landed_messages:
                        messages.append(message)
            else:
                if card[2] == 'utility':
                    if player.space_index < 12:
                        player.space_index = 12
                    elif player.space_index < 28:
                        player.space_index = 28
                    else:
                        messages.append(player.name+' passed GO')
                        messages.append(self.pay(200, Player('Bank'), player))
                        player.space_index = 12
                else:
                    if player.space_index < 15:
                        player.space_index = 15
                    elif player.space_index < 25:
                        player.space_index = 25
                    elif player.space_index < 35:
                        player.space_index = 35
                    else:
                        messages.append(player.name+' passed GO')
                        messages.append(self.pay(200, Player('Bank'), player))
                        player.space_index = 5
                space = self.BOARD[player.space_index]
                if space.owner is None:
                    if player.money >= space.buy_price:
                        space.owner = self.current_player
                        messages.append(player.space+' bought '+space.name)
                        messages.append(self.pay(space.buy_price, player, Player('Bank')))
                        player.properties.append(player.space_index)
                        purchased_space = True
                    else:
                        messages.append(player.name+' could not afford to buy '+space.name)
                elif space.owner != self.current_player:
                    if player.space_index in [12, 28]:
                        self.turn_stage = 'utility roll'
                    else:
                        messages.append(player.name+' owes double rent!')
                        messages.append(
                            self.pay(
                                2*space.house_multipliers[space.num_houses],
                                player,
                                self.PLAYERS[space.owner]
                             )
                        )
        elif card[1] == 'go to jail':
            messages.append(player.name+' was sent to Jail!')
            player.space_index = card[2]
            player.in_jail = True
        elif card[1] == 'money':
            messages.append(self.pay(card[2], Player('Bank'), player))
        elif card[1] == 'get out of jail free':
            messages.append('"Get out of jail free" card added to '+player.name+'\'s inventory')
            player.jail_cards += 1
        elif card[1] == 'movement':
            self.latest_roll = card[2]
            purchased_space, move_messages = self.move_player(player)
            for message in move_messages:
                messages.append(message)
        elif card[1] == 'repairs':
            for index in player.properties:
                if index in [5, 15, 25, 35]:
                    continue
                space = self.BOARD[index]
                if space.num_houses == 0:
                    continue
                elif space.num_houses < 5:
                    messages.append(player.name+' has '+str(space.num_houses)+' houses on '+space.name)
                    messages.append(self.pay(card[2][0]*space.num_houses, player, Player('Bank')))
                else:
                    messages.append(player.name+' has a hotel on '+space.name)
                    messages.append(self.pay(card[2][1], player, Player('Bank')))
        elif card[1] == 'pay players':
            for opponent in self.PLAYERS:
                if opponent.name != player.name:
                    messages.append(self.pay(card[2], player, opponent))

        if self.turn_stage != 'utility roll':
            self.turn_stage = 'move'
            if not self.doubles:
                messages.append(self.next_player())
        return player.space_index, player.in_jail, purchased_space, messages

    def landed_on_space(self, player):
        purchase_made = False
        messages = []
        space = self.BOARD[player.space_index]
        tax_spaces = ['Luxury Tax', 'Income Tax']
        
        messages.append(player.name+' landed on '+space.name)
        if player.space_index in player.properties:
            return purchase_made, messages
        
        if space.is_mortgaged:
            messages.append(space.name+' is mortgaged!')
        elif space.owner is None and space.name not in tax_spaces:
            if player.money >= space.buy_price:
                purchase_made = True
                space.owner = self.current_player
                messages.append(player.name+' bought '+space.name)
                messages.append(self.pay(space.buy_price, player, Player('Bank')))
                player.properties.append(player.space_index)
                if player.space_index in [5, 15, 25, 35]:
                    railroads = -1
                    for index in player.properties:
                        if index in [5, 15, 25, 35]:
                            railroads += 1
                    for index in [5, 15, 25, 35]:
                        if index in player.properties:
                            self.BOARD[index].num_houses = railroads
            else:
                messages.append(player.name+' cannot afford to buy '+space.name)
        elif space.name in tax_spaces:
            messages.append(self.pay(space.house_multipliers[space.num_houses], player, Player('Bank')))
        elif space.owner is not None:
            owner = self.PLAYERS[space.owner]
            messages.append(space.name+' is owned by '+owner.name+'!')
            if player.space_index in [12, 28]:
                if 12 in owner.properties and 28 in owner.properties:
                    messages.append(self.pay(10*self.latest_roll, player, owner))
                else:
                    messages.append(self.pay(4*self.latest_roll, player, owner))
            else:
                cost = space.house_multipliers[space.num_houses]
                messages.append(self.pay(cost, player, owner))
        return purchase_made, messages

    def reset(self):
        self.BOARD = []
        self.PLAYERS = []
        self.CHANCE = []
        self.COM_CHEST = []

        self.turn_stage = None
        self.current_player = None
        self.latest_roll = 0
        self.doubles = False
