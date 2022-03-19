def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    pre = False
    occurrence = False
    while n :
        if occurrence == True :
            pre = True
        else :
            pre = False
        if n % 10 == 8 :
            occurrence = True
        else :
            occurrence = False
        n //= 10
        if occurrence and pre :
            return True
    return False