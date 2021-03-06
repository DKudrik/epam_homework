"""
Classic task, a kind of walnut for you

Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that
    A[i] + B[j] + C[k] + D[l] is zero.

We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from typing import List
from collections import defaultdict
from itertools import product


def check_sum_of_four(a: List[int], b: List[int],
                      c: List[int], d: List[int]) -> int:
    first_sums = defaultdict(int)
    result = 0
    for elements in product(a, b):
        first_sums[(sum(elements))] += 1
    for elements in product(c, d):
        result += first_sums[-sum(elements)]
    return result
