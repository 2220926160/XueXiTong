from curses.ascii import isdigit


def tik(tok):
    """
    Returns a function that takes gram and prints tok and gram on a line.
    
    >>> tik(5)
    5
    >>> tik(5)(6)
    5 6 
    """
    def insta(gram):
        # if (hasattr(gram, '__call__')):
        #     gram
        # else:
        #     print(gram, end=' ')
        print(tok,gram)
    return insta


# tik(5)(6)
# tik(tik(5)(print(6)))(print(7))

# if __name__ == '__main__':
#     import doctest
#     doctest.testmod(verbose=True)
