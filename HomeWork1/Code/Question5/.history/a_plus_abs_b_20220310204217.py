# -*- coding: UTF-8 -*-

# from ast import operator
import operator
from audioop import add


def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    >>> a_plus_abs_b(-1, 4)
    3
    >>> a_plus_abs_b(-1, -4)
    3
    """
    if b < 0:
        f = add
    else:
        f = add
    return f(a, b)
    # return f

print(operator.)

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
