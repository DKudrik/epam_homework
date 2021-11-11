from calculator.calc import check_power_of_2


def test_positive_case():
    """Testing that actual powers of 2 give True"""
    assert check_power_of_2(65536) is True


def test_negative_case():
    """Testing that non-powers of 2 give False"""
    assert check_power_of_2(12) is False


def test_non_integer():
    """Testing that a non-integer as an input raises TypeError"""
    assert check_power_of_2('a') == 'Введите число'
