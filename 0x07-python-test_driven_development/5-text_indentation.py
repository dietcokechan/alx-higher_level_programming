#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    for idx, val in enumerate(text):
        if val in '?:.':
            print(text[i:idx + 1].strip() + '\n')
            i = idx + 1
    if not i:
        print(text, end='')
    elif i is not len(text):
        print(text[i:idx + 1].strip(), end='')
