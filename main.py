class Node:
    def __init__(self, value):
        self.value = value
        self._next = None
        self._prev = None

    @property
    def next(self):
        return self._next

    @property
    def prev(self):
        return self._prev

    @next.setter
    def next(self, other):
        if self.next is other:
            return
        self._next = other
        if not other:
            return
        other.prev = self
    # Makes sure next and prev relates symmetrically

    @prev.setter
    def prev(self, other):
        if self.prev is other:
            return
        self._prev = other
        if not other:
            return
        other.next = self
    # Makes sure next and prev relates symmetrically


class LinkedList:
    def __init__(self):
        self._first = None
        self._last = None
        self._len = 0

    @property
    def first(self):
        return self._first

    @property
    def last(self):
        return self._last

    @first.setter
    def first(self, node):
        self._first = node
        node.prev = None

    @last.setter
    def last(self, node):
        self._last = node
        node.next = None

    def __len__(self):
        return self._len

    def __bool__(self):
        return bool(len(self))

    def __iter__(self):
        return LLIterator(self)

    def _get_node(self, i):
        if i < len(self) / 2:
            n0 = self.first
            succ = lambda node: node.next
            steps = i
        else:
            n0 = self.last
            succ = lambda node: node.prev
            steps = len(self) - i
        n = n0
        for _ in range(steps):
            n = succ(n)
        return n

    def __getitem__(self, item):
        return self._get_node(item).value

    def append(self, value):
        n = Node(value)
        n.prev = self.last
        self.last = n
        if not self:
            self.first = n
        self._len += 1

    def pop(self, i):
        if not i:
            res = self[0]
            self.first = self.first.next
            self._len -= 1
            return res
        prev_node = self._get_node(i - 1)
        res = prev_node.next.value
        prev_node.next = prev_node.next.next
        self._len -= 1
        return res

    def concat(self, other):
        if not other:
            return
        if not self:
            self.first = other.first
            self.last = other.last
            self._len = len(other)
            return
        self.last.next = other.first
        self.last = other.last
        self._len += len(other)


class LLIterator:
    def __init__(self, l):
        self.n = l[0]

    def __iter__(self):
        return self

    def __next__(self):
        if not self.n:
            raise StopIteration
        value = self.n.value
        self.n = self.n.next
        return value
