class Node:
    def __init__(self, x):
        self.key = x
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None

    def listInsert(self, x):
        x.next = self.head
        if self.head != None:
            self.head.prev = x
        self.head = x
        x.prev = None

    def listSearch(self, k):
        x = self.head
        while x != None and x.key != k:
            x = x.next
        return x

    def listDelete(self, x):
        if x.prev != None:
            x.prev.next = x.next
        else:
            self.head = x.next
        if x.next != None:
            x.next.prev = x.prev
