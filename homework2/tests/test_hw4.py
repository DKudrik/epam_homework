import unittest

from hw.hw4 import multiply


class TestCacheFuncEqualValues(unittest.TestCase):
    def test_set_equal(self):
        data = 100, 200
        multiply(*data)
        multiply(*data)
        self.assertEqual(multiply.invocations, 1)


class TestCacheFuncDiffValues(unittest.TestCase):
    def test_set_different(self):
        data_1 = 100, 200
        data_2 = 23, 34
        multiply(*data_1)
        multiply(*data_2)
        self.assertEqual(multiply.invocations, 2)


if __name__ == "__main__":
    unittest.main()
