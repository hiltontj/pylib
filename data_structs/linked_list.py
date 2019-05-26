class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self._head = None
    
    def __iter__(self):
        self._loc = self._head
        return self

    def __next__(self):
        if self._loc is None:
            raise StopIteration
        result = self._loc.data
        self._loc = self._loc.next
        return result
    
    def push(self, val):
        temp = self._head
        self._head = Node(val)
        if temp is not None:
            self._head.next = temp

    def pop(self):
        temp = self._head
        self._head = self._head.next
        return temp.data

    def head(self):
        return self._head.data
