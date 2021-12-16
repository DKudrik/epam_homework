from hw.counter import instances_counter


@instances_counter
class User:
    pass


def test_instances_counter():
    """Testing with 2 instances"""
    instances_num = User.get_created_instances()
    assert instances_num == 0

    User(), User()
    instances_num = User.get_created_instances()
    assert instances_num == 2

    User()
    instances_num = User.get_created_instances()
    assert instances_num == 3

    instances_num_before_reset = User.get_created_instances()
    User.reset_instances_counter()
    assert instances_num_before_reset == 3

    instances_num_after_reset = User.get_created_instances()
    assert instances_num_after_reset == 0
