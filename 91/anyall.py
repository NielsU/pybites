VOWELS = "aeiou"
PYTHON = "python"


def contains_only_vowels(input_str):
    """Receives input string and checks if all chars are
    VOWELS. Match is case insensitive."""
    for char in input_str:
        if str(char).lower() not in VOWELS:
            return False

    return True


def contains_any_py_chars(input_str):
    """Receives input string and checks if any of the PYTHON
    chars are in it. Match is case insensitive."""
    for char in PYTHON:
        if char in str(input_str).lower():
            return True

    return False


def contains_digits(input_str):
    """Receives input string and checks if it contains
    one or more digits."""
    for char in input_str:
        if str(char).isdigit():
            return True
    return False
