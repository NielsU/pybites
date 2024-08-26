class RecordScore:
    """Class to track a game's maximum score"""

    def __init__(self):
        self._scores = []

    def __call__(self, score: int) -> int:
        self._scores.append(score)
        self._scores.sort()
        return self._scores[-1]
