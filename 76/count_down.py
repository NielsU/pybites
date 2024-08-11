from functools import singledispatch


@singledispatch
def count_down(data_type):
    raise ValueError(f"Cannot count down for data type:{type(data_type)}")


@count_down.register
def _(data_type: str):
    """Count_down overload for type string. This function handles count down for all types."""

    if not data_type.isnumeric:
        raise ValueError("Cant count down non numeric")

    for i in range(0, len(data_type)):
        print(data_type[: (len(data_type) - i)])


""" 
    Following types are handled by transforming to string: int,float,list
"""


@count_down.register(float)
@count_down.register(int)
def _(data_type):
    count_down(str(data_type))


@count_down.register
def _(data_type: list):
    """Overload for type list. Handle count as string"""
    count_down("".join(map(str, data_type)))


""" 
    Counting for following types is handled via the list overload
"""


@count_down.register(range)
@count_down.register(set)
@count_down.register(tuple)
def _(data_type):
    count_down(list(data_type))


@count_down.register
def _(data_type: dict):
    count_down(list(data_type.keys()))
