def val_convert_inputs(value: float | int, fmt: str):
    if type(value) not in (float, int):
        raise TypeError("Value param must be int or float")

    if not isinstance(fmt, str):
        raise TypeError("fmt must be str")

    if fmt not in ("cm", "in"):
        raise ValueError("fmt value must be in ('cm','in')")


def convert(value: float, fmt: str) -> float:
    """Converts the value to the designated format.

    :param value: The value to be converted must be numeric or raise a TypeError
    :param fmt: String indicating format to convert to
    :return: Float rounded to 4 decimal places after conversion
    """
    fmt = fmt.lower()

    val_convert_inputs(value, fmt)

    if fmt == "in":
        return round(value * 0.3937007874, 4)
    else:
        return round(value * 2.54, 4)
