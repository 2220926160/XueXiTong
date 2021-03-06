def digit_pos_match(n, k):
    """
    >>> digit_pos_match(980, 0) # .Case 1
    True
    >>> digit_pos_match(980, 2) # .Case 2
    False
    >>> digit_pos_match(98276, 2) # .Case 3
    True
    >>> digit_pos_match(98276, 3) # .Case 4
    False
    """
    "*** YOUR CODE HERE ***"
    i = k
    while n > 0 and i > 0 :
        n /= 10
        i -= 1
    if n % 10 == k:
        return True
    else:
        return False