from functools import wraps

known_users = ["bob", "julian", "mike", "carmen", "sue"]
loggedin_users = ["mike", "sue"]

"""
requirements: 
Using this decorator there are 3 possible scenarios you have to account for:

user is not on the system, return "please create an account"
user is on the system but not logged in, return "please login"
user is on the system and logged in, return the function's "welcome back {user}"
See also the tests for more details. Have fun and enjoy!
"""


def login_required(func):
    @wraps(func)
    def wrapper(*args):
        user = [*args][0]
        if user not in known_users:
            return "please create an account"
        if user not in loggedin_users:
            return "please login"
        return func(*args)

    return wrapper


@login_required
def welcome(user):
    """Return a welcome message if logged in"""
    return f"welcome back {user}"
