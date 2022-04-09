import doctest

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
    while n:
        isExist = False
        while n > 0 and ~isExist:
            if n % 10 == seq % 10:
                isExist = ~isExist
            n //= 10
        seq //= 10  
    if seq == 0:
        return True
    return False

# doctest.testmod(verbose=True)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
