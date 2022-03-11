# -*- coding: UTF-8 -*-

def two_of_three(i, j, k):
    """Return m*m + n*n, where m and n are the two smallest members of the
    positive numbers i, j, and k.

    >>> two_of_three(1, 2, 3)
    5
    >>> two_of_three(5, 3, 1)
    10
    >>> two_of_three(10, 2, 8)
    68
    >>> two_of_three(5, 5, 5)
    50
    """
    return (min(i, j, k) * min(i, j, k) + min((i > j ? i: j), k))


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
