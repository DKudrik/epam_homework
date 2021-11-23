from hw.task_2_mock_input import count_dots_on_i

import pytest

# import mock
import responses
import requests
import requests_mock


def test_mock_input():
    with requests_mock.mock() as m:
        m.get("http://test.com", text="data")
        # response = requests.get('http://example.com/api/123')
        result = count_dots_on_i("http://test.com")

    assert 404 is result
