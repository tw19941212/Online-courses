class NoSuchElementError(Exception):
    pass


class Node():
    '''
    helper linked list class
    '''

    def __init__(self, item, next):
        self.item = item
        self.next = next


class LinkedQueue():
    '''
    The LinkedQueue class represents a first-in-first-out (FIFO) queue of generic items

    Time complexity: O(1) for every operations
    '''

    def __init__(self):
        self.n = 0  # number of elements on queue
        self.first = None  # beginning of queue
        self.last = None  # end of queue

    def isempty(self):
        return self.first == None

    def size(self):
        return self.n

    def enqueue(self, item):
        oldlast = self.last
        self.last = Node(item, None)
        if self.isempty():
            self.first = self.last
        else:
            oldlast.next = self.last
        self.n += 1

    def dequeue(self):
        if self.isempty():
            raise NoSuchElementError("Queue underflow")
        current_item = self.first.item
        self.first = self.first.next
        self.n -= 1
        if self.isempty():
            self.last = None  # to avoid loitering
        return current_item

    def peek(self):
        if self.isempty():
            raise NoSuchElementError("Queue underflow")
        return self.first.item

    def __iter__(self):
        self._current = self.first
        return self

    def __next__(self):
        if self._current != None:
            current_item = self._current.item
            self._current = self._current.next
            return current_item
        else:
            raise StopIteration


class ResizingArrayQueue():
    '''
    The ResizingArrayQueue class represents a first-in-first-out (FIFO) queue of generic items

    Time complexity: 
        O(1) for every operations(amortized)
        O(N) for enqueue and dequeue(worst)
    '''

    def __init__(self):
        self.q = [0, 0]
        self.n = 0  # number of elements on stack
        self.first = 0  # index of first element of queue
        self.last = 0  # index of next available slot

    def isempty(self):
        return self.n == 0

    def size(self):
        return self.n

    def _resize(self, capacity):
        assert capacity >= self.n
        temp = [0]*capacity
        for i in range(self.n):
            temp[i] = self.q[(i+self.first) % len(self.q)]
        self.q = temp
        self.first = 0
        self.last = self.n

    def enqueue(self, item):
        if self.n == len(self.q):
            self._resize(2*self.n)
        self.q[self.last] = item
        self.n += 1
        self.last += 1
        if self.last == len(self.q):
            self.last = 0  # wrap-around

    def dequeue(self):
        if self.isempty():
            raise NoSuchElementError('Stack underflow')
        item = self.q[self.first]
        self.n -= 1
        self.first += 1
        if self.first == len(self.q):
            self.first = 0  # wrap-around
        if self.n > 0 and self.n == len(self.q)//4:
            self._resize(len(self.q)//2)  # shrink size of array if necessary
        return item

    def peek(self):
        if self.isempty():
            raise NoSuchElementError('Stack underflow')
        return self.q[self.first]

    def __iter__(self):
        self._current = 0
        return self

    def __next__(self):
        if self._current < self.n:
            current_item = self.q[(self.first+self._current) % len(self.q)]
            self._current += 1
            return current_item
        else:
            raise StopIteration
