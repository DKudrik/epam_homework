from hw.hw1 import SimplifiedEnum


def test_simplefied_enum_set_1():
    class ColorsEnum(metaclass=SimplifiedEnum):
        __keys = ("RED", "BLUE", "ORANGE", "BLACK")

    assert ColorsEnum.RED == "RED"
    assert ColorsEnum.BLACK == "BLACK"


def test_simplefied_enum_set_2():
    class SizesEnum(metaclass=SimplifiedEnum):
        __keys = ("XL", "L", "M", "S", "XS")

    assert SizesEnum.XL == "XL"
    assert SizesEnum.S == "S"
