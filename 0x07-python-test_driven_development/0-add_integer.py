#!/usr/bin/python3


def add_integer(a, b=98):
    """
    Adds two integers or floats together.

    :param a: An integer or float.
    :param b: An integer or float. Defaults to 98.
    :return: The addition of a and b as an integer.

    >>> add_integer(5, 6)
    11
    >>> add_integer(5.5, 6)
    11
    >>> add_integer(5.5, 6.5)
    11
    >>> add_integer(5, "6")
    Traceback (most recent call last):
        ...
    TypeError: a must be an integer or b must be an integer
    """

    if type(a) not in (int, float) or type(b) not in (int, float):
        raise TypeError("a must be an integer or b must be an integer")
    else:
        result = int(a) + int(b)
        return result

