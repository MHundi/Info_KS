"""
Informatik 11.2 
Algorithm and Datastructure
"""

def bubble_sort(a):
    """
    Third Sort Algorithm Bubblesosrt

    
    >>> bubble_sort([35, 14, 65, 19, 44, 8, 23, 19])
    [8, 14, 19, 19, 23, 35, 44, 65]
    >>> bubble_sort([5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5]
    >>> bubble_sort([])
    []
    """
    
    n = len(a)
    for j in range(n-1,0,-1):
        for i in range(0,j):
            if a[i+1]<a[i]:
                a[i], a[i+1] = a[i+1], a[i]
    return a
 

print(bubble_sort([7, 4, 56,23,1]))     