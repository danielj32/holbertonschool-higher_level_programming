#!/usr/bin/python3
def text_indentation(text):
        if type(text) is not str:
                raise TypeError("text must be a string")
        print(text)
        new_line = ['.', '?', ':']

        for c in range(len(text)):
                if text[c] is " " and text[c - 1] in new_line:
                        continue
                print(text[c], end="")
                if text[c] == ".":
                        print("", end="\n\n")
                if text[c] == "?":
                        print("", end="\n\n")
                if text[c] == ":":
                        print("", end='\n\n')
        print()
        print()
