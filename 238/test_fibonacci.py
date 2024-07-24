import pytest
from fibonacci import fib


# write one or more pytest functions below, they need to start with test_
@pytest.mark.parametrize("input", [-1, -2])
def test_raises_value_error(input):
    with pytest.raises(ValueError):
        fib(input)


@pytest.mark.parametrize(
    "input, expected",
    [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
        (7, 13),
        (8, 21),
        (9, 34),
        (10, 55),
        (11, 89),
        (12, 144),
        (13, 233),
        (14, 377),
        (15, 610),
        (16, 987),
        (17, 1597),
        (18, 2584),
        (19, 4181),
    ],
)
def test_valid_range(input, expected):
    assert fib(input) == expected
