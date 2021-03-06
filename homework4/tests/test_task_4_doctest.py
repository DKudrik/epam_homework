import pytest

from hw.task_4_doctest import fizzbuzz

test_data = [
    (0, []),
    (1, ["1"]),
    (
        15,
        [
            "1",
            "2",
            "fizz",
            "4",
            "buzz",
            "fizz",
            "7",
            "8",
            "fizz",
            "buzz",
            "11",
            "fizz",
            "13",
            "14",
            "fizzbuzz",
        ],
    ),
]


@pytest.mark.parametrize("input, output", test_data)
def test_fizzbuzz(input, output):
    result = fizzbuzz(input)
    assert result == output
