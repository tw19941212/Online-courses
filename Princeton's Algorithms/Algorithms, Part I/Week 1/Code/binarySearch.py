def binarySearch(key, a):
    """
    Binary searching for an integer in a sorted array of integers

    Time complexity: O(log(N))
    """
    lo = 0
    hi = len(a) - 1
    while lo <= hi:
        # Key is in a[lo..hi] or not present.
        mid = lo + (hi - lo) / 2
        # One 3-way compare:
        if   key < a[mid]: hi = mid - 1
        elif key > a[mid]: lo = mid + 1
        else: return mid
    return -1