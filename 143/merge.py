NOT_FOUND = "Not found"

group1 = {"tim": 30, "bob": 17, "ana": 24}
group2 = {"ana": 26, "thomas": 64, "helen": 26}
group3 = {"brenda": 17, "otto": 44, "thomas": 46}

combined = {**group1, **group2, **group3}


def get_person_age(name: str):
    """Look up name (case insensitive search) and return age.
    If name in > 1 dict, return the match of the group with
    greatest N (so group3 > group2 > group1)
    """
    name = str(name).lower()

    if name in combined:
        return combined[name]
    else:
        return NOT_FOUND


def merge_dicts(*args: dict) -> dict:
    """created this function to try out using multiple arguments with *args
    but figured that combining them by:
    combined = {**group1, **group2, **group3}
    is in this case the simpler way.
    """
    merged = {}
    for d in args:
        merged |= d

    return merged


print(combined)
