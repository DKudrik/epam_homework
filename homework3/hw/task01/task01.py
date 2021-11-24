from functools import wraps


def cache(_func=None, *, times):
    def inter(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not wrapper.counter:
                wrapper.output = func(*args, **kwargs)
                wrapper.invocations += 1
                wrapper.counter = times
            else:
                wrapper.counter -= 1
            return wrapper.output

        wrapper.output = None
        wrapper.counter = 0
        wrapper.invocations = 0
        return wrapper

    if _func is None:
        return inter
    else:
        return inter(_func)
