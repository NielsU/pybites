from random import random
from time import sleep


def cached_property(func):
    """decorator used to cache expensive object attribute lookup"""

    def getter(self) -> str:
        # initialise caching dictionary
        try:
            if self.prop_cache is None:
                pass
        except AttributeError:
            self.prop_cache = dict()

        # cache the value
        if func.__name__ not in self.prop_cache:
            self.prop_cache[func.__name__] = func(self)

        # return cached value
        return self.prop_cache[func.__name__]

    return property(getter)


class Planet:
    """the nicest little orb this side of Orion's Belt"""

    GRAVITY_CONSTANT = 42
    TEMPORAL_SHIFT = 0.12345
    SOLAR_MASS_UNITS = "M\N{SUN}"

    def __init__(self, color):
        self.color = color
        self._mass = None

    def __repr__(self):
        return f"{self.__class__.__name__}({repr(self.color)})"

    @cached_property
    def mass(self):
        scale_factor = random()
        sleep(self.TEMPORAL_SHIFT)
        self._mass = (
            f"{round(scale_factor * self.GRAVITY_CONSTANT, 4)} "
            f"{self.SOLAR_MASS_UNITS}"
        )
        return self._mass


x = Planet("white")

print(x.mass)
