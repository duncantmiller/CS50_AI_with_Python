import unittest
from tictactoe import *

class TestPlayerFunction(unittest.TestCase):

    def test_next_player_after_x(self):
        board = []
        next_player = "X"
        self.assertEqual(player(board), "O", "Next player after X should be O")

    def test_next_player_after_o(self):
        board = []
        next_player = "O"
        self.assertEqual(player(board), "X", "Next player after O should be X")


if __name__ == '__main__':
    unittest.main()
