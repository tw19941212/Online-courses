def mergeSort(a):
    """
    Rearranges the array in ascending order, using the natural order.
    @param a the array to be sorted

    Time complexity: worst O(NlogN) average O(NlogN) best O(NlogN)
    Inplace: False
    Stable: True
    Remarks: N log N  guarantee, stable
    """
    aux = [0 for _ in range(len(a))]
    _sort(a, aux, 0, len(a)-1)


def _sort(a, aux, lo, hi):
    # mergesort a[lo..hi] using auxiliary array aux[lo..hi]
    if hi <= lo:
        return
    mid = lo + (hi-lo)//2
    _sort(a, aux, lo, mid)
    _sort(a, aux, mid+1, hi)
    _merge(a, aux, lo, mid, hi)


def _merge(a, aux, lo, mid, hi):
    # stably merge a[lo .. mid] with a[mid+1 ..hi] using aux[lo .. hi]

    # copy to aux[]
    for k in range(lo, hi+1):
        aux[k] = a[k]

    # merge back to a[]
    i = lo
    j = mid+1
    for k in range(lo, hi+1):
        if i > mid:
            a[k] = a[j]
            j += 1
        elif j > hi:
            a[k] = aux[i]
            i += 1
        elif aux[j] < aux[i]:
            a[k] = aux[j]
            j += 1
        else:
            a[k] = aux[i]
            i += 1


def mergeSortBU(a):
    """
    Rearranges the array in ascending order, using the natural order.
    @param a the array to be sorted

    Time complexity: worst O(NlogN) average O(NlogN) best O(NlogN)
    Inplace: False
    Stable: True
    Remarks: Simple and non-recursive version of mergesort.
    but about 10% slower than recursive,top-down mergesort on typical systems
    """
    n = len(a)
    aux = [0 for _ in range(len(a))]
    sz = 1
    while sz < n:
        for lo in range(0, n-sz, 2*sz):
            mid = lo+sz-1
            hi = min(lo+2*sz-1, n-1)
            _merge(a, aux, lo, mid, hi)
        sz *= 2
