from functools import wraps


def cache(_func=None, *, times):
    def inter(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not wrapper.cache:
                result = func(*args, **kwargs)
                for _ in range(times):
                    wrapper.cache.append(result)
                output = wrapper.cache[-1]
            else:
                output = wrapper.cache.pop()
            return output
        wrapper.cache = []
        return wrapper

    if _func is None:
        return inter
    else:
        return inter(_func)


@cache(times=2)
def plus(a: int, b: int) -> int:
    return a + b
