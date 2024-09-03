from functools import wraps


DEFAULT_TEXT = (
    "Subscribe to our blog (sidebar) to periodically get "
    "new PyBites Code Challenges (PCCs) in your inbox"
)
DOT = "."


def strip_range(start, end):
    """Decorator that replaces characters of a text by dots, from 'start'
    (inclusive) to 'end' (exclusive) = like range.

     So applying this decorator on a function like this and 'text'
     being 'Hello world' it would convert it into 'Hel.. world' when
     applied like this:

     @strip_range(3, 5)
     def gen_output(text):
         return text
    """

    def wrapper(func):
        @wraps(func)
        def inner_strip_range(*args, **kwargs):
            txt = list(func(*args, **kwargs))

            local_start = start if start >= 0 else 0
            local_end = end if end <= len(txt) else len(txt)

            for i in range(local_start, local_end):
                txt[i] = DOT

            return "".join(txt)

        return inner_strip_range

    return wrapper


def to_upper(func):
    @wraps(func)
    def actual_decorator(text):
        text = str(text).upper()

        return func(text)

    return actual_decorator


@strip_range(4, 6)
@to_upper
@strip_range(1, 3)
def echo(text):
    return text


print(echo(text="hello world!"))

print(echo("hello world!"))
