def pal(n): 
    """Return a palindrome starting with n.
    >>> pal(12430) 
    1243003421
    """
    m = n 
    while m: 
        n, m = n * 10 + m % 10 , m // 10
    return n

# print(pal(12430) )

def contains(a, b): 
    """Return whether the digits of a are contained in the digits of b.
    >>> contains(357, 12345678)
    True
    >>> contains(753, 12345678)
    False
    >>> contains(357, 37)
    False
    """ 
    if a == b:
        return True
    if _________ > _________: 
        return False
    if ______ == ________________________________________: 
        return contains( _______________________________ , _______________________________ )
    else:
        return contains( _______________________________ , _______________________________ )

import doctest 
doctest.testmod(verbose=True)