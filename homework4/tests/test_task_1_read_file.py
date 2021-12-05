import os

import pytest

from hw.task_1_read_file import read_magic_number


def set_up(data):
    """Aux func to prepare a test data"""
    test_file = open("test_file.txt", "w+")
    test_file.write(data)
    test_file.close()


def tear_down():
    """Aux func to clear the test data up"""
    os.remove("test_file.txt")


test_data = [
    ("1", True),
    ("     1", True),
    ("1     ", True),
    ("   1   ", True),
    ("3", False),
    ("   3", False),
    ("3    ", False),
    ("   3   ", False),
    ("3a", False),
    ("  3a ", False),
    ("b", False),
    ("\n1", False),
]


@pytest.mark.parametrize("data, expected_result", test_data)
def test_read_magic_number(data, expected_result):
    set_up(data)
    result = read_magic_number("test_file.txt")
    tear_down()
    assert result is expected_result
