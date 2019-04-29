def shellSort(a):
    """
    methods for sorting an array using Shellsort with Knuth's increment sequence (1, 4, 13, 40, ...).
    Rearranges the array in ascending order, using the natural order.
    @param a the array to be sorted

    Time complexity: worst ? average ? best O(N)
    Inplace: True
    Stable: False
    Remarks: tight code, subquadratic
    """
    n = len(a)
    # 3x+1 increment sequence:  1, 4, 13, 40, 121, 364, 1093, ...
    h = 1
    while h < n//3:
        h = 3*h+1
    while h >= 1:
        # h-sort the array
        for i in range(h, n):
            for j in range(i, h-1, -h):
                if a[j] < a[j-h]:
                    a[j], a[j-h] = a[j-h], a[j]
        h //= 3
