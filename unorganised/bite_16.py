from datetime import datetime, timedelta
from pprint import pprint as pp
from itertools import islice

PYBITES_BORN = datetime(year=2016, month=12, day=19)


def gen_special_pybites_dates(start_date: datetime = PYBITES_BORN):
    while True:
        start_date += timedelta(days=100)
        yield start_date


gen = gen_special_pybites_dates()


pp(list(islice(gen, 5)))

pp(PYBITES_BORN)
