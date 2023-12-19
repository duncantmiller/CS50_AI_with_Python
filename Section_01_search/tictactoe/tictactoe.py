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
    possible_actions = set()
    for row_idx, row in enumerate(board):
        for col_idx, col in enumerate(row):
            if col == EMPTY:
                possible_actions.add((row_idx, col_idx))
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
    winner_letter = horizontal_winner(board, None)
    winner_letter = vertical_winner(board, winner_letter)
    winner_letter = diagonal_winner(board, winner_letter)

    return winner_letter

def diagonal_winner(board, winner_letter):
    """
    Returns the diagonal winner of the game, if there is one.
    """
    diagonal1 = [board[0][0], board[1][1], board[2][2]]
    diagonal2 = [board[0][2], board[1][1], board[2][0]]
    if (diagonal1 or diagonal2) == ["X", "X", "X"]:
        winner_letter = "X"
    elif (diagonal1 or diagonal2) == ["O", "O", "O"]:
        winner_letter = "O"
    return winner_letter

def vertical_winner(board, winner_letter):
    """
    Returns the vertical winner of the game, if there is one.
    """
    first_column = [row[0] for row in board]
    second_column = [row[1] for row in board]
    third_column = [row[2] for row in board]
    if (first_column or second_column or third_column) == ["X", "X", "X"]:
        winner_letter = "X"
    elif (first_column or second_column or third_column) == ["O", "O", "O"]:
        winner_letter = "O"
    return winner_letter

def horizontal_winner(board, winner_letter):
    """
    Returns the horizontal winner of the game, if there is one.
    """
    for row in board:
        if row == ["X", "X", "X"]:
            winner_letter = "X"
        elif row == ["O", "O", "O"]:
            winner_letter = "O"
    return winner_letter

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    for row in board:
        for col in row:
            if col == EMPTY:
                return False
    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    score = 0
    if winner(board) == "X":
        score = 1
    elif winner(board) == "O":
        score = -1
    return score


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    player_letter = player(board)
    player_action = ()
    if player_letter == "X":
        for x_action in actions(board):
            result_board = result(board, x_action)
            if max_value(result_board) == 1:
                player_action = x_action
                if terminal(result_board):
                    return player_action
                for o_action in actions(result_board):
                    if min_value(result(board, o_action)) == 1:
                        player_action = ()
            if player_action != ():
                return player_action
        for x_action in actions(board):
            result_board = result(board, x_action)
            if max_value(result_board) == 0:
                player_action = x_action
                for o_action in actions(result_board):
                    if min_value(result(board, o_action)) == 1:
                        player_action = ()
            if player_action != ():
                return player_action
        for x_action in actions(board):
            player_action = x_action
            for o_action in actions(result(board, x_action)):
                if min_value(result(board, o_action)) == 1:
                    player_action = ()
            if player_action != ():
                return player_action

def max_value(board):
    """
    Returns the max value of the board.
    """
    if terminal(board):
        return utility(board)
    max_v = float("-inf")
    for action in actions(board):
        max_v = max(max_v, min_value(result(board, action)))
    return max_v

def min_value(board):
    """
    Returns the min value of the board.
    This is the value that the opponent will get.
    """
    if terminal(board):
        return utility(board)
    min_v = float("inf")
    for action in actions(board):
        min_v = min(min_v, max_value(result(board, action)))
    return min_v
