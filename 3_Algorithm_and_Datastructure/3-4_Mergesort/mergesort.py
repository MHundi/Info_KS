"""
Informatik 11.2 
Algorithm and Datastructure
"""
import time

def merge_sort(a):
    """
    Sort Algorithm MergeSort

    
    >>> merge_sort([4,17,19 32, 8, 19, 44, 66])
    [4, 8, 17, 19, 19, 32, 44, 66]
    >>> min_sort([5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5]
    >>> min_sort([])
    []
    """
    
    n = len(a)
    
    for i in range(n-1):
        act_min = a[i]
        act_min_index=i
        
        for j in range(i+1, n):
            if a[j]<act_min:
                act_min = a[j]
                act_min_index = j
                
        if act_min_index > i:
            a[i], a[act_min_index]=a[act_min_index], a[i]
            
    return a
                
    
def merge_sort_timing():
    """
    Run MergeSort with increasing size .
    """
                    
    # Iterate over 500, 1000, 1500, ... 10000
    # create array from k to zero
    for n in range(500, 20001, 500):
        a=[k for k in range(n, 0, -1)]
        start_time = time.monotonic()
        merge_sort(a)
        end_time = time.monotonic()
        
        # Duration in milisecondes. Mention, that time.monotoic returns a flosting point number that
        # is in seconds
        duration = int(round((end_time - start_time)*1000))
        
        # print sizte an the time with tab seperated
        print("%d\t %d" % (n, duration))
        
if __name__=="__main__":
    merge_sort_timing()
 
""" 
in Terminal   
> python minsort.py > min_sort.times.tsv
> cat min_sort.times.tsv 
> ggnuplot -e 'plot "min_sort.times.tsv" with lines ; pause -1;'
> gnuplot -e 'set terminal pdf; plot "min_sort.times.tsv" with lines ; pause -1;'

"""