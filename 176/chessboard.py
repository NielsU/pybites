"""
:) This bite reminded me to model things as they really are, 
that the perspective on the problem to solve makes the difference.

My mind was on printing rows, not on the actual thing, constructing a board.
After building my solution i realise it works only for even sizes.

I added some logic to append a char depening on size being even.
Looked at the code and thought well, the tests dont require it. 
Code is now more complicated. lets not be perfectionistic to add unneeded logic. So i removed it.

Than seeing the provided solution  (adding the char based on position on the board in nested for loop),
i realised if i had had the perspective of constructing a board,
i may have ended up building it with support for odd size without even thinking about it,
and the solution would be just as simple. :).
"""

WHITE, BLACK = " ", "#"


def create_chessboard(size=8):
    """Create a chessboard with of the size passed in.
    Don't return anything, print the output to stdout"""

    for row_nr in range(1, size + 1):
        if row_nr % 2 == 0:
            print((BLACK + WHITE) * int(size / 2))
        else:
            print((WHITE + BLACK) * int(size / 2))
