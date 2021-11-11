import unittest
from hw.task04 import check_sum_of_four


class TestCheckSumOfFour(unittest.TestCase):
    def test_no_match(self):
        call = check_sum_of_four([1], [-3], [2], [-2])
        self.assertEqual(call, 0)

    def test_1_match(self):
        call = check_sum_of_four([1], [-1], [2], [-2])
        self.assertEqual(call, 1)

    def test_2_matches(self):
        call = check_sum_of_four([1, -3], [-1, 3], [2, 5], [-2, 5])
        self.assertEqual(call, 2)


if __name__ == '__main__':
    unittest.main()
