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
        self.assertEqual(actions(board), {(0, 0), (0, 1), (0, 2),
                                          (1, 0), (1, 1), (1, 2),
                                          (2, 0), (2, 1), (2, 2)})

    def test_actions_for_one(self):
        board = [["X", "O", "X",],
                 ["O", EMPTY, "O"],
                 ["X", "O", "X"]]
        self.assertEqual(actions(board), {(1, 1)})

    def test_actions_for_two(self):
        board = [[EMPTY, "O", "X",],
                 ["O", EMPTY, "O"],
                 ["X", "O", "X"]]
        self.assertEqual(actions(board), {(0, 0), (1, 1)})

    def test_result(self):
        board = [[EMPTY, "O", "X",],
                 ["O", EMPTY, "O"],
                 ["X", "O", "X"]]
        action = (0, 0)
        self.assertEqual(result(board, action), [["X", "O", "X",],
                                                 ["O", EMPTY, "O"],
                                                 ["X", "O", "X"]])

    def test_result_exception_for_taken_coord(self):
        board = [[EMPTY, "O", "X",],
                 ["O", EMPTY, "O"],
                 ["X", "O", "X"]]
        action = (0, 1)
        with self.assertRaises(Exception):
            result(board, action)

    def test_result_exception_for_invalid_coord(self):
        board = [[EMPTY, "O", "X",],
                 ["O", EMPTY, "O"],
                 ["X", "O", "X"]]
        action = (9, 9)
        with self.assertRaises(Exception):
            result(board, action)

    def test_result_should_not_change_original_board(self):
        board = [[EMPTY, "O", "X",],
                 ["O", EMPTY, "O"],
                 ["X", "O", "X"]]
        action = (0, 0)
        self.assertEqual(result(board, action), [["X", "O", "X",],
                                                 ["O", EMPTY, "O"],
                                                 ["X", "O", "X"]])
        self.assertEqual(board, [[EMPTY, "O", "X",],
                                 ["O", EMPTY, "O"],
                                 ["X", "O", "X"]])

    def test_winner_for_none(self):
        board = [[EMPTY, "O", "X",],
                 ["O", EMPTY, "O"],
                 ["X", "O", "X"]]
        self.assertEqual(winner(board), None)

    def test_winner_for_tie(self):
        board = [["O", "X", "O",],
                 ["O", "X", "X"],
                 ["X", "O", "X"]]
        self.assertEqual(winner(board), None)

    def test_winner_for_row(self):
        board = [["X", "X", "X",],
                 ["O", EMPTY, "O"],
                 ["X", "O", "X"]]
        self.assertEqual(winner(board), "X")

    def test_winner_for_row1(self):
        board = [["X", EMPTY, "X",],
                 ["O", "X", "O"],
                 ["X", "O", "X"]]
        self.assertEqual(winner(board), "X")

    def test_winner_for_column(self):
        board = [["O", "O", "X",],
                 ["O", EMPTY, "O"],
                 ["O", "O", "X"]]
        self.assertEqual(winner(board), "O")

    def test_winner_for_column1(self):
        board = [["O", "O", "X",],
                 [EMPTY, "O", "O"],
                 ["O", "O", "X"]]
        self.assertEqual(winner(board), "O")

    def test_winner_for_diagonal1(self):
        board = [["X", EMPTY, EMPTY,],
                 ["O", "X", "O"],
                 [EMPTY, "O", "X"]]
        self.assertEqual(winner(board), "X")

    def test_winner_for_diagonal2(self):
        board = [[EMPTY, EMPTY, "O",],
                 ["X", "O", "X"],
                 ["O", "X", EMPTY]]
        self.assertEqual(winner(board), "O")

    def test_terminal_for_empty(self):
        board = [[EMPTY, "O", "X",],
                 ["O", EMPTY, "O"],
                 ["X", "O", "X"]]
        self.assertFalse(terminal(board))

    def test_terminal_for_winner(self):
        board = [["X", "O", "X",],
                 ["O", "X", "O"],
                 ["X", "O", "X"]]
        self.assertTrue(terminal(board))

    def test_terminal_for_tie(self):
        board = [["O", "X", "O",],
                 ["O", "X", "X"],
                 ["X", "O", "X"]]
        self.assertTrue(terminal(board))

    def test_utility_for_x(self):
        board = [["X", "X", "X",],
                 ["O", EMPTY, "O"],
                 ["X", "O", "X"]]
        self.assertEqual(utility(board), 1)

    def test_utility_for_o(self):
        board = [["O", "O", "X",],
                 ["O", EMPTY, "O"],
                 ["O", "O", "X"]]
        self.assertEqual(utility(board), -1)

    def test_utility_for_tie(self):
        board = [["O", "X", "O",],
                 ["O", "X", "X"],
                 ["X", "O", "X"]]
        self.assertEqual(utility(board), 0)

    def test_minimax_for_terminal(self):
        board = [["X", "O", "X",],
                 ["O", "X", "O"],
                 ["X", "O", "X"]]
        self.assertEqual(minimax(board), None)

    def test_minimax_for_simple_win(self):
        board = [["X", "O", "X",],
                 ["O", EMPTY, "O"],
                 ["X", "O", "X"]]
        self.assertEqual(minimax(board), (1, 1))

    def test_minimax_for_simple_tie(self):
        board = [["X", "O", "X",],
                 [EMPTY, "O", "O"],
                 ["O", "X", "X"]]
        self.assertEqual(minimax(board), (1, 0))

    def test_minimax_for_begin(self):
        board = [[EMPTY, EMPTY, EMPTY],
                 [EMPTY, EMPTY, EMPTY],
                 [EMPTY, EMPTY, EMPTY]]
        self.assertNotEqual(minimax(board), None)

    def test_minimax_for_mid_win(self):
        board = [[EMPTY, "O", "O"],
                 ["X", "X", EMPTY],
                 [EMPTY, EMPTY, EMPTY]]
        self.assertEqual(minimax(board), (1, 2))

    def test_minimax_for_mid_defense(self):
        board = [[EMPTY, "O", "O"],
                 [EMPTY, "X", EMPTY],
                 [EMPTY, "X", EMPTY]]
        self.assertEqual(minimax(board), (0, 0))

    def test_minimax_for_third_move(self):
        board = [[EMPTY, EMPTY, "O"],
                 [EMPTY, "X", EMPTY],
                 [EMPTY, EMPTY, EMPTY]]
        self.assertNotEqual(minimax(board), None)

    def test_minimax_for_game(self):
        board = [["X", "O", "X"],
                 ["O", "X", EMPTY],
                 [EMPTY, EMPTY, EMPTY]]
        self.assertNotEqual(minimax(board), None)

if __name__ == '__main__':
    unittest.main()
