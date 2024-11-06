""" 
Author: bin ich
Info Kurs Klasse 11
"""
import time
def min_sort(a):
    """
    My first algorithm in Minsort. 
    
    Doctest:
    >>> min_sort([35,14,65,19,44,8,23,19])
    [8,14,19,19,23,35,44,65]
    >>> min_sort([6,5,4,3,2,1])
    [1,2,3,4,5,6]
    >>> min_sort[3]
    [3]
    >>> min_sort([])
    []
    """
    
    n = len(a)
    
    for i in range(n-1):
        act_min=a[i]
        act_min_index=i
        
        for j in range(i+1, n):
            if a[j]<act_min:
                act_min=a[j]
                act_min_index= j
        # change elements in list        
        if act_min_index < i:
            a[i],a[act_min_index] = a[act_min_index]  ,a[i]
    
    return a

def min_sort_timing():
    """
    Iterate over 500, 1000,... 100000 entries
    Create array from k to zero
    """
    for n in range(500, 10001 ,500):
        a=[k for k in range(n,0,-1)]
        
        start_time= time.monotonic()
        min_sort(a)
        end_time = time.monotonic()
        
        # Duration in millisenconds, remember that time.monotonic is a floating point number an time.monotonic
        # returns seconds
        
        duration = int(round((end_time-start_time)*1000))
        
        # print size an duration tabseperated
        print("%d \t %d " %(n, duration))
        
if __name__ == "__main__":
    min_sort_timing()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    