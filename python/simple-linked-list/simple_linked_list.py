class Node(object):
    def __init__(self, value, _next=None):
        self._value = value
        self._next = _next

    def value(self):
        return self._value

    def next(self):
        return self._next


class LinkedList(object):
    def __init__(self, values=[]):
        self._head = None
        for v in values:
            self._head = Node(v, self._head) 


    def __len__(self):
        count = 0
        for _ in self:
            count += 1
        return count
    
    def __iter__(self):
        pointer = self._head
        while pointer:
            yield pointer.value()
            pointer = pointer.next()

    def head(self):
        if not self._head:
            raise EmptyListException("Empty list.")
        return self._head

    def push(self, value):
        self._head = Node(value, self._head)

    def pop(self):
        node = self._head
        self._head = self.head().next()
        return node.value()

    # is this method kidding me?
    # the test says it should not be reversed...
    def reversed(self):
        return self.__class__((list(self)))


class EmptyListException(Exception):
    pass
