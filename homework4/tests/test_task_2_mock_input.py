from unittest.mock import patch

import pytest

from hw.task_2_mock_input import count_dots_on_i


def test_mock_input_with_5_i():
    with patch("requests.get") as mock_request:
        mock_request.return_value.text = "iiiii"
        assert count_dots_on_i("qwe") == 5


def test_mock_input_connection_error():
    with patch("requests.get", side_effect=ConnectionError) as mock_request:
        mock_request.return_value.text = "qwerty"
        with pytest.raises(ConnectionError):
            count_dots_on_i("https://example.com")
