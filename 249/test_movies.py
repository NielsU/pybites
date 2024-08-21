import os
import random
import string
import sqlite3

import pytest

from movies import MovieDb

salt = "".join(random.choice(string.ascii_lowercase) for i in range(20))
DB = os.path.join(os.getenv("TMP", "/tmp"), f"movies_{salt}.db")
# https://www.imdb.com/list/ls055592025/
DATA = [
    ("The Godfather", 1972, 9.2),
    ("The Shawshank Redemption", 1994, 9.3),
    ("Schindler's List", 1993, 8.9),
    ("Raging Bull", 1980, 8.2),
    ("Casablanca", 1942, 8.5),
    ("Citizen Kane", 1941, 8.3),
    ("Gone with the Wind", 1939, 8.1),
    ("The Wizard of Oz", 1939, 8),
    ("One Flew Over the Cuckoo's Nest", 1975, 8.7),
    ("Lawrence of Arabia", 1962, 8.3),
]
TABLE = "movies"


@pytest.fixture
def db():
    # instantiate MovieDb class using above constants
    # do proper setup / teardown using MovieDb methods
    # https://docs.pytest.org/en/latest/fixture.html (hint: yield)
    db = MovieDb(db=DB, data=DATA, table=TABLE)
    db.init()

    yield db

    # tear down
    db.drop_table()
    db.con.close()
    os.remove(DB)


# write tests for all MovieDb's query / add / delete
def test_db_init(db):
    assert type(db) is MovieDb


def test_db_query(db):
    assert len(db.query()) == 10


def test_db_query_title(db):
    title = "Citizen Kane"
    movie_list = db.query(title=title)

    assert len(movie_list) == 1
    assert type(movie_list[0]) is tuple
    assert movie_list[0][1] == title


def test_db_query_year(db):
    title = "Citizen Kane"
    movie_list = db.query(year=1941)

    assert len(movie_list) == 1
    assert movie_list[0][1] == title


def test_db_query_score(db):
    score = 8.9
    movie_list = db.query(score_gt=score)

    for movie in movie_list:
        assert movie[3] > score

    assert len(movie_list) == 2


def test_db_query_no_match(db):
    movie_list = db.query(score_gt=10)
    assert len(movie_list) == 0


def test_add(db):
    # record to add:
    title = "Forrest Gump"
    year = 1994
    score = 8.8

    db.add(title, year, score)
    expected = [(11, title, year, score)]

    assert db.query(title=title) == expected


def test_delete(db):
    title = "Lawrence of Arabia"
    # get movie index
    idx = db.query(title=title)[0][0]

    # remove by index
    db.delete(idx)

    # movie should no longer exist.
    assert db.query(title=title) == []
