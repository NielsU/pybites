from collections import Counter, defaultdict
import csv
import io

import requests

CSV_URL = "https://raw.githubusercontent.com/pybites/SouthParkData/master/by-season/Season-{}.csv"  # noqa E501


def get_season_csv_file(season):
    """Receives a season int, and downloads loads in its
    corresponding CSV_URL"""
    with requests.Session() as s:
        download = s.get(CSV_URL.format(season))
        return download.content.decode("utf-8")


def get_num_words_spoken_by_character_per_episode(content):
    """Receives loaded csv content (str) and returns a dict of
    keys=characters and values=Counter object,
    which is a mapping of episode=>words spoken"""

    reader = csv.DictReader(io.StringIO(content))

    result = defaultdict(Counter)

    for item in reader:
        num_words_spoken = len(item["Line"].split())
        episode = item["Episode"]
        character = item["Character"]

        result[character].update({episode: num_words_spoken})

    return result
