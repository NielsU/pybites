"""
    solution idea's:
        1 - Default dict as counter, return (first item in) list of keys sorted by max value. (loops through entire list)
        2 - same as 1 but remove the counted values from list so that looping through entire number is not needed. 
        3 - count same as previous but create new view (map) of prevous map excluding the counted number?
        4 - ah!! collections counter! :) 
"""

from collections import Counter


def freq_digit(num: int) -> int:
    number, _ = Counter(str(num)).most_common(1)[0]
    return int(number)
