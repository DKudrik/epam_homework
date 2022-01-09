"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"

Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished"

    [[-, -, o],
     [-, o, o],
     [x, x, x]]

     Return value should be "x wins!"

"""
from collections import Counter
from typing import List


def tic_tac_toe_checker(board: List[List]) -> str:
    """
    Function puts all data in all possible win positions (vert_left, hor_right,
    axial_1 etc). Then it checks if there are three "x" or "o" in any of
    positions. At the same time it checks if there is free space squares and
    changes the flag "is_free_space" accordingly. If there are no three chars
    and free space flag is True - it returns "unfinished", if no free space -
    returns "draw".
    """
    vert_left = [board[0][0], board[1][0], board[2][0]]
    vert_mid = [board[0][1], board[1][1], board[2][1]]
    vert_right = [board[0][2], board[1][2], board[2][2]]
    hor_upper = [board[0][0], board[0][1], board[0][2]]
    hor_mid = [board[1][0], board[1][1], board[1][2]]
    hor_lower = [board[2][0], board[2][1], board[2][2]]
    axial_1 = [board[2][0], board[1][1], board[0][2]]
    axial_2 = [board[0][0], board[1][1], board[2][2]]

    possible_win_positions = (
        vert_left,
        vert_mid,
        vert_right,
        hor_upper,
        hor_mid,
        hor_lower,
        axial_1,
        axial_2,
    )
    is_free_space = False
    for pos in possible_win_positions:
        most_common_char_count = Counter(pos).most_common(1)
        if "-" in pos:
            is_free_space = True
        if most_common_char_count[0][1] == 3 and most_common_char_count[0][0] != "-":
            return f"{most_common_char_count[0][0]} wins!"
    if is_free_space:
        return "unfinished"
    return "draw!"
