from collections import namedtuple

from bs4 import BeautifulSoup as Soup
import requests
import re

PACKT = "https://bites-data.s3.us-east-2.amazonaws.com/packt.html"
CONTENT = requests.get(PACKT).text

Book = namedtuple("Book", "title description image link")


def deal_of_the_day(tag):
    if tag.name == "div" and tag.has_attr("id"):
        if tag["id"] == "deal-of-the-day":
            return True
    return False


def get_book():
    """make a Soup object, parse the relevant html sections, and return a Book namedtuple"""

    soup = Soup(CONTENT, "html.parser")
    dotd = soup.find(deal_of_the_day)

    img = dotd.find("img")
    img_src = img["src"]

    title_tag = dotd.find("div", class_="dotd-title")
    title = title_tag.find(re.compile("^h")).string.strip()

    br = dotd.find("br")
    description = ""

    for sibling in br.next_siblings:
        if sibling.name == "div":
            if sibling.string is not None:
                print(sibling.string)
                description = description.join(sibling.string.strip())

    link = dotd.a["href"]

    return Book(title=title, description=description, image=img_src, link=link)
