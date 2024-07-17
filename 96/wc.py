def wc(file_):
    """Takes an absolute file path/name, calculates the number of
    lines/words/chars, and returns a string of these numbers + file, e.g.:
    3 12 60 /tmp/somefile
    (both tabs and spaces are allowed as separator)"""

    with open(file_) as f:
        file_content = f.read()
        nr_chars = len(file_content)
        lines = str(file_content).splitlines()
        nr_lines = len(lines)
        nr_words = len(str.split(file_content))

    return f"{nr_lines} {nr_words} {nr_chars} {file_}"


if __name__ == "__main__":
    # make it work from cli like original unix wc
    import sys

    print(wc(sys.argv[1]))
