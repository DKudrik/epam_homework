"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.

Write a function that accept any iterable of unique values and then
it behaves as range function:


import string


assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']

"""
from typing import AnyStr, List


def custom_range(data, *args) -> List[str]:
    """
    The first arg is an iterable object. In case the second arg is the last
     one - it's supposed to be a start value, else: the second arg is a start
     value, the third one is a stop value and the last one is a step.

     ---Example---
     custom_range(string.ascii_lowercase, 'f') == ['a', 'b', 'c', 'd', 'e']
     custom_range(string.ascii_lowercase, 'g', 'k') == ['g', 'h', 'i', 'j']
     custom_range(string.ascii_lowercase, 'p', 'h', -2) == ['p', 'n', 'l', 'j']
    """
    if len(args) == 1:
        start = 0
        stop = args[0]
        step = 1
    elif len(args) == 2:
        start = args[0]
        stop = args[1]
        step = 1
    elif len(args) == 3:
        start = args[0]
        stop = args[1]
        step = args[2]
    if step < 1:
        data = data[::-1]
        step = abs(step)
    result = []
    index = 0
    for item in data:
        if item == start:
            result.clear()
            result.append(item)
            index = 1
            continue
        elif item == stop:
            return result
        else:
            if index % step == 0:
                result.append(item)
            index += 1
    return result
