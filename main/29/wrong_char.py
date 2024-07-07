def get_index_different_char(chars):
    alpha = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")

    # Get indexes by filtering through list comprehention, the index of odd char is in list of len 1.
    alpha_idx = [i for i, char in enumerate(chars) if char in alpha]
    non_alpha_idx = [i for i, char in enumerate(chars) if char not in alpha]

    # Return the index matching the odd char.
    if len(alpha_idx) == 1:
        return alpha_idx[0]
    else:
        return non_alpha_idx[0]
