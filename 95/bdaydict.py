from datetime import date

MSG = "Hey {}, there are more people with your birthday!"


class BirthdayDict(dict):
    """Override dict to print a message every time a new person is added that has
    the same birthday (day+month) as somebody already in the dict"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._birthdays = set()

    def __setitem__(self, name, birthday):

        if (birthday.day, birthday.month) in self._birthdays:
            print(MSG.format(name))

        self._birthdays.add((birthday.day, birthday.month))

        super().__setitem__(name, birthday)
