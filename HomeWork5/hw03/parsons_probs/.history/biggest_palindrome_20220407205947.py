def biggest_palindrome(n): 
    """Return the largest even-length palindrome in n.
    >>> biggest_palindrome(3425534) 
    4554 
    >>> biggest_palindrome(126130450234125) 
    21300312 
    """
return big(n, 0)
def big(n, k): """A helper function for biggest_palindrome."""
if n == 0: return 0
choices = [big( _________________ , k) , big( _________________ , _________________ )] if contains(k, ______________________________________________________________________): __________________________________________________________________________________
return max(choices)