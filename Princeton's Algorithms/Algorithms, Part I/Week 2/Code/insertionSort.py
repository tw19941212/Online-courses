def insertionSort(a):
    """
    methods for sorting an array using insertion sort.
    Rearranges the array in ascending order, using the natural order.
    @param a the array to be sorted
    
    Time complexity: worst O(N^2/2) average O(N^2/4) best O(N)
    Inplace: True
    Stable: True
    Remarks: use for small N or partially ordered
    """
    n = len(a)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]
