from itertools import count


class Animal:
    _sequence = count(10001)
    _animals = []

    def __init__(self, name):
        self.name = str(name).title()
        self.id = next(self._sequence)
        self._animals.append(self)

    def __str__(self):
        return f"{self.id}. {self.name}"

    @classmethod
    def zoo(cls):
        return "\n".join(str(animal) for animal in cls._animals)
