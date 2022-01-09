"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.

Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from typing import Any


example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        },
    },
    "fourth": "RED",
}


def list_processor(data: list, el_to_find: Any, counter: int) -> int:
    """
    Aux func to process list data in initial input data.
    """
    for el in data:
        if el == el_to_find:
            counter += 1
        elif isinstance(el, list):
            counter = list_processor(el, el_to_find, counter)
        elif isinstance(el, dict):
            counter = find_occurrences(el, el_to_find, counter)
    return counter


def find_occurrences(tree: dict, element: Any, counter=None) -> int:
    counter = 0 if counter is None else counter
    for k, v in tree.items():
        if k == element:
            counter += 1
        if v == element:
            counter += 1
        elif isinstance(v, dict):
            counter = find_occurrences(v, element, counter)
        elif isinstance(v, list):
            counter = list_processor(v, element, counter)
    return counter


if __name__ == "__main__":
    print(find_occurrences(example_tree, "RED"))
