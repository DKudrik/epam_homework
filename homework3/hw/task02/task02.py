import hashlib
import random
import struct
import time
from multiprocessing import Pool


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack("<" + "B" * len(data), data))


values = [x for x in range(501)]


def pool_handler():
    p = Pool(60)
    result = sum(p.map(slow_calculate, values))
    return result


if __name__ == "__main__":
    print(pool_handler())
