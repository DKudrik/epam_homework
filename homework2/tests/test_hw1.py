import unittest
from unittest.mock import mock_open, patch

from hw.hw1 import (count_non_ascii_chars, count_punctuation_chars,
                    get_longest_diverse_words, get_rarest_char,
                    get_most_common_non_ascii_char)


def open_mock(data):
    """An auxiliary method to prepare mock_open"""
    m_open = mock_open(read_data=data)
    m_open.return_value.__iter__.return_value = data.splitlines()
    return m_open


class TestGetLongestDiverseWords(unittest.TestCase):
    def test_set_1(self):
        """Testing with the correct set of 11 words. The first item 'a' in the
        data is supposed to be out of place"""
        data = """a ab abc abcd abcde abcdef abcdefg abcdefgh abcdefghi
               abcdefghij abcdefghijk"""
        m_open = open_mock(data)
        with patch("builtins.open", m_open):
            result = get_longest_diverse_words("file_name")
        self.assertEqual(
            result,
            [
                "ab",
                "abc",
                "abcd",
                "abcde",
                "abcdef",
                "abcdefg",
                "abcdefgh",
                "abcdefghi",
                "abcdefghij",
                "abcdefghijk",
            ],
        )

    def test_set_2(self):
        """Testing with the wrong set of 11 words. The first item 'a' in the
        comparison data is wrong"""
        data = """a ab abc abcd abcde abcdef abcdefg abcdefgh abcdefghi
               abcdefghij abcdefghijk"""
        m_open = open_mock(data)
        with patch("builtins.open", m_open):
            result = get_longest_diverse_words("file_name")
        self.assertNotEqual(
            result,
            [
                "a",
                "abc",
                "abcd",
                "abcde",
                "abcdef",
                "abcdefg",
                "abcdefgh",
                "abcdefghi",
                "abcdefghij",
                "abcdefghijk",
            ],
        )


class TestGetRarestChar(unittest.TestCase):
    def test_correct_set_1(self):
        data = "aaa bb ccc dddd /"
        m_open = open_mock(data)
        with patch("builtins.open", m_open):
            result = get_rarest_char("file_name")
        self.assertEqual(result, "/")

    def test_correct_set_2(self):
        data = "aaa bb . ccc dddd"
        m_open = open_mock(data)
        with patch("builtins.open", m_open):
            result = get_rarest_char("file_name")
        self.assertEqual(result, ".")


class TestCountPunctuationChars(unittest.TestCase):
    def test_set_1(self):
        data = ". ? ! , ; : - ( ) \" ' „ “"
        m_open = open_mock(data)
        with patch("builtins.open", m_open):
            result = count_punctuation_chars("file_name")
        self.assertEqual(result, 13)


class TestCountNonAsciiChars(unittest.TestCase):
    def test_correct_set(self):
        data = "£ ¤"
        m_open = open_mock(data)
        with patch("builtins.open", m_open):
            result = count_non_ascii_chars("file_name")
        self.assertEqual(result, 2)

    def test_wrong_set(self):
        data = "a b c"
        m_open = open_mock(data)
        with patch("builtins.open", m_open):
            result = count_non_ascii_chars("file_name")
        self.assertEqual(result, 0)


class TestGetMostCommonNonAsciiChar(unittest.TestCase):
    def test_correct_set(self):
        data = "£ ¤ ¤"
        m_open = open_mock(data)
        with patch("builtins.open", m_open):
            result = get_most_common_non_ascii_char("file_name")
        self.assertEqual(result, '¤')


if __name__ == "__main__":
    unittest.main()
