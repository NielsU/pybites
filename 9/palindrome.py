"""A palindrome is a word, phrase, number, or other sequence of characters
which reads the same backward as forward"""

import os
import urllib.request
from math import ceil

TMP = os.getenv("TMP", "/tmp")
DICTIONARY = os.path.join(TMP, "dictionary_m_words.txt")
urllib.request.urlretrieve(
    "https://bites-data.s3.us-east-2.amazonaws.com/dictionary_m_words.txt", DICTIONARY
)


def load_dictionary():
    """Load dictionary (sample) and return as generator (done)"""
    with open(DICTIONARY) as f:
        return (word.lower().strip() for word in f.readlines())


def reverse(input: str):
    return "".join(char for char in reversed(input))


def is_palindrome(word):
    """Return if word is palindrome, 'madam' would be one.
    Case insensitive, so Madam is valid too.
    It should work for phrases too so strip all but alphanumeric chars.
    So "No 'x' in 'Nixon'" should pass (see tests for more)"""

    # Compare the reverse with first half of the string with the second half of the string.
    # Both halfs include the middle char

    # Keep only alphanumeric"
    word = "".join(char.lower() for char in word if char.isalnum())

    # Get lenght of half the word, round up to include the middel char of the word.
    half_length = ceil(float(len(word)) / 2)

    first_half = word[:half_length]

    # If lenght is even there is no middle char -> (len(word) % 2) == 0
    # Else second half should include middle char to enable being equal to first half
    second_half = word[half_length - (len(word) % 2) :]

    return reverse(first_half) == second_half


def get_longest_palindrome(words=None):
    """Given a list of words return the longest palindrome
    If called without argument use the load_dictionary helper
    to populate the words list"""

    if not words:
        words = list(load_dictionary())

    return max([word for word in words if is_palindrome(word)], key=len)


print(is_palindrome("A Toyota’s a Toyota."))
