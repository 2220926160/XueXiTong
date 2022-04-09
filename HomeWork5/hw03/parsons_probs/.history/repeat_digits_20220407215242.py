def repeat_digits(n):
    """Given a positive integer N, returns a number with each digit repeated.
    >>> repeat_digits(1234) 
    11223344 
    >>> repeat_digits(23) 
    2233
    >>> repeat_digits(456123) 
    445566112233
    """
    # i = 1
    # sum = 0
    # while n:
    #     x = n % 10
    #     sum += pow(10, i) * x + pow(10, i - 1) * x
    #     n //= 10
    #     i += 2
    # return sum
    last, rest = n % 10, n % 10 * 10 + n % 10
    if n == 0:
        return 0
    return repeat_digits(n // 10) * 100 + rest


import doctest
doctest.testmod(verbose=True)