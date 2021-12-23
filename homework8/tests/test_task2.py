import os.path

from hw.task2 import TableData


def test_tabledata_len_method():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "example.sqlite")
    presidents = TableData(db_path, "presidents")
    assert len(presidents) == 3


def test_tabledata_getitem_method():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "example.sqlite")
    presidents = TableData(db_path, "presidents")
    assert presidents["Yeltsin"] == ("Yeltsin", 999, "Russia")


def test_tabledata_contains_method():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "example.sqlite")
    presidents = TableData(db_path, "presidents")
    assert ("Yeltsin" in presidents) is True


def test_tabledata_iter_method():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "example.sqlite")
    presidents = TableData(db_path, "presidents")
    for president in presidents:
        assert isinstance(president["name"], str) is True
