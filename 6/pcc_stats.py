from collections import Counter, namedtuple
import os
import urllib.request

# prep
tmp = os.getenv("TMP", "/tmp")
tempfile = os.path.join(tmp, "dirnames")
urllib.request.urlretrieve(
    "https://bites-data.s3.us-east-2.amazonaws.com/dirnames.txt", tempfile
)

IGNORE = ["static", "templates", "data", "pybites", "bbelderbos", "hobojoe1848"]

Stats = namedtuple("Stats", "user challenge")


def gen_files(tempfile=tempfile):
    """
    Parse the tempfile passed in, filtering out directory names
    (first column) using the last "is_dir" column.

    Lowercase these directory names and return them as a generator.

    "tempfile" has the following format:
    challenge<int>/file_or_dir<str>,is_dir<bool>

    For example:
    03/rss.xml,False
    03/tags.html,False
    03/Mridubhatnagar,True
    03/aleksandarknezevic,True

    => Here you would return 03/mridubhatnagar (lowercased!)
       followed by 03/aleksandarknezevic
    """

    files = []

    with open(tempfile) as f:

        for line in f.readlines():
            name, is_dir = line.split(",")

            if is_dir.strip() == "True":
                files.append(name.lower())

    for f in files:
        yield (f)


def diehard_pybites(files=None):
    """
    Return a Stats namedtuple (defined above) that contains:
    1. the user that made the most pull requests (ignoring the users in IGNORE), and
    2. a tuple of:
        ("most popular challenge id", "amount of pull requests for that challenge")

    Calling this function on the default dirnames.txt should return:

    Stats(user='clamytoe', challenge=('01', 7))
    """
    if files is None:
        files = gen_files()

    users = Counter()
    popular_challenges = Counter()

    for f in files:
        challenge, user = f.split("/")

        if user not in IGNORE:
            users.update([user])
            popular_challenges.update([challenge])

    return Stats(
        user=users.most_common(1)[0][0], challenge=popular_challenges.most_common(1)[0]
    )


print(diehard_pybites())
