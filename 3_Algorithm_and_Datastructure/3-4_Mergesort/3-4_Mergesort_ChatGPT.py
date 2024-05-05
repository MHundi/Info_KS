def merge_sort(arr):
    width = 1
    n = len(arr)
    while width < n:
        l = 0
        while l < n:
            r = min(l + (width * 2 - 1), n - 1)
            m = min(l + width - 1, n - 1)
            merge(arr, l, m, r)
            l += width * 2
        width *= 2

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    left = arr[l:l + n1]
    right = arr[m + 1:m + 1 + n2]

    i = j = 0
    k = l

    while i < n1 and j < n2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = left[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = right[j]
        j += 1
        k += 1

def print_array(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

# Beispiel für die Verwendung des Mergesort-Algorithmus
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    print("Gegebenes Array:")
    print_array(arr)

    merge_sort(arr)
    print("Sortiertes Array:")
    print_array(arr)