chance_list = [  # Chance
    ('Advance to Go (Collect $200).', 'go to space', 0),
    ('Advance to Illinois Ave.', 'go to space', 24),
    ('Advance token to nearest Utility. If unowned, you may buy it from the Bank. '
        'If owned, throw dice and pay owner a total ten times the amount thrown.', 'go to space', 'utility'),
    ('Advance token to the nearest Railroad and pay owner twice the rental to which he/she is otherwise entitled. '
        'If Railroad is unowned, you may buy it from the Bank.', 'go to space', 'railroad'),
    ('Advance token to the nearest Railroad and pay owner twice the rental to which he/she is otherwise entitled. '
        'If Railroad is unowned, you may buy it from the Bank.', 'go to space', 'railroad'),
    ('Advance to St. Charles Place – if you pass Go, collect $200.', 'go to space', 11),
    ('Bank pays you dividend of $50.', 'money', 50),
    ('Get out of Jail free – this card may be kept until needed, or traded/sold.', 'get out of jail free', None),
    ('Go back 3 spaces.', 'movement', -3),
    ('Go directly to Jail – do not pass Go, do not collect $200.', 'go to jail', 10),
    ('Make general repairs on all your property – for each house pay $25 – for each hotel $100.', 'repairs', [25, 100]),
    ('Pay poor tax of $15.', 'money', -15),
    ('Take a trip to Reading Railroad – if you pass Go collect $200.', 'go to space', 5),
    ('Take a walk on the Boardwalk – advance token to Boardwalk.', 'go to space', 39),
    ('You have been elected chairman of the board – pay each player $50. ', 'pay players', 50),
    ('Your building loan matures – collect $150.', 'money', 150),
    ('You have won a crossword competition - collect $100.', 'money', 100)
]


def get_chance():
    return chance_list


community_chest_list = [  # Community Chest
    ('Advance to Go (Collect $200).', 'go to space', 0),
    ('Bank error in your favor – collect $75.', 'money', 75),
    ('Doctor\'s fees – Pay $50.', 'money', -50),
    ('Get out of jail free – this card may be kept until needed, or sold.', 'get out of jail free', None),
    ('Go to jail – go directly to jail – Do not pass Go, do not collect $200.', 'go to jail', 10),
    ('It is your birthday. Collect $10 from each player.', 'pay players', -10),
    ('Grand Opera Night – collect $50 from every player for opening night seats.', 'pay players', -50),
    ('Income Tax refund – collect $20.', 'money', 20),
    ('Life Insurance Matures – collect $100.', 'money', 100),
    ('Pay Hospital Fees of $100.', 'money', -100),
    ('Pay School Fees of $50.', 'money', -50),
    ('Receive $25 Consultancy Fee.', 'money', 25),
    ('You are assessed for street repairs – $40 per house, $115 per hotel.', 'repairs', [40, 115]),
    ('You have won second prize in a beauty contest– collect $10.', 'money', 10),
    ('You inherit $100.', 'money', 100),
    ('From sale of stock you get $50.', 'money', 50),
    ('Holiday Fund matures - Receive $100.', 'money', 100)
]


def get_community_chest():
    return community_chest_list
