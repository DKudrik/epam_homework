from hw.hw2 import Order


def test_discount_strategy_set_1():
    def morning_discount(order: Order) -> float:
        return order.price * order.morning_discount

    order_1 = Order(100, morning_discount)
    assert order_1.final_price() == 75


def test_discount_strategy_set_2():
    def elder_discount(order: Order) -> float:
        return order.price * 0.9

    order_2 = Order(100, elder_discount)
    assert order_2.final_price() == 10


def test_discount_strategy_set_3():
    def half_price_discount(order: Order) -> float:
        return order.price * 0.5

    order_3 = Order(100, half_price_discount)
    assert order_3.final_price() == 50
