import hashlib
from math import ceil


def hash_query(query: str, length: int = 32) -> str:
    """Return a hash value for a given query.

    Args:
        query (str): An SQL query.
        length (int, optional): Length of the hash value. Defaults to 32.

    Raises:
        ValueError: Parameter length has to be greater equal 1.
        TypeError: Parameter length has to be of type integer.

    Returns:
        str: String representation of the hashed value.
    """
    # Input validation
    if not isinstance(length, int):
        raise TypeError("Parameter length has to be of type integer.")

    if length < 1:
        raise ValueError("Parameter length has to be greater equal 1.")

    # Query formatting
    trans_table = str().maketrans("", "", ';/"')
    normalized_query = str(query).lower().strip().translate(trans_table)

    # Split and sort to facilitate ignore column sequence
    normalized_query = " ".join(sorted(normalized_query.split()))

    # hash the query make sure intended length is returned.
    digest_length = ceil(length / 2)
    h = hashlib.shake_256(normalized_query.encode())
    return h.hexdigest(digest_length)[:length]
