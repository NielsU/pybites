import pytest

from fizzbuzz import fizzbuzz


@pytest.mark.parametrize(
    "input,expected_result",
    [
        (1, 1),
        (2, 2),
        (3, "fizz"),
        (4, 4),
        (5, "buzz"),
        (6, "fizz"),
    ],
)
def test_fizzbuzz(input, expected_result):
    assert fizzbuzz(input) == expected_result
