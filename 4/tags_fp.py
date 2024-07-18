import os
from collections import Counter
import urllib.request
import feedparser

# prep
tmp = os.getenv("TMP", "/tmp")
tempfile = os.path.join(tmp, "feed")
urllib.request.urlretrieve(
    "https://bites-data.s3.us-east-2.amazonaws.com/feed", tempfile
)

with open(tempfile) as f:
    content = f.read()


def get_pybites_top_tags(n=10):
    """use Counter to get the top 10 PyBites tags from the feed
    data already loaded into the content variable"""

    counter = Counter()

    feed = feedparser.parse(content)

    counter.update(
        [tags["term"].lower() for item in feed.entries for tags in item.tags]
    )

    return counter.most_common(n)


print(get_pybites_top_tags())
