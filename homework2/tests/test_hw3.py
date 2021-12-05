import unittest

from hw.hw3 import combinations


class TestCombinations(unittest.TestCase):
    def test_set_1(self):
        data = [1], [3]
        result = combinations(*data)
        self.assertEqual(result, [[1, 3]])

    def test_set_2(self):
        data = [1, 2], [3, 4]
        result = combinations(*data)
        self.assertEqual(result, [[1, 3], [1, 4], [2, 3], [2, 4]])


if __name__ == '__main__':
    unittest.main()
