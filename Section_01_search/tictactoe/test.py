import unittest
from tictactoe import *

class TestPlayerFunction(unittest.TestCase):

    def test_next_player_after_x(self):
        board = [["X"]]
        self.assertEqual(player(board), "O", "player after X should be O")

    def test_next_player_after_o(self):
        board = [["O"]]
        self.assertEqual(player(board), "X", "player after O should be X")

    def test_first_player(self):
        board = [[]]
        self.assertEqual(player(board), "X", "First player should be X")

if __name__ == '__main__':
    unittest.main()
