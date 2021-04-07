import unittest
import monopoly_game


class TestMonopolyGame(unittest.TestCase):
    def test_space_class(self):
        name = 'test1'
        base_rent = 123
        house_multipliers = [1, 5, 10]
        mortgage = 53
        build_cost = 12535
        num_houses = 0
        test1 = monopoly_game.Space(name, base_rent, house_multipliers, mortgage, build_cost)
        self.assertEqual(name, test1.name)
        self.assertEqual(base_rent, test1.base_rent)
        self.assertEqual(house_multipliers, test1.house_multipliers)
        self.assertEqual(mortgage, test1.mortgage)
        self.assertEqual(build_cost, test1.build_cost)
        self.assertEqual(num_houses, test1.num_houses)
        self.assertFalse(test1.is_mortgaged)
        self.assertIsNone(test1.owner)

    def test_player_class(self):
        name = 'player1'
        money = 1500
        properties = []
        space_index = 0
        test1 = monopoly_game.Player(name)
        self.assertEqual(name, test1.name)
        self.assertEqual(money, test1.money)
        self.assertEqual(properties, test1.properties)
        self.assertEqual(space_index, test1.space_index)

    def test_init_board(self):
        monopoly_game.init_board()
        self.assertEqual(40, len(monopoly_game.BOARD))
        self.assertEqual('GO', monopoly_game.BOARD[0].name)
        self.assertEqual('Boardwalk', monopoly_game.BOARD[39].name)

    def test_init_players(self):
        players = ['test1', 'test2', 'test3']
        monopoly_game.init_players(players)
        self.assertEqual('test1', monopoly_game.PLAYERS[0].name)
        self.assertEqual('test2', monopoly_game.PLAYERS[1].name)
        self.assertEqual('test3', monopoly_game.PLAYERS[2].name)

    def test_roll_dice(self):
        result, file_1, file_2 = monopoly_game.roll_dice()
        roll_1 = int(file_1[-5])
        roll_2 = int(file_2[-5])
        self.assertEqual(result, roll_1+roll_2)


if __name__ == '__main__':
    unittest.main()
