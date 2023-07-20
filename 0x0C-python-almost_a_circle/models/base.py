#!/usr/bin/python3

class Base:
    """Base class that takes Id as an argument
    args: id - the identufication given to the first argument
    """
    __nb_objects = 0
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
