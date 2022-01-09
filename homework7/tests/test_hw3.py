import pytest

from hw.hw3 import tic_tac_toe_checker


test_data = [
    ([["x", "x", "x"], ["-", "o", "o"], ["x", "o", "x"]], "x wins!"),
    ([["x", "o", "x"], ["-", "x", "o"], ["x", "o", "x"]], "x wins!"),
    ([["x", "o", "x"], ["-", "o", "o"], ["x", "x", "x"]], "x wins!"),
    ([["x", "o", "x"], ["o", "o", "o"], ["o", "x", "x"]], "o wins!"),
    ([["x", "o", "o"], ["o", "o", "x"], ["o", "x", "x"]], "o wins!"),
    ([["x", "o", "x"], ["o", "o", "x"], ["o", "x", "o"]], "draw!"),
    ([["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]], "unfinished"),
    ([["-", "-", "o"], ["-", "-", "-"], ["-", "-", "x"]], "unfinished"),
    ([["x", "o", "o"], ["o", "-", "x"], ["o", "x", "x"]], "unfinished"),
]


@pytest.mark.parametrize("tree, result", test_data)
def test_tic_tac_toe_checker(tree, result):
    assert tic_tac_toe_checker(tree) == result
