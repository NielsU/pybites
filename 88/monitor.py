from collections import Counter
from contextlib import contextmanager
from datetime import date
from time import time

OPERATION_THRESHOLD_IN_SECONDS = 2.2
ALERT_THRESHOLD = 3
ALERT_MSG = "ALERT: suffering performance hit today"

violations = Counter()


def get_today():
    """Making it easier to test/mock"""
    return date.today()


@contextmanager
def timeit():
    start_time = time()

    yield None

    end_time = time()
    duration = end_time - start_time

    if duration >= OPERATION_THRESHOLD_IN_SECONDS:
        violations.update([get_today()])

        if violations.get(get_today(), 0) >= ALERT_THRESHOLD:
            print(ALERT_MSG)


with timeit():
    print("hello")
