from collections import namedtuple

Bite = namedtuple("Bite", ["number", "title", "is_complex"])


def make_namedtuple(number, title, score):

    x: Bite = Bite(number, title, int(score) > 5)
    # Your code here
    return x


bite: Bite = make_namedtuple(1, "first bite", 6)
print(bite)
bite = make_namedtuple(2, "second bite", 5)
print(f"{bite!s}")
