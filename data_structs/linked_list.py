class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def push(val):
        temp = self.head
        self.head = Node(val)
        if temp is not None:
            self.head.next = temp

    def pop():
        temp = self.head
        self.head = self.head.next
        return temp
