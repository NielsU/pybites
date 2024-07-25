import pytest, sys

from workouts import print_workout_days

""" workouts table to test. 
{
'mon': 'upper body #1',
'tue': 'lower body #1',
'wed': '30 min cardio',
'thu': 'upper body #2',
'fri': 'lower body #2'}
"""


@pytest.mark.parametrize(
    "input, expected",
    [
        ("Upper Body #1", "Mon\n"),
        ("Lower Body #1", "Tue\n"),
        ("30 min cardio", "Wed\n"),
        ("upper body #2", "Thu\n"),
        ("lower body #2", "Fri\n"),
        ("Upper", "Mon, Thu\n"),
        ("upper", "Mon, Thu\n"),
        ("lower", "Tue, Fri\n"),
        ("Body", "Mon, Tue, Thu, Fri\n"),
        ("#", "Mon, Tue, Thu, Fri\n"),
        ("30", "Wed\n"),
        ("min", "Wed\n"),
        ("cardio", "Wed\n"),
        ("1", "Mon, Tue\n"),
        ("2", "Thu, Fri\n"),
        (" ", "Mon, Tue, Wed, Thu, Fri\n"),
        ("notAmatch", "No matching workout\n"),
        ("", "Mon, Tue, Wed, Thu, Fri\n"),
    ],
)
def test_print_workout_days(capsys, input, expected):
    print_workout_days(input)
    captured = capsys.readouterr()

    assert captured.out == expected


@pytest.mark.parametrize(
    "input, expected",
    [
        ("Upper Body #1", "Mon\n"),
        ("Lower Body #1", "Tue\n"),
        ("30 min cardio", "Wed\n"),
        ("upper body #2", "Thu\n"),
        ("lower body #2", "Fri\n"),
        ("Upper", "Mon, Thu\n"),
        ("upper", "Mon, Thu\n"),
        ("lower", "Tue, Fri\n"),
        ("Body", "Mon, Tue, Thu, Fri\n"),
        ("#", "Mon, Tue, Thu, Fri\n"),
        ("30", "Wed\n"),
        ("min", "Wed\n"),
        ("cardio", "Wed\n"),
        ("1", "Mon, Tue\n"),
        ("2", "Thu, Fri\n"),
        (" ", "Mon, Tue, Wed, Thu, Fri\n"),
        ("notAmatch", "No matching workout\n"),
        ("", "Mon, Tue, Wed, Thu, Fri\n"),
    ],
)
def test_print_workout_days_capfd(capfd, input, expected):
    print_workout_days(input)
    captured = capfd.readouterr()

    assert captured.out == expected
