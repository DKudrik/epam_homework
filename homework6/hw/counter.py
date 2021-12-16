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
    @classmethod
    def inits_counter(cls):
        if "created_instances" not in cls.__dict__:
            cls.created_instances = 0

    original_init = cls.__init__

    def new_init(self, *args, **kwargs):
        self.__class__.inits_counter()
        self.__class__.created_instances += 1
        original_init(self, *args, **kwargs)

    @classmethod
    def get_created_instances(cls):
        cls.inits_counter()
        return cls.created_instances

    @classmethod
    def reset_instances_counter(cls):
        cls.inits_counter()
        counter_to_return = cls.created_instances
        cls.created_instances = 0
        return counter_to_return

    setattr(cls, "__init__", new_init)
    setattr(cls, "inits_counter", inits_counter)
    setattr(cls, "get_created_instances", get_created_instances)
    setattr(cls, "reset_instances_counter", reset_instances_counter)
    return cls
