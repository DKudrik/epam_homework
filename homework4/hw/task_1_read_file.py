"""
Write a function that gets file path as an argument.
Read the first line of the file.
If first line is a number return true if number in an interval [1, 3)*
and false otherwise.
In case of any error, a ValueError should be thrown.

Write a test for that function using pytest library.
You should create files required for the testing inside the test run and remove them after the test run.
(Opposite to previous homeworks when you used files created manually before the test.)

Definition of done:
 - function is created
 - function is properly formatted
 - function has positive and negative tests
 - tests do a cleanup and remove remove files generated by tests

You will learn:
 - how to test Exceptional cases
 - how to clean up after tests
 - how to check if file exists**
 - how to handle*** and raise**** exceptions in test. Use sample from the documentation.

* https://en.wikipedia.org/wiki/Interval_(mathematics)#Terminology
** https://docs.python.org/3/library/os.path.html
*** https://docs.python.org/3/tutorial/errors.html#handling-exceptions
**** https://docs.python.org/3/tutorial/errors.html#raising-exceptions
"""
import os


def read_magic_number(path: str) -> bool:
    """
    The func takes a file path as an argument and reads the first line of
    the file.
    If the first line is a number in an interval [1, 3), the func returns True
    and false otherwise.
    In case of any error, the func returns a ValueError.
    """
    try:
        os.path.exists(path)
        with open(path, "r") as fi:
            line = fi.readline()
        line = line.replace(" ", "")
        if line.isdigit():
            line = int(line)
            if 1 <= line < 3:
                return True
        return False
    except:
        raise ValueError("Файл не найден")
