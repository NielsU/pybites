from typing import Union


def fizzbuzz(num: int) -> Union[str, int]:
    """
    replacing any number divisible by three with the word "fizz",
    and any number divisible by five with the word "buzz".
    """

    if num % 3 == 0:
        return "fizz"
    elif num % 5 == 0:
        return "buzz"
    else:
        return num
