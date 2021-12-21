"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.

"""
from contextlib import contextmanager


class Suppressor:
    """
    >>> with Suppressor(IndexError):
    ...    [][2]
    """

    def __init__(self, exception):
        self.exception = exception

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        return isinstance(exc_value, self.exception)


@contextmanager
def suppressor(error_name):
    """
    >>> with suppressor(IndexError):
    ...    [][2]
    """
    try:
        yield
    except error_name:
        pass
