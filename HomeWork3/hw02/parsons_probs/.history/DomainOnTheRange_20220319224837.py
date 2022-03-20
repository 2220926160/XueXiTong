from cmath import inf
from curses.ascii import isdigit

def restrict_domain(f, low_d, high_d):
    """Returns a function that restricts the domain of F, 
    a function that takes a single argument x. 
    If x is not between LOW_D and HIGH_D (inclusive), 
    it returns -Infinity, but otherwise returns F(x).

    >>> from math import sqrt 
    >>> f = restrict_domain(sqrt, 1, 100) 
    >>> f(25) 
    5.0 
    >>> f(-25) 
    -inf 
    >>> f(125)
    -inf 
    >>> f(1)
    1.0 
    >>> f(100)
    10.0 
    """
    if isdigit(f):
        if f > low_d and f < high_d:
            return f
        else:
            return -inf
    return f    

f = restrict_domain(sqrt, 1, 100) 
f(25)
# if __name__ == '__main__':
#     import doctest
#     doctest.testmod(verbose=True)
