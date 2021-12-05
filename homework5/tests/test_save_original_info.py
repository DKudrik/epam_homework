from hw.save_original_info import custom_sum, print_result


def test_print_result():
    custom_sum([1, 2, 3], [4, 5])
    custom_sum(1, 2, 3, 4)
    assert custom_sum.__doc__ == "This function can sum any objects " \
                                 "which have __add___"
    assert custom_sum.__name__ == "custom_sum"

    without_print = custom_sum.__original_func
    assert without_print(1, 2, 3, 4) == 10
