import csv
from collections import defaultdict, namedtuple
import os
from urllib.request import urlretrieve
from statistics import mean
from operator import itemgetter

BASE_URL = "https://bites-data.s3.us-east-2.amazonaws.com/"
TMP = os.getenv("TMP", "/tmp")

fname = "movie_metadata.csv"
remote = os.path.join(BASE_URL, fname)
local = os.path.join(TMP, fname)
urlretrieve(remote, local)

MOVIE_DATA = local
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple("Movie", "title year score")


def get_movies_by_director():
    """Extracts all movies from csv and stores them in a dict,
    where keys are directors, and values are a list of movies,
    use the defined Movie namedtuple"""
    movies_by_director = defaultdict(list)

    with open(MOVIE_DATA, encoding="utf-8") as movie_file:
        for movie in csv.DictReader(movie_file):
            # Construct Movie tuple
            # Only extract director_name, movie_title, title_year and imdb_score,
            # ignoring movies without all of these fields.
            try:
                movie_tuple = Movie(
                    title=movie["movie_title"].strip(),
                    year=int(movie["title_year"].strip()),
                    score=float(movie["imdb_score"].strip()),
                )
            except ValueError:
                # Just skip, maybe good enough to exclude movies without all required fields present.
                continue

            # discard any movies older than 1960.
            if movie_tuple.year < MIN_YEAR:
                continue

            # add movie to director
            movies_by_director[movie["director_name"]].append(movie_tuple)

    return movies_by_director


def calc_mean_score(movies):
    """Helper method to calculate mean of list of Movie namedtuples,
    round the mean to 1 decimal place"""
    m = mean([movie.score for movie in movies])

    return round(m, 1)


def get_average_scores(directors):
    """Iterate through the directors dict (returned by get_movies_by_director),
    return a list of tuples (director, average_score) ordered by highest
    score in descending order. Only take directors into account
    with >= MIN_MOVIES"""
    average_scores = []

    for director_name, movies in directors.items():
        # Only take directors into account with >= MIN_MOVIES
        if len(movies) >= MIN_MOVIES:
            average_scores.append((director_name, calc_mean_score(movies)))

    average_scores.sort(reverse=True, key=itemgetter(1))

    return average_scores


mbd = get_average_scores(get_movies_by_director())

print(mbd)
