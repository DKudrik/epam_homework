import unittest
from unittest.mock import mock_open, patch
from hw.task03 import find_maximum_and_minimum


class TestFindMaxAndMin(unittest.TestCase):
    @staticmethod
    def open_mock(data):
        """An auxiliary method to prepare mock_open"""
        m_open = mock_open(read_data=data)
        m_open.return_value.__iter__.return_value = data.splitlines()
        return m_open

    def test_equal_values(self):
        data = '\n'.join(['1', '1', '1', '1'])
        m_open = self.open_mock(data)
        with patch('builtins.open', m_open):
            call = find_maximum_and_minimum('file_name')
        self.assertEqual(call[0], 1)
        self.assertEqual(call[1], 1)

    def test_set_1(self):
        """Testing with a min value at the start and the max at the end"""
        data = '\n'.join(['-1', '0', '2', '3'])
        m_open = self.open_mock(data)
        with patch('builtins.open', m_open):
            call = find_maximum_and_minimum('file_name')
        self.assertEqual(call[0], -1)
        self.assertEqual(call[1], 3)

    def test_set_2(self):
        """Testing with a min value at the end and the max at the start"""
        data = '\n'.join(['6', '0', '2', '-33'])
        m_open = self.open_mock(data)
        with patch('builtins.open', m_open):
            call = find_maximum_and_minimum('file_name')
        self.assertEqual(call[0], -33)
        self.assertEqual(call[1], 6)

    def test_set_3(self):
        """Testing with a min value followed with next min value"""
        data = '\n'.join(['0', '2', '-3', '-4'])
        m_open = self.open_mock(data)
        with patch('builtins.open', m_open):
            call = find_maximum_and_minimum('file_name')
        self.assertEqual(call[0], -4)
        self.assertEqual(call[1], 2)

    def test_set_4(self):
        """Testing with a max value followed with next max value"""
        data = '\n'.join(['0', '-1', '5', '6'])
        m_open = self.open_mock(data)
        with patch('builtins.open', m_open):
            call = find_maximum_and_minimum('file_name')
        self.assertEqual(call[0], -1)
        self.assertEqual(call[1], 6)


if __name__ == '__main__':
    unittest.main()
