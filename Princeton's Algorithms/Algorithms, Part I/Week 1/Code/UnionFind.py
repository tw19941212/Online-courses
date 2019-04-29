class QuickFindUF():
    '''
    Initializes an empty union–find data structure with n sites 0 through n-1.
    Each site is initially in its own component.

    Parameters:
        N - the number of sites

    Time complexity: O(MN) where M is the number of operations
        initialize - N
        union - N
        connected - 1
    '''

    def __init__(self, N):
        self._count = N
        self.parent = list(range(N))

    def count(self):
        return self._count

    def find(self, p):
        self._validate(p)
        return self.parent[p]

    def _validate(self, p):
        N = len(self.parent)
        if p < 0 or p >= N:
            raise IndexError(f'Index {p} is not between 0 and {N-1}')

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        p_par = self.parent[p]
        q_par = self.parent[q]
        if p_par == q_par:
            return
        for i, par in enumerate(self.parent):
            if par == p_par:
                self.parent[i] = q_par
        self._count -= 1


class QuickUnionUF():
    '''
    Initializes an empty union–find data structure with n sites 0 through n-1.
    Each site is initially in its own component.

    Parameters:
        N - the number of sites

    Time complexity: O(MN) where M is the number of operations
        initialize - N
        union - N
        connected - N
    '''

    def __init__(self, N):
        self._count = N
        self.parent = list(range(N))

    def count(self):
        return self._count

    def find(self, p):
        self._validate(p)
        while p != self.parent[p]:
            p = self.parent[p]
        return p

    def _validate(self, p):
        N = len(self.parent)
        if p < 0 or p >= N:
            raise IndexError(f'Index {p} is not between 0 and {N-1}')

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        p_root = self.find(p)
        q_root = self.find(q)
        if p_root == q_root:
            return
        self.parent[p_root] = q_root
        self._count -= 1


class WeightedQuickUnionUF():
    '''
    Initializes an empty union–find data structure with n sites 0 through n-1.
    Each site is initially in its own component.

    Parameters:
        N - the number of sites

    Time complexity: O(N + M*log(N)) where M is the number of operations
        initialize - N
        union - log(N)
        connected - log(N)
    '''

    def __init__(self, N):
        self._count = N
        self.parent = list(range(N))
        self.size = [1] * N

    def count(self):
        return self._count

    def find(self, p):
        self._validate(p)
        while p != self.parent[p]:
            # one extra line more fast O(N + M*(log*N))
            # self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p

    def _validate(self, p):
        N = len(self.parent)
        if p < 0 or p >= N:
            raise IndexError(f'Index {p} is not between 0 and {N-1}')

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        p_root = self.find(p)
        q_root = self.find(q)
        if p_root == q_root:
            return
        if self.size[p_root] < self.size[q_root]:
            self.parent[p_root] = q_root
            self.size[q_root] += self.size[p_root]
        else:
            self.parent[q_root] = p_root
            self.size[p_root] += self.size[q_root]
        self._count -= 1
