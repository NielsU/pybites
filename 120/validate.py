from functools import wraps


def int_args(func):
    @wraps(func)
    def validate_args_int(*args, **kwargs):
        # complete this decorator
        for value in args:
            if type(value) is not int:
                raise TypeError
            if int(value) < 0:
                raise ValueError
        return func(*args, **kwargs)

    return validate_args_int
