from hw.hw1 import find_occurrences


def test_find_occurrences_set_1():
    assert find_occurrences({"RED": "RED"}, "RED") == 2


def test_find_occurrences_set_2():
    assert find_occurrences({"RED": ["RED", "RED"]}, "RED") == 3


test_data_1 = {"RED": {1: ["qwe", "RED"]}}


def test_find_occurrences_set_3():
    assert find_occurrences(test_data_1, "RED") == 2


test_data_2 = {
    "first": ["RED", 2, "RED"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": {1: "RED"},
            "key2": "RED",
            "key3": ["of", "values", {"RED": "RED"}, ["RED"], {"1": "RED"}],
        },
    },
}


def test_find_occurrences_set_4():
    assert find_occurrences(test_data_2, "RED") == 10
