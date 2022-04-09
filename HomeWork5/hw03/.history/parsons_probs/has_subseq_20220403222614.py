from pymysql import NULL


def has_subseq(n, seq):
    """
    Complete has_subseq, a function which takes in a number n and a "sequence"
    of digits seq and returns whether n contains seq as a subsequence, which
    does not have to be consecutive.

    >>> has_subseq(123, 12)
    True
    >>> has_subseq(141, 11)
    True
    >>> has_subseq(144, 12)
    False
    >>> has_subseq(144, 1441)
    False
    >>> has_subseq(1343412, 134)
    True
    """
    "*** YOUR CODE HERE ***"
    i = 0
    while n:
        j = 0
        t = i
        while seq[j]:
            if n[t] == seq[j]:
                t += 1
                j += 1
        if seq[j] is NULL:
            return True
        i += 1
    return False

import doctest
doctest.testmod()
