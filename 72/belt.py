from itertools import takewhile

scores = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
belts = "white yellow orange green blue brown black paneled red".split()


def get_belt(user_score, scores=scores, belts=belts):
    belt_levels = dict(zip(scores, belts))

    # handle min max level
    if user_score < 10:
        return None
    if user_score >= 1000:
        return belts[-1]

    # get the level of current user score
    current_score_level = list(takewhile(lambda x: x <= user_score, scores))[-1]

    # return belt matching current level.
    return belt_levels[current_score_level]
