from datetime import datetime
import json
import os
from pathlib import Path
from urllib.request import urlretrieve
from typing import NamedTuple

import pytest

from zodiac import (
    get_signs,
    get_sign_with_most_famous_people,
    signs_are_mutually_compatible,
    get_sign_by_date,
    Sign,
)

# original source: https://zodiacal.herokuapp.com/api
URL = "https://bites-data.s3.us-east-2.amazonaws.com/zodiac.json"
TMP = os.getenv("TMP", "/tmp")
PATH = Path(TMP, "zodiac.json")


@pytest.fixture(scope="module")
def signs():
    if not PATH.exists():
        urlretrieve(URL, PATH)
    with open(PATH, encoding="utf-8") as f:
        data = json.loads(f.read())
    return get_signs(data)


""" 
    Requirements for tests:
    1. correct syntax, 
    2. pytest passes all tests, 
    3. 100% coverage, 
    4. 100% mutation score (mutpy)
"""


def test_sign_type():
    assert "zodiac.Sign" in str(Sign)


def test_get_sign_with_most_famous_people(signs):
    result = get_sign_with_most_famous_people(signs)
    assert isinstance(result, tuple)
    assert isinstance(result[0], str)
    assert isinstance(result[1], int)
    assert result == ("Scorpio", 35)
    assert len(result) == 2


@pytest.fixture(scope="module")
def epmty_list():
    return []


@pytest.fixture(scope="module")
def signs_for_compatibilitytest():
    return [
        Sign(name="A", compatibility=["B", "D"], famous_people=[], sun_dates=[]),
        Sign(name="B", compatibility=["A"], famous_people=[], sun_dates=[]),
        Sign(name="C", compatibility=["A"], famous_people=[], sun_dates=[]),
        Sign(name="D", compatibility=["A"], famous_people=[], sun_dates=[]),
    ]


# fmt: off
@pytest.mark.parametrize("signs,sign1,sign2,expected",[
    ("signs_for_compatibilitytest","A","B",True),  #sign1 first compatible with sign2 => True
    ("signs_for_compatibilitytest","B","A",True),  #sign2 first compatible with sign1 => True
    ("signs_for_compatibilitytest","D","A",True),  #to check that compatibility remains a list supporting multiple items.
    ("signs_for_compatibilitytest","C","A",True),  #only one needs to be compatible with the other
    ("signs_for_compatibilitytest","C","D",False), #no compatibility match => false
    ("signs_for_compatibilitytest","X","Y",False),  #both signs not present in list => False
    ("epmty_list","A","B",False) #empty signs list => False
    ])
# fmt: on


def test_signs_are_mutually_compatible(request, signs, sign1, sign2, expected):
    signs_list = request.getfixturevalue(signs)
    assert signs_are_mutually_compatible(signs_list, sign1, sign2) == expected


def test_signs_are_mutually_compatible_required_input():
    with pytest.raises(TypeError):
        signs_are_mutually_compatible()
        signs_are_mutually_compatible([])
        signs_are_mutually_compatible("", "")


def test_get_sign_by_date():
    # fmt: off
    local_signs=[Sign(name="A",compatibility=[],famous_people=[],sun_dates=["January 2", "February 1"]),
            Sign(name="B",compatibility=[],famous_people=[],sun_dates=["February 2", "March 1"])]
    # fmt: on
    # match start
    assert get_sign_by_date(local_signs, datetime(2022, 1, 2)) == "A"
    # match end
    assert get_sign_by_date(local_signs, datetime(2022, 2, 1)) == "A"
    # in range
    assert get_sign_by_date(local_signs, datetime(2022, 1, 15)) == "A"
    # no match becouse no sign in scope
    assert get_sign_by_date(local_signs, datetime(2022, 3, 15)) is None
    # no match becouse of no input
    assert get_sign_by_date([], datetime(2022, 3, 15)) is None
