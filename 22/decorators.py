from functools import wraps


def make_html(element):
    def decorator_make_html(func):
        @wraps(func)
        def wrapper_make_html(*args, **kwargs):
            return f"<{element}>{func(*args,**kwargs)}</{element}>"

        return wrapper_make_html

    return decorator_make_html
