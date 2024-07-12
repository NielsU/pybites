INDENTS = 4


def print_hanging_indents(poem: str):
    new_paragraph: bool = False
    formatted_poem = []

    for line in poem.split("\n"):
        line = line.lstrip()

        if len(line) <= 0:
            new_paragraph = True
            continue
        elif not new_paragraph:
            line = " " * INDENTS + line
        else:
            new_paragraph = False

        formatted_poem.append(line + "\n")

    print("".join(formatted_poem))
