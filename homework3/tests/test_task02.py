import time
import unittest

from hw.task02.task02 import pool_handler


class TestSlowCalculate(unittest.TestCase):
    def test_slow_calculate(self):
        start = time.time()
        pool_handler()
        finish = time.time()
        total_time = finish - start
        self.assertTrue(total_time < 60)


if __name__ == '__main__':
    unittest.main()
