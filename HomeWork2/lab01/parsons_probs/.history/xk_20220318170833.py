def xk(c, d):
    '''
    >>> xk(10, 10) # case 1
    23
    >>> xk(10, 6) # case 2
    23
    >>> xk(4, 6) # case 3
    6
    >>> xk(0, 0) # case 4
    25
    '''
    if c == 4:
        return 6
elif d >= 4:
        return 6 + 7 + c
    else:
        return 25