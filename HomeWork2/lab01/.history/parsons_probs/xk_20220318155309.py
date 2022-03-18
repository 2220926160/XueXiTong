def xk(c, d):
    '''
    >>> xk(10, 10)
    
    >>> xk(10, 6)


    >>> xk(4, 6)


    >>> xk(0, 0)

    '''
    if c == 4:
        return 6
    elif d >= 4:
        return 6 + 7 + c
    else:
        return 25