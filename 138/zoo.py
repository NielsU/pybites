class Animal:
    sequence = 10000
    animals = []

    @classmethod
    def next_id(cls) -> int:
        cls.sequence += 1
        return cls.sequence

    def __init__(self, name):
        self.name = str(name).title()
        self.id = self.next_id()
        self.animals.append(self)

    def __str__(self):
        return f"{self.id}. {self.name}"

    @classmethod
    def zoo(cls):
        return "\n".join(str(animal) for animal in cls.animals)
