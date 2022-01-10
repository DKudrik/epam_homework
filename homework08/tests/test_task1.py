from unittest.mock import mock_open, patch

import pytest

from hw.task1 import KeyValueStorage


def open_mock(data):
    """An auxiliary method to prepare mock_open"""
    m_open = mock_open(read_data=data)
    m_open.return_value.__iter__.return_value = data.splitlines()
    return m_open


@pytest.fixture()
def test_data():
    data = (
        "name=kek \nlast_name=top \npower=9001 \nsong=shadilay \n3=qwe "
        "\n__doc__=document"
    )
    m_open = open_mock(data)
    with patch("builtins.open", m_open):
        storage = KeyValueStorage("file_name")
    return storage


def test_key_value_storage(test_data):
    assert test_data["name"] == "kek"
    assert test_data.song == "shadilay"
    assert isinstance(test_data.power, int) is True
    assert 3 not in dir(KeyValueStorage)
    assert KeyValueStorage.__doc__ != "document"
