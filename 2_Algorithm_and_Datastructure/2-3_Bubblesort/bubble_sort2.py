# Author: Martin
# Bubble Sort


def bubble_sort(a):
    """
    Bubble Sort alias Minsort.
    Sort a given array using the bubble_sort algorithm
    >>> bubble_sort([31, 23,4, 55, 1, 12])
    [1, 4, 12, 23,31, 55]
    >>> bubble_sort([6, 4, 3, 2, 1, 0])
    [0, 1, 2, 3, 4, 5, 6]
    >>> bubble_sort([])
    []
    """
    print(a)
    n = len(a)
    for j in range(n-1,0,-1):
        for i in range(0, j):
            if a[i+1]<a[i]:
                a[i], a[i+1] = a[i+1], a[i]
        print(a)
    return a

def test():
    b = [5, 4, 3, 2, 1, 0]
    bubble_sort(b)
    
test()
    
    

    
        
            
    