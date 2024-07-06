ninjabelt_scores = {
    "white": 10,
    "yellow": 20,
    "orange": 30,
    "green": 40,
    "blue": 50,
    "brown": 60,
    "black": 70,
}


def look_up_score(belt_key: str) -> str:
    # your code
    score: int = ninjabelt_scores[belt_key]
    message: str = f"Your {belt_key} belt has a score of {score}."
    return message


ninjabelt_scores = {
    "white": 10,
    "yellow": 20,
    "orange": 30,
    "green": 40,
    "blue": 50,
    "brown": 60,
    "black": 70,
}


def look_up_score_advanced(belt_key: str) -> str:
    score: int = ninjabelt_scores.get(belt_key)
    message: str = ""

    if score != None:
        message = f"Your {belt_key} belt has a score of {score}."
    else:
        message = f"A {belt_key} belt does not exist."

    return message
