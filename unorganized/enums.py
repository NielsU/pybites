from enum import Enum, unique


@unique
class Colour(Enum):
    RED = 1
    BLUE = 2
    BLACK = 0
    ORANGE = 0


print(Colour(1))
