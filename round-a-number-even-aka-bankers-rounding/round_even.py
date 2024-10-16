import math


def round_even(number):
    """Takes a number and returns it rounded even"""
    # result = 0
    # # Only x.5 numbers get the "special" treatment.
    # if number % 2 == 0.5:
    #     # return the nearest even integer
    #     result = (
    #         math.floor(number) if math.floor(number) % 2 == 0 else math.ceil(number)
    #     )

    # else:
    #     result = round(number, 0)

    # return result

    # turns out python 3 rounding is already half_even.
    # https://docs.python.org/3/library/functions.html#round
    return round(number, 0)
