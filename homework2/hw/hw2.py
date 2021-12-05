"""
Given an array of size n, find the most common and the least common elements.
The most common element is the element that appears more than n // 2 times.
The least common element is the element that appears fewer than other.

You may assume that the array is non-empty and the most common element
always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3, 2

Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2, 1

"""
import operator
from collections import Counter
from typing import List, Tuple


def major_and_minor_elem(inp: List) -> Tuple[int, int]:
    counted_chars = Counter(inp)
    sorted_tuples = sorted(counted_chars.items(), key=operator.itemgetter(1))
    sorted_result = {k: v for k, v in sorted_tuples}
    listed_result = list(sorted_result.keys())
    most_common = listed_result[-1]
    if len(listed_result) > 1:
        least_common = listed_result[0]
    else:
        least_common = None
    return most_common, least_common
