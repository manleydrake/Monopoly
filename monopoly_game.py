from random import randint


def start_game():
    """ TODO build out a function to initialize the game on the server and send initial game data to the users """
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
    return


def community_chest():
    """ TODO create Card class and an initializer for the community_chest cards """
    """ TODO create a result that this function can return to the server """
    return


def pay(amount, payer, recipient):
    """ TODO build out this function so that the amount goes from the payer to the recipient """
    """ TODO return the result to the players """
    return
