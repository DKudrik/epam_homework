import os

import pytest

from hw.hw3 import universal_file_counter


def set_up(data):
    """Aux func to prepare a test data"""
    test_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(test_dir)
    file_1 = open("test_file.txt", "a+")
    file_1.write(data)
    file_1.close()


def tear_down():
    """Aux func to clear the test data up"""
    os.remove("test_file.txt")


test_data = [
    ("a", None, 1),
    ("a\nb", None, 2),
    ("a\nb c", str.split, 3),
]


@pytest.mark.parametrize("data, tokenizer, expected_result", test_data)
def test_merge_sorted_files(data, tokenizer, expected_result):
    set_up(data)
    test_dir = os.path.dirname(os.path.abspath(__file__))
    result = universal_file_counter(test_dir, ".txt", tokenizer)
    tear_down()
    assert result == expected_result
