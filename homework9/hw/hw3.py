"""
Write a function that takes directory path, a file extension and an optional tokenizer.
It will count lines in all files with that extension if there are no tokenizer.
If a the tokenizer is not none, it will count tokens.

For dir with two files from hw1.py:
# >>> universal_file_counter(test_dir, "txt")
# 6
# >>> universal_file_counter(test_dir, "txt", str.split)
# 6

"""
import os
from pathlib import Path
from typing import Callable, Optional


def tokenizing(line, tokenizer=None):
    if tokenizer is None:
        return 1
    return len(tokenizer(line))


def universal_file_counter(
    dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None
) -> int:
    counter = 0
    for file in os.listdir(dir_path):
        file_path = os.path.join(dir_path, file)
        if file.endswith(file_extension):
            with open(file_path) as fh:
                for line in fh:
                    counter += tokenizing(line, tokenizer)
    return counter
