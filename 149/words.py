def sort_words_case_insensitively(words):
    """Sort the provided word list ignoring case, and numbers last
    (1995, 19ab = numbers / Happy, happy4you = strings, hence for
     numbers you only need to check the first char of the word)

    """

    return sorted(
        words,
        key=lambda k: "z" * 3 + k.casefold() if k[0].isdigit() else k.casefold(),
    )
