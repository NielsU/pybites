import pytest

from numbers_to_dec import list_to_decimal


@pytest.mark.parametrize("input", [[-1], [-11], [10], [11], [100]])
def test_out_of_range(input):
    with pytest.raises(ValueError):
        list_to_decimal(input)


@pytest.mark.parametrize(
    "input", [["1"], [1.0], [True], [{"abc": 1}], [[]], ["invalid"]]
)
def test_invalid_type(input):
    with pytest.raises(TypeError):
        assert list_to_decimal(input)


@pytest.mark.parametrize(
    "input,expected",
    [
        ([1, 2, 3], 123),
        ([4, 5, 6], 456),
        ([7, 8, 9], 789),
        ([0], 0),
        ([1], 1),
        ([2], 2),
        ([3], 3),
        ([4], 4),
        ([5], 5),
        ([6], 6),
        ([7], 7),
        ([8], 8),
        ([9], 9),
    ],
)
def test_valid_range(input, expected):
    assert list_to_decimal(input) == expected
