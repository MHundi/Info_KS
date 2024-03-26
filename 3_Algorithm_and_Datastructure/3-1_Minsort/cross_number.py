"""
Presentation: Doctest 
Author: Martin Hund
"""
def cross_sum(number):
    """
    Function to calculate the cross sum of a given number.
    
    >>> cross_sum(112)
    5
    >>> cross_sum(0)
    0
    >>> cross_sum(99)
    18
    """
    #convert number with type int in a string
    s_number=str(number)
    
    result = 0
    
    # create digits out of a number
    for digit in s_number:
        result = result + int(digit)
    return result