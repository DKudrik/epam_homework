"""
Write a function that merges integer from sorted files and returns an iterator

file1.txt:
1
3
5

file2.txt:
2
4
6

#>>> list(merge_sorted_files(["file1.txt", "file2.txt"]))
[1, 2, 3, 4, 5, 6]
"""
from pathlib import Path
from typing import Iterator, List, Union


def process_file(file_list: List[Union[Path, str]]) -> Iterator:
    """
    Aux func to open and process txt files.
    """
    for file in file_list:
        with open(file) as f:
            for line in f:
                yield int(line.rstrip())


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:
    for item in sorted(process_file(file_list)):
        yield item
