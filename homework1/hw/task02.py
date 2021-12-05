"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers,
    and returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""
from math import sqrt
from typing import Sequence


def is_perfect_square(x):
    s = int(sqrt(x))
    return s * s == x


def check_fib(data: Sequence[int]) -> bool:
    if len(data) < 3:
        return False
    result = []
    for num in data:
        if num < 0:
            return False
        result.append(
            is_perfect_square(5 * num ** 2 + 4)
            or is_perfect_square(5 * num ** 2 - 4)
        )
    return all(result)
