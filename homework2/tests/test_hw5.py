import string
import unittest

from hw.hw5 import custom_range


class TestCustomRange(unittest.TestCase):
    def test_set_1(self):
        data = [1, 2, 3, 4, 5]
        result = custom_range(data, 3)
        self.assertEqual(result, [1, 2])

    def test_set_2(self):
        data = string.ascii_lowercase
        result = custom_range(data, "f", "k")
        self.assertEqual(result, ["f", "g", "h", "i", "j"])

    def test_set_3(self):
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        result = custom_range(data, 2, 12, 2)
        self.assertEqual(result, [2, 4, 6, 8, 10])

    def test_set_4(self):
        data = string.ascii_lowercase
        result = custom_range(data, "s", "c", -3)
        self.assertEqual(result, ["s", "p", "m", "j", "g", "d"])


if __name__ == "__main__":
    unittest.main()
