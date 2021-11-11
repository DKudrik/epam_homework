"""
Write down the function, which reads input line-by-line, and find maximum and
minimum values.
Function should return a tuple with the max and min values.

For example for [1, 2, 3, 4, 5], function should return [1, 5]

We guarantee, that file exists and contains line-delimited integers.

To read file line-by-line you can use this snippet:

with open("some_file.txt") as fi:
    for line in fi:
        ...

"""
from typing import Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    with open(file_name) as fi:
        for count, line in enumerate(fi):
            line = int(line)
            if count == 0:
                min_value = line
                max_value = line
            min_value = line if line < min_value else min_value
            max_value = line if line > max_value else max_value
        return min_value, max_value
