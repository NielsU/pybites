from datetime import date

from dataclasses import dataclass

weekdays = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}


def get_pybites_first_day() -> str:
    first_date: date = date(2016, 12, 19)
    week_day: int = first_date.weekday()
    return weekdays[week_day]


print(get_pybites_first_day())
