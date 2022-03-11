# -*- coding: UTF-8 -*-

from sqlalchemy import false, trues

def k_in_num(k, num):
    """
    Complete k_in_num, a function which returns True if num has the digit k and
    returns False if num does not have the digit k. 0 is considered to have no
    digits.

    >>> k_in_num(3, 123) # .Case 1
    true
    >>> k_in_num(2, 123) # .Case 2
    true
    >>> k_in_num(5, 123) # .Case 3
    false
    >>> k_in_num(0, 0) # .Case 4
    false
    """
    if num == 0 and k == 0:
        return true
    while num != 0:
        if k == num % 10:
            return true
        num /= 10
    return false

if __name__=='__main__':
    import doctest
    doctest.testmod(verbose=True)