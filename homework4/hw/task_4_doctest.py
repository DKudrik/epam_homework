"""
Write a function that takes a number N as an input and returns N FizzBuzz numbers*
Write a doctest for that function.

Definition of done:
 - function is created
 - function is properly formatted
 - function has doctests
 - doctests are run with pytest command

You will learn:
 - the most common test task for developers
 - how to write doctests
 - how to run doctests


assert fizzbuzz(5) == ["1", "2", "fizz", "4", "buzz"]

* https://en.wikipedia.org/wiki/Fizz_buzz
** Энциклопедия профессора Фортрана page 14, 15, "Робот Фортран, чисть картошку!"
"""
from typing import List
import doctest

def fizzbuzz(n: int) -> List[str]:
    """Accepts a number N. For num in range(N) appends to a resulting lust
     'fizz' if num%3 == 0 or 'buzz' if num%5==0 or 'fizzbuzz'
     if N%3 == 0 or N%3 = 0 else appends a num.

    >>> fizzbuzz(10)
    ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz']

    """
    result = []
    for num in range(1, n + 1):
        if num % 15 == 0:
            result.append("fizzbuzz")
        elif num % 3 == 0:
            result.append("fizz")
        elif num % 5 == 0:
            result.append("buzz")
        else:
            result.append(str(num))
    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
