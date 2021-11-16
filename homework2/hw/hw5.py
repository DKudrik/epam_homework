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


def custom_range(data, start=None, stop=None, step=None) -> List[str]:
    start = 0 if start is None else start
    stop = -1 if stop is None else stop
    step = 1 if step is None else step
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
