class UnorderedArrayMaxPQ():
    '''
    Priority queue implementation with an unsorted array

    Time complexity: 
        O(1) for insert operations
        O(N) for delmax operations
        O(N) for max operations

    Limitations
        no array resizing 
        does not check for overflow or underflow
    '''

    def __init__(self, capacity):
        # set initial size of heap to hold size elements
        self.pq = [0] * capacity  # elements
        self.n = 0  # number of elements

    def isEmpty(self):
        return self.n == 0

    def size(self):
        return self.n

    def insert(self, key):
        self.pq[self.n] = key
        self.n += 1

    def delMax(self):
        m = 0
        for i in range(self.n):
            if m < i:
                m = i
        self.pq[m], self.pq[self.n -
                            1] = self.pq[self.n-1], self.pq[m]
        self.n -= 1
        return self.pq[self.n]


class OrderedArrayMaxPQ():
    '''
    Priority queue implementation with an ordered array

    Time complexity: 
        O(N) for insert operations
        O(1) for delmax operations
        O(1) for max operations

    Limitations
        no array resizing 
        does not check for overflow or underflow
    '''

    def __init__(self, capacity):
        # set initial size of heap to hold size elements
        self.pq = [0] * capacity  # elements
        self.n = 0  # number of elements

    def isEmpty(self):
        return self.n == 0

    def size(self):
        return self.n

    def delMax(self):
        self.n -= 1
        return self.pq[self.n]

    def insert(self, key):
        i = self.n - 1
        while i >= 0 and key < self.pq[i]:
            self.pq[i+1] = self.pq[i]
            i -= 1
        self.pq[i+1] = key
        self.n += 1
