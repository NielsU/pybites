import re


def count_indents(text: str) -> int:
    """
    Count and return the number of leading white space characters (' ').
    """

    """
        Approaches explored:
        1- For loop over string, count break when no char.isspace().
        2- List comprehension using enumerate, save index of non space chars. Return value of first item.  
        3- Regular expression, match on spaces return end index of match.
        4- Implement break with helper function raising StopIteration if non space char found. (rather complicated)
    """
    # return count_by_list_comp(text)

    # count_by_list_comp_break(text)

    # return count_by_for_loop(text)

    return count_by_re(text)


def count_by_for_loop(text: str) -> int:
    """1- For loop over string, count break when no char.isspace()."""

    for index, char in enumerate(text):
        if char != " ":
            return index

    return len(text)


def count_by_list_comp(text: str) -> int:
    """2- List comprehension using enumerate, save index of non space chars. Return value of first item."""
    nr_indents = [index for index, value in enumerate(text) if value != " "]
    if len(nr_indents) > 0:
        return nr_indents[0]
    else:
        return 0


def count_by_re(text: str) -> int:
    """3- Regular expression, match on spaces return end index of match."""
    match = re.match("[ ]*", text)
    return match.span()[1]


def count_by_list_comp_break(text: str) -> int:
    """4- Implement break with helper function raising StopIteration if non space char found. (rather complicated)"""
    nr_indents = []

    def is_space(value):
        """helper function to break list comprehension."""
        if value != " ":
            raise StopIteration("non space value found")

        return True

    try:
        [nr_indents.append(value) for value in text if is_space(value)]
    except StopIteration:
        pass

    return len(nr_indents)
