from collections import defaultdict
import os
from urllib.request import urlretrieve
import string

from bs4 import BeautifulSoup


# prep data
tmp = os.getenv("TMP", "/tmp")
page = "us_holidays.html"
holidays_page = os.path.join(tmp, page)
urlretrieve(f"https://bites-data.s3.us-east-2.amazonaws.com/{page}", holidays_page)

with open(holidays_page) as f:
    content = f.read()

holidays = defaultdict(list)


def get_us_bank_holidays(content=content):
    """Receive scraped html output, make a BS object, parse the bank
    holiday table (css class = list-table), and return a dict of
    keys -> months and values -> list of bank holidays"""
    holidays = defaultdict(list)

    # the soup got spoiled, so added some cleaning to remove line breaks and white space from the html content.
    lines = content.splitlines()
    lines = [line.strip(string.whitespace) for line in lines if line != " "]
    cleaned_content = "".join(lines)

    soup = BeautifulSoup(cleaned_content, "html.parser")

    # first table is the one with holidays
    table = soup.find_all(name="table")[0]

    for tr in table.tbody.children:
        month = tr.find("time")["datetime"].split("-")[1]
        holiday = tr.contents[3].find("a").string.strip()

        holidays[month].append(holiday)

    return holidays
