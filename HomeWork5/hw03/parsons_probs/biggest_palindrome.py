# def pal(n): 
#     """Return a palindrome starting with n.
#     >>> pal(12430) 
#     1243003421
#     >>> pal(1100)
#     11000011
#     """
#     m = n 
#     while m: 
#         n, m = n * 10 + m % 10 , m // 10
#     return n

from secrets import choice


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
    if a > b: 
        return False
    if a % 10 == b % 10: 
        return contains(a // 10, b // 10)
    else:
        return contains(a, b // 10)
    
def biggest_palindrome(n):
    """Return the largest even-length palindrome in n.
    >>> biggest_palindrome(3425534) 
    4554
    >>> biggest_palindrome(126130450234125)
    21300312
    """
    return big(n, 0)
    
def big(n, k): 
    """A helper function for biggest_palindrome."""
    choice = []
    
    # if n == 0: 
    #     return 0
    # choices = [big(n // 10, k) , big( ____ , _____ )] 
    # if contains(k, n): 
    #     choices += k
    # return max(choices)

import doctest 
doctest.testmod(verbose=True)