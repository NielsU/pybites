WHITE, BLACK = " ", "#"


def create_chessboard(size=8):
    """Create a chessboard with of the size passed in.
    Don't return anything, print the output to stdout"""

    for row_nr in range(1, size + 1):
        if row_nr % 2 == 0:
            print((BLACK + WHITE) * int(size / 2))
        else:
            print((WHITE + BLACK) * int(size / 2))
