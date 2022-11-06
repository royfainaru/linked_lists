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

    @prev.setter
    def prev(self, other):
        if self.prev is other:
            return
        self._prev = other
        if not other:
            return
        other.next = self

