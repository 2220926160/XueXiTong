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

import doctest 
doctest.testmod(verbose=True)