def check_power_of_2(a: int) -> bool:
    if not isinstance(a, int):
        return 'Введите число'
    elif a <= 0:
        return ValueError('Число должно быть позитивным')
    return not (bool(a & (a - 1)))
