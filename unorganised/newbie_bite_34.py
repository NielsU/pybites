import random


def guess_my_number() -> str:
    secret_number: int = random.randint(1, 100)
    user_guess: int = int(input("Please guess a number between 1 and 100."))

    if user_guess == secret_number:
        return "You got it!"
    elif user_guess > secret_number:
        return "Your guess is too high."
    else:
        return "Your guess is too low."
