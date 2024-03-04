#!/usr/bin/python3
"""Declares a class called Square With Private Attributes"""

class square:
    """
    A class called Square

    arg: size- a private attribute for defining its size
    """

    def __init__(self, size=0):
        """Initialises the size attribute"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
