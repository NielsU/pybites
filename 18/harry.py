import os
import urllib.request
import string
from collections import Counter

# data provided
tmp = os.getenv("TMP", "/tmp")
stopwords_file = os.path.join(tmp, "stopwords")
harry_text = os.path.join(tmp, "harry")
urllib.request.urlretrieve(
    "https://bites-data.s3.us-east-2.amazonaws.com/stopwords.txt", stopwords_file
)
urllib.request.urlretrieve(
    "https://bites-data.s3.us-east-2.amazonaws.com/harry.txt", harry_text
)


def list_stopwords():
    with open(stopwords_file) as swf:
        return swf.read().splitlines()


def get_harry_most_common_word():
    stopwords_list = list_stopwords()

    harry_words = []
    # read harry text
    with open(harry_text, encoding="utf-8") as ht:
        content = ht.read()

        # requirement: Make sure you convert to lowercase, strip out non-alphanumeric characters and stopwords.
        for line in content.splitlines():

            for word in line.split():
                # clean the words
                word = word.lower().strip(string.punctuation + string.whitespace)

                # exclude stop words and empty strings
                if word not in stopwords_list and word != "":
                    harry_words.append(word)

    # count words
    wc = Counter()
    wc.update(harry_words)

    # requirement: Your function should return a tuple of (most_common_word, frequency).
    return wc.most_common(1)[0]
