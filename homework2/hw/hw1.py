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


def get_longest_diverse_words(file_path: str) -> List[str]:
    file = open(file_path, "r", encoding="unicode escape")
    text = [y for x in file.readlines() for y in x.split()]
    file.close()
    result = [text[0]]
    for value in text[1:]:
        set_value = set(value)
        set_result_0 = set(result[0])
        if len(result) < 10 and len(set_value) >= len(set_result_0):
            result.append(value)
        elif len(set_value) > len(set_result_0):
            result[0] = value
        result.sort(key=len)
    return result


def get_rarest_char(file_path: str) -> str:
    file = open(file_path, "r", encoding="unicode escape")
    result = {}
    for char in file.read():
        if result.get(char, False):
            result[char] += 1
        else:
            result[char] = 1
    file.close()
    sorted_tuples = sorted(result.items(), key=operator.itemgetter(1))
    sorted_result = {k: v for k, v in sorted_tuples}
    return list(sorted_result.keys())[0]


def count_punctuation_chars(file_path: str) -> int:
    PUNCT_CHARS = ('?', '!', '„', '“', '.', ',', ';', ':', '-', '(', ')', '"',
                   '\'')
    file = open(file_path, "r", encoding="unicode escape")
    result = 0
    for char in file.read():
        if char in PUNCT_CHARS:
            result += 1
    file.close()
    return result


def count_non_ascii_chars(file_path: str) -> int:
    file = open(file_path, "r", encoding="unicode escape")
    result = 0
    for char in file.read():
        if ord(char) > 127:
            result += 1
    file.close()
    return result


def get_most_common_non_ascii_char(file_path: str) -> str:
    file = open(file_path, "r", encoding="unicode escape")
    result = {}
    for char in file.read():
        if ord(char) > 127:
            if result.get(char, False):
                result[char] += 1
            else:
                result[char] = 1
    file.close()
    sorted_tuples = sorted(result.items(), key=operator.itemgetter(1))
    sorted_result = {k: v for k, v in sorted_tuples}
    return list(sorted_result.keys())[-1]
