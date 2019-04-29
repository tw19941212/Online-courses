class NoSuchElementException(Exception):
    pass


class MaxPQ():
    '''
    Generic max priority queue implementation with a binary heap.
    Can be used with a comparator instead of the natural order,
    but the generic Key type must still be Comparable.

    Time complexity: 
        O(logN) for insert operations
        O(logN) for delmax operations
        O(1) for max operations
    '''

    def __init__(self, initCapacity=None, keys=None):
        # Initializes an empty priority queue with the given initial capacity
        if initCapacity:
            self.pq = [0] * (initCapacity+1)  # store items at indices 1 to n
            self.n = 0  # number of items on priority queue
        # Initializes a priority queue from the array of keys
        elif keys:
            self.n = len(keys)
            self.pq = [0]
            for k in keys:
                self.pq.append(k)
            for i in range(self.n//2, 0, -1):
                self._sink(i)

    def isEmpty(self):
        return self.n == 0

    def size(self):
        return self.n

    def max(self):
        if self.isEmpty():
            raise NoSuchElementException('Priority queue underflow')
        return self.pq[1]

    # helper function to double the size of the heap array
    def _resize(self, capacity):
        assert capacity > self.n
        temp = [None] * capacity
        for i in range(self.n):
            temp[i] = self.pq[i]
        self.pq = temp

    def insert(self, key):
        # double size of array if necessary
        if self.n == len(self.pq)-1:
            self._resize(2*len(self.pq))
        # add x, and percolate it up to maintain heap invariant
        self.n += 1
        self.pq[self.n] = key
        self._swim(self.n)

    def delMax(self):
        '''
        Removes and returns a largest key on this priority queue.

        @return a largest key on this priority queue
        @throws NoSuchElementException if this priority queue is empty
        '''
        if self.isEmpty():
            raise NoSuchElementException('Priority queue underflow')
        m = self.pq[1]
        self.pq[1], self.pq[self.n] = self.pq[self.n], self.pq[1]
        self.n -= 1
        self._sink(1)
        # to avoid loitering and help with garbage collection
        self.pq[self.n+1] = None
        if self.n > 0 and self.n == (len(self.pq)-1)//4:
            self._resize(len(self.pq)//2)
        return m

    '''***************************************************************************
    * Helper functions to restore the heap invariant.
    ***************************************************************************'''

    def _swim(self, k):
        while k > 1 and self.pq[k//2] < self.pq[k]:
            self.pq[k], self.pq[k//2] = self.pq[k//2], self.pq[k]
            k //= 2

    def _sink(self, k):
        while 2*k <= self.n:
            j = 2 * k
            if j < self.n and self.pq[j] < self.pq[j+1]:
                j += 1
            if self.pq[k] >= self.pq[j]:
                break
            self.pq[k], self.pq[j] = self.pq[j], self.pq[k]
            k = j

    '''***************************************************************************
    * Helper functions for compares and swaps.
    ***************************************************************************'''

    # is pq[1..N] a max heap?
    def isMaxHeap(self):
        return self._isMaxHeap(1)

    # is subtree of pq[1..n] rooted at k a max heap?
    def _isMaxHeap(self, k):
        if k > self.n:
            return True
        left, right = 2*k, 2*k+1
        if left <= self.n and self.pq[k] < self.pq[left]:
            return False
        if right <= self.n and self.pq[k] < self.pq[right]:
            return False
        return self._isMaxHeap(left) and self._isMaxHeap(right)

    '''************************************************************************
    * Iterator.
    ************************************************************************'''

    def __iter__(self):
        # create a new pq
        self.copy = MaxPQ(initCapacity=self.size())
        # add all items to copy of heap
        # takes linear time since already in heap order so no keys move
        for i in range(1, self.n+1):
            self.copy.insert(self.pq[i])
        return self.copy

    def __next__(self):
        if not self.isEmpty():
            return self.delMax()
        else:
            raise StopIteration
