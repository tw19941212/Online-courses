def selectionSort(a):
    """
    methods for sorting an array using selection sort.
    Rearranges the array in ascending order, using the natural order.
    @param a the array to be sorted
    
    Time complexity: worst O(N^2/2) average O(N^2/2) best O(N^2/2)
    Inplace: True
    Stable: False
    Remarks: N exchanges
    """
    n = len(a)
    for i in range(n):
        minimal = i
        for j in range(i+1, n):
            if a[j] < a[minimal]:
                minimal = j
        a[minimal], a[i] = a[i], a[minimal]
