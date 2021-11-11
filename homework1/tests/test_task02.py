import unittest

from hw.task02 import check_fib


class TestCheckFib(unittest.TestCase):
    def test_correct_seq(self):
        call = check_fib([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233])
        self.assertEqual(call, True)

    def test_wrong_seq_start(self):
        """ Testing the check_fib func with a wrong number at the beginning"""
        call = check_fib([11, 1, 1, 2, 3, 5, 8, 13, 21])
        self.assertEqual(call, False)

    def test_wrong_seq_mid(self):
        """ Testing the check_fib func with a wrong number in the middle"""
        call = check_fib([0, 1, 1, 2, 33, 5, 8, 13, 21])
        self.assertEqual(call, False)

    def test_wrong_seq_end(self):
        """ Testing the check_fib func with a wrong number at the end"""
        call = check_fib([0, 1, 1, 2, 3, 5, 8, 13, 222])
        self.assertEqual(call, False)

    def test_short_seq(self):
        """ Testing the check_fib func with a short sequence"""
        call = check_fib([5, 8])
        self.assertEqual(call, False)


if __name__ == '__main__':
    unittest.main()
