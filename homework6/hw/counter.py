"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять

Ниже пример использования
"""


def instances_counter(cls):
    def get_created_instances():
        return cls.counter

    def reset_instances_counter():
        counter_to_return = cls.counter
        cls.counter = 0
        return counter_to_return

    setattr(cls, "get_created_instances", get_created_instances)
    setattr(cls, "reset_instances_counter", reset_instances_counter)
    return cls


@instances_counter
class User:
    counter = 0

    def __init__(self):
        self.__class__.counter += 1


if __name__ == "__main__":
    User.get_created_instances()  # 0
    user, _, _ = User(), User(), User()
    User.get_created_instances()  # 3
    User.reset_instances_counter()  # 3
