import os

import pytest

from hw.hw1 import merge_sorted_files


def set_up(data_1, data_2):
    """Aux func to prepare a test data"""
    test_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(test_dir)
    file_1 = open("test_file_1.txt", "a+")
    file_1.write(data_1)
    file_1.close()
    file_2 = open("test_file_2.txt", "a+")
    file_2.write(data_2)
    file_2.close()


def tear_down():
    """Aux func to clear the test data up"""
    os.remove("test_file_1.txt")
    os.remove("test_file_2.txt")


test_data = [
    ("1\n3\n5", "2\n4\n6", [1, 2, 3, 4, 5, 6]),
    ("1\n3\n5", "-4", [-4, 1, 3, 5]),
    ("1\n3\n5", "", [1, 3, 5]),
]


@pytest.mark.parametrize("data_1, data_2, expected_result", test_data)
def test_merge_sorted_files(data_1, data_2, expected_result):
    set_up(data_1, data_2)
    result = list(merge_sorted_files(["test_file_1.txt", "test_file_2.txt"]))
    tear_down()
    assert result == expected_result
