from sympy import false, true


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
    pre = false
    occurrence = false
    while n :
        if occurrence == true :
            pre = true
        else :
            pre = false
        if n % 10 == 8 :
            occurrence = true
        else :
            occurrence = false
        n //= 10
        if occurrence and pre :
            return true
    return false