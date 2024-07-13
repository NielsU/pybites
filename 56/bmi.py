import argparse


def calc_bmi(weight, length):
    """Provided/DONE:
    Calc BMI give a weight in kg and length in cm, return the BMI
    rounded on 2 decimals"""
    bmi = int(weight) / ((int(length) / 100) ** 2)
    return round(bmi, 2)


def create_parser():
    """TODO:
    Create an ArgumentParser adding the right arguments to pass the tests,
    returns a argparse.ArgumentParser object

      -h, --help            show this help message and exit
        -w WEIGHT, --weight WEIGHT
                                Your weight in kg
        -l LENGTH, --length LENGTH
                                Your length in cm

    """
    parser = argparse.ArgumentParser(
        prog="bmy.py", description="Calculate your BMI.", exit_on_error=True
    )

    parser.add_argument(
        "-w", "--weight", required=False, type=int, help="Your weight in kg"
    )
    parser.add_argument(
        "-l", "--length", required=False, type=int, help="Your length in cm"
    )

    return parser


def handle_args(args=None):
    """Provided/DONE:
    Call calc_bmi with provided args object.
    If args are not provided get them from create_parser"""
    if args is None:
        parser = create_parser()
        args = parser.parse_args()

    if args.weight and args.length:
        bmi = calc_bmi(args.weight, args.length)
        print(f"Your BMI is: {bmi}")
    else:
        print("Need both weight and length args")


if __name__ == "__main__":
    handle_args()
