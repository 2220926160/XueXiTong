from itertools import count
from attr import has


def neighbor_digits(num, prev_digit=-1):
    """
    Returns the number of digits in num that have the same digit to its right
    or left.
    >>> neighbor_digits(111)
    3
    >>> neighbor_digits(123)
    0
    >>> neighbor_digits(112)
    2
    >>> neighbor_digits(1122)
    4
    """
    "*** YOUR CODE HERE ***"
    hash = []
    # print(str(hash))?
    for i in range(10):
        hash.append(-1)
    count = 0
    while num:
        hash[num % 10] += 1
        num //= 10
    for i in hash:
        if i != -1:
            count += i
    return count
# neighbor_digits(0)
