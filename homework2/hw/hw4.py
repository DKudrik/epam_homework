"""
Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.


def func(a, b):
    return (a ** b) ** 2


cache_func = cache(func)

some = 100, 200

val_1 = cache_func(*some)
val_2 = cache_func(*some)

assert val_1 is val_2

"""
from collections import defaultdict
from typing import Callable


def cache_func(func: Callable) -> Callable:
    cache = defaultdict()
    def wrapper(*args, **kwargs):
        key = " ".join(str(i) for i in [func.__name__, str(args), str(kwargs)])
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]

    return wrapper


@cache_func
def multiply(a: int, b: int) -> int:
    return a * b
