# -*- coding: UTF-8 -*-

from ast import operator


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
        f = operator.__add__
    else:
        f = operator.__add__

    return f(a, b)
    # return f


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
