import numpy as np


def shuffle(a):
    """
    Rearranges an array of objects in uniformly random order
    (under the assumption that {@code np.random.random()} generates independent
    and uniformly distributed numbers between 0 and 1).
    @param a the array to be shuffled

    Time complexity: O(N)
    """
    n = len(a)
    for i in range(n):
        # choose index uniformly in [0, i]
        r = int(np.random.random()*(i+1))
        a[r], a[i] = a[i], a[r]


def shuffleAlternate(a):
    """
    Rearranges an array of objects in uniformly random order
    (under the assumption that {@code np.random.random()} generates independent
    and uniformly distributed numbers between 0 and 1).
    @param a the array to be shuffled

    Time complexity: O(N)
    """
    n = len(a)
    for i in range(n):
        # choose index uniformly in [i, n-1]
        r = i + int(np.random.random()*(n-i))
        a[r], a[i] = a[i], a[r]
