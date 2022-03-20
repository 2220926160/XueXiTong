def tik(tok):
    """
    Returns a function that takes gram and prints tok and gram on a line.

    >>> tik(5)(6) 
    5 6 
    """
    def insta(gram):
        print(gram)  # The implementation of this function has been omitted.
        return insta
