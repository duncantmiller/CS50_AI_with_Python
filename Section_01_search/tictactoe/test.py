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

    def test_actions_for_empty(self):
        board = [[EMPTY, EMPTY, EMPTY],
                 [EMPTY, EMPTY, EMPTY],
                 [EMPTY, EMPTY, EMPTY]]
        self.assertEqual(actions(board), ((0, 0), (0, 1), (0, 2),
                                          (1, 0), (1, 1), (1, 2),
                                          (2, 0), (2, 1), (2, 2)))

    def test_actions_for_one(self):
        board = [["X", "O", "X",],
                 ["O", EMPTY, "O"],
                 ["X", "O", "X"]]
        self.assertEqual(actions(board), ((1, 1),))

    def test_actions_for_two(self):
        board = [[EMPTY, "O", "X",],
                 ["O", EMPTY, "O"],
                 ["X", "O", "X"]]
        self.assertEqual(actions(board), ((0, 0), (1, 1),))
if __name__ == '__main__':
    unittest.main()
