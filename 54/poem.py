INDENTS = 4
"""
    looks to me what is expected is:
    
    - to have paragraphs recognized by indentation instead of empty lines. 
    
    - so when empty line next line is not indented, every other line is indented. 
        - in onther words, for each line, append indentation. 
        - if prev was empty skip indendation           

"""


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
