import unittest

from hw.hw2 import major_and_minor_elem


class TestMajorAndMinorElem(unittest.TestCase):
    def test_set_1(self):
        data = [2, 2, 1, 1, 1, 2, 2]
        result = major_and_minor_elem(data)
        self.assertEqual(result, (2, 1))

    def test_set_2(self):
        data = [1, 2, 3, 4, 4, 4, 4]
        result = major_and_minor_elem(data)
        self.assertEqual(result, (4, 1))


if __name__ == '__main__':
    unittest.main()
