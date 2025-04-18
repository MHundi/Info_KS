"""
Informatik 11.2 
Algorithm and Datastructure
"""
import time

def python_sort(a):
    """
    Sort Algorithm von Python

    
    >>> python_sort([35, 14, 65, 19, 44, 8, 23, 19])
    [8, 14, 19, 19, 23, 35, 44, 65]
    >>> python_sort([5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5]
    >>> python_sort([])
    []
    """
    
def python_sort(a):
    erg= sorted(a)
    return erg
                
    
def python_sort_timing():
    """
    Run Pythonsort with increasing size .
    """
                    
    # Iterate over 500, 1000, 1500, ... 10000
    # create array from k to zero
    for n in range(0, 10000000, 50000):
        a=[k for k in range(n, 0, -1)]
        start_time = time.monotonic()
        python_sort(a)
        end_time = time.monotonic()
        
        # Duration in milisecondes. Mention, that time.monotoic returns a flosting point number that
        # is in seconds
        duration = int(round((end_time - start_time)*1000))
        
        # print sizte an the time with tab seperated
        print("%d\t %d" % (n, duration))
        
if __name__=="__main__":
    python_sort_timing()
 
""" 
in Terminal   
> python minsort.py > min_sort.times.tsv
> cat min_sort.times.tsv 
> ggnuplot -e 'plot "min_sort.times.tsv" with lines ; pause -1;'
> gnuplot -e 'set terminal pdf; plot "min_sort.times.tsv" with lines ; pause -1;'

"""