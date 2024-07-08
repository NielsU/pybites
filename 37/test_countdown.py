import inspect

import pytest

from countdown import countdown_for, countdown_recursive

expected = """10
9
8
7
6
5
4
3
2
1
time is up
"""
expected_other_start_arg = """13
12
11
"""
expected_other_start_arg += expected


def test_countdown_for(capfd):
    countdown_for()
    out, _ = capfd.readouterr()
    assert out == expected


def test_countdown_recursive(capfd):
    countdown_recursive()
    out, _ = capfd.readouterr()
    assert out == expected


def test_test_countdown_recursive_different_start(capfd):
    countdown_recursive(13)
    out, _ = capfd.readouterr()
    assert out == expected_other_start_arg


def test_recursion_used():
    func = countdown_recursive
    err = f"expecting {func.__name__} twice in your answer"
    assert inspect.getsource(func).count(func.__name__) == 2, err


def test_countdown_from_zero_prints_time_is_up(capfd):
    countdown_for(0)
    out, _ = capfd.readouterr()
    assert out.strip() == "time is up"


def test_countdown_recursive_from_zero_prints_time_is_up(capfd):
    try:
        countdown_recursive(0)
    except RecursionError:
        pytest.fail("countdown_recursive(0) raised a RecursionError exception")
    out, _ = capfd.readouterr()
    assert out.strip() == "time is up"
