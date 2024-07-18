from collections import namedtuple
from datetime import datetime
import json


blog = dict(
    name="PyBites",
    founders=("Julian", "Bob"),
    started=datetime(year=2016, month=12, day=19),
    tags=["Python", "Code Challenges", "Learn by Doing"],
    location="Spain/Australia",
    site="https://pybit.es",
)

# define namedtuple here
Blog = namedtuple("Blog", "name founders started tags location site")


def dict2nt(dict_: dict):
    return Blog(**dict_)


def nt2json(nt: Blog):

    d = nt._asdict()

    for key in d.keys():
        if type(d[key]) is datetime:
            d[key] = datetime.date(d[key]).isoformat()

    return json.JSONEncoder().encode(d)


print(nt2json(dict2nt(blog)))
