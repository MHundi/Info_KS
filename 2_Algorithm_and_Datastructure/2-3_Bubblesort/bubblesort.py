"""
Informatik 11.2 
Algorithm and Datastructure
"""
import time

def bubble_sort(a):
	"""
	Third Sort Algorithm Bubblesosrt

	
	>>> bubble_sort([35, 14, 65, 19, 44, 8, 23, 19])
	[8, 14, 19, 19, 23, 35, 44, 65]
	>>> bubble_sort([5, 4, 3, 2, 1])
	[1, 2, 3, 4, 5]
	>>> min_sort([])
	[]
	"""
	
	n = len(a)
	for j in range(n-1,0,-1):
		for i in range(0,j):
			if a[i+1]<a[i]:
				a[i], a[i+1] = a[i+1], a[i]
	return a
	
def bubble_sort_timing():
	"""
	Run Bubble Sort with increasing size .
	"""
					
	# Iterate over 500, 1000, 1500, ... 10000
	# create array from k to zero
	for n in range(500, 10001, 500):
		a=[k for k in range(n, 0, -1)]
		start_time = time.monotonic()
		bubble_sort(a)
		end_time = time.monotonic()
		
		# Duration in milisecondes. Mention, that time.monotoic returns a flosting point number that
		# is in seconds
		duration = int(round((end_time - start_time)*1000))
		
		# print sizte an the time with tab seperated
		print("%d\t %d" % (n, duration))
		
if __name__=="__main__":
	bubble_sort_timing()
 
""" 
in Terminal   
> python bubblesort.py > bub_sort_times.tsv
> cat bub_sort_times.tsv 
> gnuplot -e 'plot "bub_sort_times.tsv" with lines ; pause -1;'
> gnuplot -e 'set terminal pdf; plot "bub_sort_times.tsv" with lines ; pause -1;'

"""