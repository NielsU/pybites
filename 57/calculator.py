import argparse


def calculator(operation, numbers):
    """TODO 1:
    Create a calculator that takes an operation and list of numbers.
    Perform the operation returning the result rounded to 2 decimals"""
    result = None
    if operation in ("a", "add"):
        result = numbers[0]
        for number in numbers[1:]:
            result += number
    elif operation in ("s", "sub"):
        result = numbers[0]
        for number in numbers[1:]:
            result -= number
    elif operation in ("d", "div"):
        result = numbers[0]
        for number in numbers[1:]:
            result /= number
    elif operation in ("m", "mul"):
        result = numbers[0]
        for number in numbers[1:]:
            result *= number
    else:
        return result

    return round(result, 2)


def create_parser():
    """TODO 2:
    Create an ArgumentParser object:
    - have one operation argument,
    - have one or more integers that can be operated on.
    Returns a argparse.ArgumentParser object.

    Note that type=float times out here so do the casting in the calculator
    function above!"""
    parser = argparse.ArgumentParser(description="A simple calculator")

    parser.add_argument(
        "-a",
        "--add",
        metavar="ADD",
        nargs="+",
        type=float,
        action="extend",
        help="Sums numbers",
    )

    parser.add_argument(
        "-s",
        "--sub",
        metavar="SUB",
        nargs="+",
        type=float,
        action="extend",
        help="Subtracts numbers",
    )

    parser.add_argument(
        "-m",
        "--mul",
        metavar="MUL",
        nargs="+",
        type=float,
        action="extend",
        help="Multiplies numbers",
    )

    parser.add_argument(
        "-d",
        "--div",
        metavar="DIV",
        nargs="+",
        type=float,
        action="extend",
        help="Divides numbers",
    )
    return parser


def call_calculator(args=None, stdout=False):
    """Provided/done:
    Calls calculator with provided args object.
    If args are not provided get them via create_parser,
    if stdout is True print the result"""
    parser = create_parser()

    if args is None:
        args = parser.parse_args()

    # taking the first operation in args namespace
    # if combo, e.g. -a and -s, take the first one
    for operation, numbers in vars(args).items():
        if numbers is None:
            continue

        try:
            res = calculator(operation, numbers)
        except ZeroDivisionError:
            res = 0

        if stdout:
            print(res)

        return res


if __name__ == "__main__":
    call_calculator(stdout=True)
