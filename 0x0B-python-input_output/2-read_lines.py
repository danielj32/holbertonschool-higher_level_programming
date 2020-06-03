#!/usr/bin/python3
""" function read n lines in stdout"""


def read_lines(filename="", nb_lines=0):
    """reads n lines of a text file (UTF8)
     and prints it to stdout: """
    with open(filename, 'r', encoding='utf8') as f:
        if nb_lines <= 0:
            print(f.read(), end='')
        else:
            for i in f:
                if nb_lines == 0:
                    break
                print(i, end='')
                nb_lines -= 1
