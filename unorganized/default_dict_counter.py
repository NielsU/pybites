"""
    To practice using default dict as counter and some text cleaning. 
"""

from collections import defaultdict
import string

TEXT = """Lets see if this works, splitting, stripping, counting words.
hello, hello hello! not-separate-words."""


def count_word_occurance_in_text(text: str) -> defaultdict:
    """
    Counts the number each word occurs in the provided text.
    """
    wordcount = defaultdict(int)

    for word in text.split():
        clean_word = word.strip(string.punctuation + string.whitespace).casefold()

        wordcount[clean_word] += 1

    return wordcount


for word, count in count_word_occurance_in_text(TEXT).items():
    print(f"{word}:{count}")
