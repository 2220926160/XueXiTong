def tik(tok):
    """
    Returns a function that takes gram and prints tok and gram on a line.
    >>> tik(5)(6)
    5 6
    """
    def insta(gram):
        print(tok, gram)
    return insta


# tik(5)(6)
tik(tik(5)(print(6)))(print(7))

# if __name__ == '__main__':
#     import doctest
#     doctest.testmod(verbose=True)
