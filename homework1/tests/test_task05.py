import unittest
from hw.task05 import find_maximal_subarray_sum


class TestFindMaximalSubarraySum(unittest.TestCase):
    def test_set_1(self):
        nums = [1, 3, -1, -3, 5, 3, 6, 7]
        k = 3
        result = find_maximal_subarray_sum(nums, k)
        self.assertEqual(result, 18)

    def test_set_2(self):
        """Testing with the set consisting of two biggest values at start"""
        nums = [9, 9, -1, -3, 5, 3, 6, 7]
        k = 3
        result = find_maximal_subarray_sum(nums, k)
        self.assertEqual(result, 25)


    def test_set_3(self):
        """Testing with the set consisting of equal values"""
        nums = [9, 9, 9, 9]
        k = 2
        result = find_maximal_subarray_sum(nums, k)
        self.assertEqual(result, 18)

    def test_set_4(self):
        """Testing with the set consisting of two smallest values at the end"""
        nums = [9, 7, 8, -5, -5]
        k = 3
        result = find_maximal_subarray_sum(nums, k)
        self.assertEqual(result, 24)


if __name__ == '__main__':
    unittest.main()
