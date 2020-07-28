class Node(object):
    def __init__(self, value, succeeding=None, previous=None):
        self._value = value
        self._prev = previous
        self._next = succeeding


class LinkedList(object):
    def __init__(self):
        self._head = None
        self._end = None
    
    def push(self, value):
        node = Node(value, None, self._end)
        if self._end is not None:
            self._end._next = node
        if self._head is None:
            self._head = node
        self._end = node
    
    def pop(self):
        node = self._end
        self._end = self._end._prev
        if self._end is not None:
            self._end._next = None
        else:
            self._head = None
        return node._value
    
    def unshift(self, value):
        node = Node(value, self._head, None)
        if self._head is not None:
            self._head._prev = node
        if self._end is None:
            self._end = node
        self._head = node

    def shift(self):
        node = self._head
        self._head = self._head._next
        if self._head is not None:
            self._head._prev = None
        else:
            self._end = None
        return node._value
    
    def __iter__(self):
        pointer = self._head
        while pointer:
            yield pointer._value
            pointer = pointer._next
    
    def __len__(self):
        counter = 0
        for _ in self:
            counter += 1
        return counter