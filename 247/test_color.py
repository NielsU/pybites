from unittest.mock import patch

import pytest

import color


@pytest.fixture(scope="module")
def gen():
    return color.gen_hex_color()


@patch("color.sample")
def test_gen_hex_color(MockSample, gen):
    MockSample.return_value = 10, 10, 10
    assert next(gen) == "#0A0A0A"


@patch(target="color.sample", autospec=True)
def test_gen_hex_color_FF(MockSample, gen):
    MockSample.return_value = 255, 255, 255
    assert next(gen) == "#FFFFFF"


@patch(target="color.sample")
def test_gen_hex_color_out_verify_input_range(MockSample, gen):
    MockSample.return_value = 255, 255, 255
    next(gen)
    MockSample.assert_called_with(range(0, 256), 3)

    args = MockSample.call_args.args

    assert args[1] == 3
    assert args[0] == range(0, 256)


if __name__ == "__main__":
    mock = test_gen_hex_color_out_verify_input_range(gen)
    a = mock
