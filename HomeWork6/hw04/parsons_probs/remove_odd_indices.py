import imp


def remove_odd_indices(lst, odd):
    """ 
    Remove elements of lst that have odd indices.
    >>> s = [1, 2, 3, 4]
    >>> t = remove_odd_indices(s, True)
    >>> s
    [1, 2, 3, 4]
    >>> t
    [1, 3]
    >>> l = [5, 6, 7, 8]
    >>> m = remove_odd_indices(l, False)
    >>> m
    [6, 8]
    """
    if odd:
        return [x for x in lst if x % 2 == 1]  
    else:
        return [x for x in lst if x % 2 == 0]

import doctest
doctest.testmod(verbose=True)