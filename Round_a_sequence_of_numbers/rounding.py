"""

Level: Beginner (score: 2)

It's time to get mathematical! In this Bite we ask that you complete the round_up_or_down function that receives a transactions list of floats and an optional up argument.

If up is True (default) you round them up to the nearest full integer, if it is False, you round down to the nearest full integer. Return a new list with the rounded int values.

Use whatever method you see fit, good luck!


"""

import math


def round_up_or_down(transactions, up=True):
    """Round the list of transactions passed in.
    If up=True (default) round up, else round down.
    Return a new list of rounded values
    """

    return [
        math.ceil(transaction) if up else math.floor(transaction)
        for transaction in transactions
    ]
