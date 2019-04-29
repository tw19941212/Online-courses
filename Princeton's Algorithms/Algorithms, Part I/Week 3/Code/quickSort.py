import numpy as np


def quickSort(a):
    """
    Rearranges the array in ascending order, using the natural order.
    @param a the array to be sorted

    Time complexity: worst O(N^2/2) average O(2NlogN) best O(NlogN)
    Inplace: True
    Stable: False
    Remarks: N log N  probabilistic guaranteefastest in practice
    """
    np.random.shuffle(a)
    _sort(a, 0, len(a)-1)


def _sort(a, lo, hi):
    # quicksort the subarray from a[lo] to a[hi]
    if hi <= lo:
        return
    j = _partition(a, lo, hi)
    _sort(a, lo, j-1)
    _sort(a, j+1, hi)


def _partition(a, lo, hi):
    # partition the subarray a[lo..hi] so that a[lo..j-1] <= a[j] <= a[j+1..hi]
    # and return the index j.
    i, j = lo+1, hi
    v = a[lo]
    while True:
        # find item on lo to swap
        while a[i] < v:
            if i == hi:
                break
            i += 1
        # find item on hi to swap
        while v < a[j]:
            if j == lo:
                break  # redundant since a[lo] acts as sentinel
            j -= 1
        # check if pointers cross
        if i >= j:
            break

        a[i], a[j] = a[j], a[i]

    a[lo], a[j] = a[j], a[lo]
    return j


def quick3waySort(a):
    """
    Rearranges the array in ascending order with 3-way partitioning
    @param a the array to be sorted

    Time complexity: worst O(N^2/2) average O(2NlogN) best O(N)
    Inplace: True
    Stable: False
    Remarks: improves quicksort in presenceof duplicate keys
    """
    np.random.shuffle(a)
    _3waysort(a, 0, len(a)-1)


def _3waysort(a, lo, hi):
    # quicksort the subarray a[lo .. hi] using 3-way partitioning
    if hi <= lo:
        return
    lt, gt = lo, hi
    v = a[lo]
    i = lo+1
    while i <= gt:
        if a[i] < v:
            a[i], a[lt] = a[lt], a[i]
            i, lt = i+1, lt+1
        elif a[i] > v:
            a[i], a[gt] = a[gt], a[i]
            gt -= 1
        else:
            i += 1
    # a[lo..lt-1] < v = a[lt..gt] < a[gt+1..hi].
    _3waysort(a, lo, lt-1)
    _3waysort(a, gt+1, hi)


def quickselect(a, k):
    '''
    Given an array of N items, find a kth smallest item
    @param a the array to be selected
    @param k the kth smallest item

    Time complexity: Quick-select takes linear time on average
    Remarks: Quick-select uses ~ ½N^2 compares in the worst case, but(as with quicksort) the random shuffle provides a probabilistic guarantee
    '''
    np.random.shuffle(a)
    lo, hi = 0, len(a)-1
    while hi > lo:
        j = _partition(a, lo, hi)
        if j < k:
            lo = j+1
        elif j > k:
            hi = j-1
        else:
            return a[k]
    return a[k]
