"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers,
    and returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""
from typing import Sequence


def check_fib(data: Sequence[int]) -> bool:
    if len(data) < 3:
        return False
    a = data[0]
    b = data[1]
    c = data[2]
    while data[:-2]:
        if not a + b == c:
            return False
        try:
            a, b = b, c
            data = data[1:]
            c = data[2]
        except IndexError:
            continue
    return True
