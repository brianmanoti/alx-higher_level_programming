#!/usr/bin/python3
""" A fuction that reads a  text file"""
def read_file(filename=""):
    with (filename="", encoding="utf-8") as F:
        print(F.read())
