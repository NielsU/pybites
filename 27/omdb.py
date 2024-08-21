import json
import re


def get_movie_data(files: list) -> list:
    """Parse movie json files into a list of dicts"""
    return [json.load(open(file)) for file in files]


def get_single_comedy(movies: list) -> str:
    """return the movie with Comedy in Genres"""
    comedy_movies = [movie for movie in movies if "Comedy" in movie["Genre"]]

    if len(comedy_movies) > 0:
        return comedy_movies[0]["Title"]
    else:
        return ""


def nr_of_nominations(movie: dict) -> int:
    r = re.compile(r"(?P<n2>\d*) nominations.")
    matches = r.findall(movie["Awards"])
    return sum(int(number) for number in matches)


def get_movie_most_nominations(movies: list) -> str:
    """Return the movie that had the most nominations"""
    # Solution using sort
    # movies.sort(key=lambda movie: nr_of_nominations(movie), reverse=True)
    # return movies[0].get("Title")

    # solution with max, had overlooked max has key argument,
    # pybites provided solutions was hint. simplifies the solution a bit i think.
    mv = max(movies, key=lambda m: nr_of_nominations(m))
    return mv.get("Title")


def get_movie_longest_runtime(movies: list) -> str:
    """Return the movie that has the longest runtime"""
    movies.sort(key=lambda movie: int(str(movie["Runtime"]).split()[0]), reverse=True)
    return movies[0].get("Title")


mov = {"Awards": "10 wins & 32 nominations."}
print(nr_of_nominations(mov))
