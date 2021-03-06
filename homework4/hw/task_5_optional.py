"""
This task is optional.

Write a generator that takes a number N as an input
and returns a generator that yields N FizzBuzz numbers*
Don't use any ifs, you can find an approach for the implementation in this video**.


Definition of done:
 - function is created
 - function is properly formatted
 - function has tests


>>> list(fizzbuzz(5))
["1", "2", "fizz", "4", "buzz"]

* https://en.wikipedia.org/wiki/Fizz_buzz
** https://www.youtube.com/watch?v=NSzsYWckGd4
"""
from typing import Generator, List


def fizzbuzz(n: int) -> Generator[str, None, None]:
    """ The func takes a number N as an input and returns a generator
    that yields N FizzBuzz numbers

    >>> list(fizzbuzz(5))
    ["1", "2", "fizz", "4", "buzz"]
    """
    for num in range(1, n + 1):
        yield "fizz" * (not num % 3) + "buzz" * (not num % 5) or str(num)


if __name__ == "__main__":
    import doctest

    doctest.testmod()


# при запуске доктеста почему-то результат в одиночных кавычках, хотя добавляю
# в двойных. В задаче с доктестом такой проблемы не было, тесты проходят норм.