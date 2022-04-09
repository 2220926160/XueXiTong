import doctest
from numpy import number
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
    number = -1
    seqCopy = seq
    while seqCopy:
        seqCopy //= 10
        number += 1
    while n:
        if n < seq:
            return False
        nCopy = n
        while nCopy:
            pass
    
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


doctest.testmod()
