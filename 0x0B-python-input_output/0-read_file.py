#!/usr/bin/python3
"""
function that reads a text
file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """
    function that reads a text file
    """
    with open('filename', mode='r', encoding='utf-') as file:
        print(file.read(), end='')
