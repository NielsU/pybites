import pytest
from fizzbuzz import fizzbuzz


# write one or more pytest functions below, they need to start with test_
@pytest.mark.parametrize(
    "num,output",
    [
        (0, "Fizz Buzz"),
        (1, 1),
        (2, 2),
        (3, "Fizz"),
        (4, 4),
        (5, "Buzz"),
        (6, "Fizz"),
        (7, 7),
        (8, 8),
        (9, "Fizz"),
        (10, "Buzz"),
        (11, 11),
        (12, "Fizz"),
        (13, 13),
        (14, 14),
        (15, "Fizz Buzz"),
        (16, 16),
        (17, 17),
        (18, "Fizz"),
        (19, 19),
        (20, "Buzz"),
    ],
)
def test_fizzbuss(num, output):
    assert fizzbuzz(num) == output
