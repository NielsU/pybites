# use one or more Standard Library modules
from secrets import choice
import string


# get a random char.
def get_char():
    return choice(string.ascii_uppercase + string.digits)


def get_part(length: int):
    # get one part to use in the liscense of length: length.
    return "".join([get_char() for _ in range(length)])


def gen_key(parts: int = 4, chars_per_part: int = 8) -> str:
    """
    Generate and return a random license key containing
    upper case characters and digits.

    Example with default "parts" and "chars_per_part"
    being 4 and 8: KI80OMZ7-5OGYC1AC-735LDPT1-4L11XU1U

    If parts = 3 and chars_per_part = 4 a random license
    key would look like this: 54N8-I70K-2JZ7
    """

    # get the indicated number of parts, separated by a dash.
    return "-".join([get_part(chars_per_part) for _ in range(parts)])


for _ in range(10):
    key = gen_key(3, 10)
    print(key)
