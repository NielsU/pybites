def is_armstrong(n: int) -> bool:
    # initialize sum
    sum = 0
    power = len(str(n))

    for digit in str(n):
        sum += int(digit) ** power

    return sum == n


def is_armstrong1(n: int) -> bool:
    # initialize sum
    sum = 0
    power = len(str(n))

    temp = n
    while temp > 0:
        digit = temp % 10
        sum += digit**power
        temp //= 10

    return sum == n
