def tik(tok):
    """
    Returns a function that takes gram and prints tok and gram on a line.
    
    >>> tik(5)(6) 
    5
    6  
    """
    def insta(gram):
        print(gram, end=' ')
        return insta
    return insta(tok)
    
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
