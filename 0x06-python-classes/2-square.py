#!/usr/bin/python3
"""Declares a class called Square With Private Attributes"""

class square:
    """
    A class called Square

    arg: size- a private attribute for defining its size
    """

    def __init__(self, size, size=0):
        """Initialises the size attribute"""
        if type(size) is int:
            if size < 0 :
                raise ValueError("size must >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")
