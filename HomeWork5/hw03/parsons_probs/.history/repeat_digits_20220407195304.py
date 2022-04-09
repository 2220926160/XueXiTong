def repeat_digits(n):
    """Given a positive integer N, returns a number with each digit repeated.
    >>> repeat_digits(1234) 
    11223344 
    """
    # i = 1
    # sum = 0
    # while n:
    #     x = n % 10
    #     sum += pow(10, i) * x + pow(10, i - 1) * x
    #     n //= 10
    #     i += 2
    # return sum
    # last, rest = n % 10, n * 10
    # if n == 0:
    #     return last
    # return repeat_digits(n // 10) * 10 + last

print(repeat_digits(1))
print(repeat_digits(1234))