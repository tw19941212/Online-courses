class NoSuchElementError(Exception):
    pass


class Node():
    '''
    helper linked list class
    '''

    def __init__(self, item, next):
        self.item = item
        self.next = next


class LinkedStack():
    '''
    The LinkedStack class represents a last-in-first-out (LIFO) stack of generic items

    Time complexity: O(1) for every operations
    '''

    def __init__(self):
        self.first = None
        self.n = 0  # number of elements on stack

    def isempty(self):
        return self.first == None

    def size(self):
        return self.n

    def push(self, item):
        oldfirst = self.first
        self.first = Node(item, oldfirst)
        self.n += 1

    def pop(self):
        if self.isempty():
            raise NoSuchElementError('Stack underflow')
        item = self.first.item
        self.first = self.first.next
        self.n -= 1
        return item

    def peek(self):
        if self.isempty():
            raise NoSuchElementError('Stack underflow')
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


class ResizingArrayStack():
    '''
    The ResizingArrayStack class represents a last-in-first-out (LIFO) stack of generic items

    Time complexity: 
        O(1) for every operations(amortized)
        O(N) for push and pop(worst)
    '''

    def __init__(self):
        self.a = [0, 0]
        self.n = 0  # number of elements on stack

    def isempty(self):
        return self.n == 0

    def size(self):
        return self.n

    def _resize(self, capacity):
        assert capacity >= self.n
        temp = [0]*capacity
        for i in range(self.n):
            temp[i] = self.a[i]
        self.a = temp

    def push(self, item):
        if self.n == len(self.a):
            self._resize(2*self.n)
        self.a[self.n] = item
        self.n += 1

    def pop(self):
        if self.isempty():
            raise NoSuchElementError('Stack underflow')
        item = self.a[self.n-1]
        self.n -= 1
        if self.n > 0 and self.n == len(self.a)//4:
            self._resize(len(self.a)//2)
        return item

    def peek(self):
        if self.isempty():
            raise NoSuchElementError('Stack underflow')
        return self.a[self.n-1]

    def __iter__(self):
        self._current = self.n-1
        return self

    def __next__(self):
        if self._current >= 0:
            current_item = self.a[self._current]
            self._current -= 1
            return current_item
        else:
            raise StopIteration
