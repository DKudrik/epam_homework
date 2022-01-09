import pytest

from hw.hw2 import backspace_compare

test_data = [
    ("#", "", True),
    ("ab###", "", True),
    ("ab#c", "ad#c", True),
    ("a##c", "#a#c", True),
    ("a#c", "b", False),
    ("aa", "aac#", True),
    ("abc", "abc###abc", True),
]


@pytest.mark.parametrize("first, second, result", test_data)
def test_backspace_compare(first, second, result):
    assert backspace_compare(first, second) == result
