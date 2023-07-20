#!/usr/bin/python3

class Base:
    """
    This is the Base class that represents a base object.

    Attributes:
        __nb_objects (int): A private class attribute to keep track of the number of instances created.
        id (int): A public instance attribute representing the ID of the object.

    Methods:
        __init__(self, id=None): The constructor method to initialize a Base object.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a Base object.

        Args:
            id (int, optional): The ID for the object. If not provided, it will be auto-generated.

        Returns:
            None
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

