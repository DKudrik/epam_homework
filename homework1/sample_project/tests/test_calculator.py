import unittest

from calculator.calc import check_power_of_2
from parameterized import parameterized


class TestCheckPowerOf2(unittest.TestCase):
    test_data = [
        (0, False),
        (-1, False),
        (-16, False),
        (12, False),
        (16, True),
        (65536, True),
        ("a", False),
    ]

    @parameterized.expand(test_data)
    def test_check_power_of_2_func(self, test_input, expected):
        self.assertEqual(check_power_of_2(test_input), expected)
