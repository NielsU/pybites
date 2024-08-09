import random

BITES = {
    6: "PyBites Die Hard",
    7: "Parsing dates from logs",
    9: "Palindromes",
    10: "Practice exceptions",
    11: "Enrich a class with dunder methods",
    12: "Write a user validation function",
    13: "Convert dict in namedtuple/json",
    14: "Generate a table of n sequences",
    15: "Enumerate 2 sequences",
    16: "Special PyBites date generator",
    17: "Form teams from a group of friends",
    18: "Find the most common word",
    19: "Write a simple property",
    20: "Write a context manager",
    21: "Query a nested data structure",
}
BITES_DONE = {6, 10, 16, 18, 21}


class NoBitesAvailable(Exception):
    """There are no more Bites available to pick from"""


class Promo:

    def __init__(self):
        # updated Bite to make local copies (avoid globals!)
        self.all_bites = BITES.copy()
        self.bites_done = BITES_DONE.copy()

    def _pick_random_bite(self):
        """Pick a random Bite that is not done yet, if all
        Bites are done, raise a NoBitesAvailable exception"""

        # determine which bites are available
        """
        available_bites = list(
            filter(lambda x: x not in self.bites_done, self.all_bites.keys())
        )
       

        # cool, this also works by creating a set :)
        available_bites = list(set(self.all_bites).difference(self.bites_done))
        """

        # after seeing solution learned this works too:
        available_bites = list(BITES.keys() - self.bites_done)

        if len(available_bites) == 0:
            raise NoBitesAvailable

        # random sample of 1 from set also worked but got a warning that
        # this is deprecated.
        return random.choice(available_bites)

    def new_bite(self):
        """Get  a random Bite using _pick_random_bite,
        add it to self.bites_done, then return it"""

        new_bite = self._pick_random_bite()

        self.bites_done.add(new_bite)

        return new_bite
