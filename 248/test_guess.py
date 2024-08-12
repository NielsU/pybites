from unittest.mock import patch
import pytest

from guess import GuessGame, InvalidNumber, MAX_NUMBER
from contextlib import nullcontext as does_not_raise


def test_max_number():
    assert MAX_NUMBER == 15


# write test code to reach 100% coverage and a 100% mutpy score


ask_for_input_text = "Guess a number: \n"
correct_guess_response = "You guessed it!\n"


def test_init_default_max_guesses():
    g = GuessGame(4)
    assert g.max_guesses == 5


"""
     test validations
"""


def test_init_validations():
    with pytest.raises(InvalidNumber, match="Not a number"):
        GuessGame("not_a_number")

    with pytest.raises(InvalidNumber, match="Negative number"):
        GuessGame(-1)

    with pytest.raises(InvalidNumber, match="Number too high"):
        GuessGame((MAX_NUMBER + 1))

    with does_not_raise():
        GuessGame(0)
        GuessGame(MAX_NUMBER)


def test_validations_function():
    # Just to also test the valdidation function directly.
    g = GuessGame(1)
    with pytest.raises(InvalidNumber, match="Not a number"):
        g._validate("still not a number")

    with pytest.raises(InvalidNumber, match="Negative number"):
        g._validate(-1)

    with pytest.raises(InvalidNumber, match="Number too high"):
        g._validate((MAX_NUMBER + 1))


""" Test plan:
    output common: "Guess a number: \n"

    input output effect 
    1- input: not a number output (adds) :" "Enter a number, try again\n"
    2- input: number equal to secret_number output (adds): You guessed it!\n
    3- input: < secret_numbers output: "Too low\n" 
    4- input: < secret_number: "Too high\n"    
    5- max guesses exceeded: f"Sorry, the number was {self.secret_number}\n"

    test_call_scenarios:
    1 - sunny day guessed right first try
    2 - to high,  max guesses exceeded
    3 - to low, guessed it
    4 - not a number, guesed it
    
    
"""
# fmt: off
@pytest.mark.parametrize(
    "secret_number,max_guesses,side_effect,expected_output",
    [
        pytest.param(1, 5, ["1"], f"{ask_for_input_text}{correct_guess_response}", id="scenario 1"),
        pytest.param(4, 1, ["5"], f"{ask_for_input_text}Too high\nSorry, the number was 4\n", id="scenario 2"),
        pytest.param(5, 2, ["4","5"], f"{ask_for_input_text}Too low\n{ask_for_input_text}{correct_guess_response}", id="scenario 3"),
        pytest.param(5, 3, ["NotANumber","5"], f"{ask_for_input_text}Enter a number, try again\n{ask_for_input_text}{correct_guess_response}", id="scenario 4"),
    ],
)
#fmt_on
@patch("builtins.input")
def test_call_scenarios(
    mock_input, secret_number, max_guesses, side_effect, expected_output, capsys
):
    mock_input.side_effect = side_effect
    g = GuessGame(secret_number, max_guesses)
    g()
    cap = capsys.readouterr()

    assert cap.out == expected_output
