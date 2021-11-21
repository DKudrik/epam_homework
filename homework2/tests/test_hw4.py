import unittest

from hw.hw4 import multiply


class TestCacheFunc(unittest.TestCase):
    def test_set(self):
        data = 100, 200
        val_1 = multiply(*data)
        val_2 = multiply(*data)
        self.assertIs(val_1, val_2)


if __name__ == "__main__":
    unittest.main()
