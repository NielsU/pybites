from collections import namedtuple

import feedparser

# cached version to have predictable results for testing
FEED_URL = "https://bites-data.s3.us-east-2.amazonaws.com/steam_gaming.xml"

Game = namedtuple("Game", "title link")


def get_games():
    games = feedparser.parse(FEED_URL)
    return [Game(item["title"], item["link"]) for item in games["items"]]
