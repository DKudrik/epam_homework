"""
Classic task, a kind of walnut for you

Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that
    A[i] + B[j] + C[k] + D[l] is zero.

We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from typing import List


def check_sum_of_four(a: List[int], b: List[int],
                      c: List[int], d: List[int]) -> int:
    result = 0
    for index_a, _ in enumerate(a):
        for index_b, _ in enumerate(b):
            for index_c, _ in enumerate(c):
                for index_d, _ in enumerate(d):
                    if a[index_a] + b[index_b] + c[index_c] + d[index_d] == 0:
                        result += 1
    return result
