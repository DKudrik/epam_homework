import pytest

from hw.task_3_get_print_output import my_precious_logger

test_data = [
    ("OK", "OK", ""),
    ("error: file not found", "", "error: file not found"),
]


@pytest.mark.parametrize("text, stdout_value, stderr_value", test_data)
def test_my_precious_logger(capsys, text, stdout_value, stderr_value):
    my_precious_logger(text)
    out, err = capsys.readouterr()
    assert out == stdout_value
    assert err == stderr_value
