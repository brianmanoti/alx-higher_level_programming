#!/usr/bin/pythone3


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout.

    :param filename: The name of the file to read.
    :type filename: str
    """
    with open(filename, mode='r', encoding='utf-8') as f:
        for line in f:
            print(line, end='')

