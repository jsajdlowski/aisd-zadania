class Node:
    def __init__(self, k) -> None:
        self.key = k
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert(self, x):
        x.next = self.head
        if self.head != None:
            self.head.prev = x
        self.head = x
        x.prev = None

    def search(self, k):
        x = self.head
        while x != None and x.key != k:
            x = x.next
        return x

    def delete(self, x):
        if x.prev != None:
            x.prev.next = x.next
        else:
            self.head = x.next
        if x.next != None:
            x.next.prev = x.prev

    # def deleteWithGuardian(self, x):
    #     x.prev.next = x.next
    #     x.next.prev = x.prev

    # def listSearch(self, k):
    #     x = self.none.next
    #     while x != None and x.key != k:
    #         x = x.next
    #     return x
