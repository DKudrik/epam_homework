import random
import unittest

from hw.task01.task01 import plus


class TestCache(unittest.TestCase):
    def test_plus(self):
        res_1, res_2, res_3, res_4 = (
            plus(random.randint(1, 10), random.randint(1, 10)) for _ in range(4)
        )
        self.assertTrue(
            res_1 is res_2 and res_2 is res_3 and res_3 is not res_4)


if __name__ == "__main__":
    unittest.main()
