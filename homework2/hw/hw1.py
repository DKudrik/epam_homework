"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
import operator
from typing import List


def file_open(file_path: str, encoding: str):
    """Auxiliary func to open files"""
    with open(file_path, 'r', encoding=encoding) as fi:
        words = []
        for line in fi:
            words += line.split()
    return words


def get_longest_diverse_words(file_path: str, encoding='utf8') -> List[str]:
    words = file_open(file_path, encoding=encoding)
    result = [words[0]]
    print(encoding)
    for value in words[1:]:
        set_value = set(value)
        set_result_0 = set(result[0])
        if len(result) < 10 and len(set_value) >= len(set_result_0):
            result.append(value)
        elif len(set_value) > len(set_result_0):
            result[0] = value
        result.sort(key=len)
    return result


def get_rarest_char(file_path: str, encoding='utf8') -> str:
    words = file_open(file_path, encoding=encoding)
    result = {}
    for word in words:
        for char in word:
            if result.get(char, False):
                result[char] += 1
            else:
                result[char] = 1
    sorted_tuples = sorted(result.items(), key=operator.itemgetter(1))
    sorted_result = {k: v for k, v in sorted_tuples}
    return list(sorted_result.keys())[0]


def count_punctuation_chars(file_path: str, encoding='utf8') -> int:
    PUNCT_CHARS = ('?', '!', '„', '“', '.', ',', ';', ':', '-', '(', ')', '"',
                   '\'')
    words = file_open(file_path, encoding=encoding)
    result = 0
    for char in words:
        if char in PUNCT_CHARS:
            result += 1
    return result


def count_non_ascii_chars(file_path: str, encoding='utf8') -> int:
    words = file_open(file_path, encoding=encoding)
    result = 0
    for char in words:
        if ord(char) > 127:
            result += 1
    return result


def get_most_common_non_ascii_char(file_path: str, encoding='utf8') -> str:
    words = file_open(file_path, encoding=encoding)
    result = {}
    for char in words:
        if ord(char) > 127:
            if result.get(char, False):
                result[char] += 1
            else:
                result[char] = 1
    sorted_tuples = sorted(result.items(), key=operator.itemgetter(1))
    sorted_result = {k: v for k, v in sorted_tuples}
    return list(sorted_result.keys())[-1]
