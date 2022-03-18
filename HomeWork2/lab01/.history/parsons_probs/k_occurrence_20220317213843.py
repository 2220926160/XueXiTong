# -*- coding: UTF-8 -*-

def k_occurrence(k, num):
    """
    >>> k_occurrence(5, 10)  # .Case 1
    0
    >>> k_occurrence(5, 5115)  # .Case 2
    2
    >>> k_occurrence(0, 100)  # .Case 3
    2
    >>> k_occurrence(0, 0)  # .Case 4
    0
    """
    "*** YOUR CODE HERE ***"
    result = 0
    while num > 0 :
        if (num % 10) == k :
            result += 1
        num //= 10
            
    return result
