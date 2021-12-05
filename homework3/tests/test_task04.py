import unittest

from parameterized import parameterized

from hw.task04.task04 import is_armstrong


class TestIsArmstrong(unittest.TestCase):
    armstrong_nums = [(1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,),
                      (9,), (153,), (370,), (371,), (407,), (1634,),
                      (8208,), (9474,), (54748,), (92727,)]

    non_armstrong_nums = [(11,), (12,), (13,), (14,), (15,), (16,), (17,),
                          (18,), (19,)]

    @parameterized.expand(armstrong_nums)
    def test_with_armstrong_nums(self, arg_1):
        self.assertEqual(is_armstrong(arg_1), True)

    @parameterized.expand(non_armstrong_nums)
    def test_with_non_armstrong_nums(self, arg_1):
        self.assertEqual(is_armstrong(arg_1), False)


if __name__ == "__main__":
    unittest.main()
