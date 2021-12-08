import os.path

from hw.task2 import TableData


def test_tabledata_class():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "example.sqlite")
    presidents = TableData(db_path, "presidents")
    assert len(presidents) == 3
    assert presidents["Yeltsin"] == ("Yeltsin", 999, "Russia")
    assert ("Yeltsin" in presidents) is True
    for president in presidents:
        assert isinstance(president["name"], str) is True
