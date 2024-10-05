def uncommon_cities(my_cities, other_cities):
    """Compare my_cities and other_cities and return the number of different
    cities between the two"""

    """
    unique_my_cities = list(filter(lambda item: item not in other_cities, my_cities))
    unique_other_cities = list(filter(lambda item: item not in my_cities, other_cities))

    return len(unique_my_cities) + len(unique_other_cities)
    """

    return len(set(my_cities) ^ set(other_cities))
