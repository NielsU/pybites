def get_index_different_char(chars):
    alpha = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")

    # Devide alphanumeric chars from non alpha chars in separate dictionaries linked to their original index
    # The char index is used as key as those are unique.
    alpha_dict = {idx: char for idx, char in enumerate(chars) if str(char) in alpha}
    non_alpha_dict = {
        idx: char for idx, char in enumerate(chars) if str(char) not in alpha
    }

    # List the keys for both dictionaries,which are the indexes
    alpha_idx = list(alpha_dict.keys())
    non_alpha_idx = list(non_alpha_dict.keys())

    # The list with length 1 is the odd char, return its value being the index
    if len(alpha_idx) == 1:
        return alpha_idx[0]
    else:
        return non_alpha_idx[0]


print(get_index_different_char([1, "=", 3, 4, 5, "A", "b", "a", "b", "c"]))  # prints 1
