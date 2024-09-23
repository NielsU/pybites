import csv
import requests
from collections import Counter

CSV_URL = "https://bites-data.s3.us-east-2.amazonaws.com/community.csv"


def get_csv():
    """Use requests to download the csv and return the
    decoded content"""
    r = requests.get(CSV_URL)
    r.encoding = "utf8"

    return r.text


def create_user_bar_chart(content):
    """Receives csv file (decoded) content and print a table of timezones
    and their corresponding member counts in pluses to standard output
    """
    reader = csv.DictReader(str(content).splitlines())

    c = Counter([row["tz"] for row in reader])

    for tz, count in c.items():
        print(f"{tz:<21}| " + "+" * count)
