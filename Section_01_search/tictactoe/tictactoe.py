"""
Tic Tac Toe Player
"""

import math
import pdb
import copy

X = "X"
O = "O"
EMPTY = None

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = 0
    o_count = 0
    for row in board:
        for col in row:
            if col == "X":
                x_count += 1
            elif col == "O":
                o_count += 1
    next_player = "X" if o_count >= x_count else "O"
    return next_player

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = ()
    for row_idx, row in enumerate(board):
        for col_idx, col in enumerate(row):
            if col == EMPTY:
                possible_actions += ((row_idx, col_idx),)
    return possible_actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)
    if action[0] > 2 or action[1] > 2 or action[0] < 0 or action[1] < 0:
        raise Exception("Invalid action")
    for row_idx, row in enumerate(board):
        for col_idx, col in enumerate(row):
            if (row_idx, col_idx) == action:
                if col == EMPTY:
                    new_board[row_idx][col_idx] = player(board)
                else:
                    raise Exception("Invalid action")
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    winner = None
    for row_idx, row in enumerate(board):
        if row == ["X", "X", "X"]:
            winner = "X"
        elif row == ["O", "O", "O"]:
            winner = "O"
        for col_idx, col in enumerate(row):
            if col == ["X", "X", "X"]:
                winner = "X"
            elif col == ["O", "O", "O"]:
                winner = "O"
    return winner

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
