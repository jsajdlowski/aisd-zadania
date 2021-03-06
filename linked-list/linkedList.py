import copy


class Node:
    def __init__(self, data: str | None) -> None:
        self.data = data
        self.next: None | Node = None
        self.prev: None | Node = None


class LinkedList:
    def __init__(self, data=None) -> None:
        if data == None:
            self.head: None | Node = None
        self.head = Node(data)

        self.none = Node(None)
        self.none.next = self.head

    def prepend(self, node: Node) -> None:
        node.next = self.head

        if self.head != None:
            self.head.prev = node

        self.head = node
        node.prev = self.none
        self.none.next = node

    def listPrint(self) -> None:
        temp = []

        current = self.none
        while current.next != None:
            current = current.next
            temp.append(current.data)

        print(temp)

    def search(self, data: str | None) -> Node | None:
        node = self.none.next

        while node != None and node.data != data:
            node = node.next

        return node

    def listDelete(self, node: Node) -> None:
        temp = self.search(node.data)
        if temp == None:
            return

        temp.prev.next = temp.next
        temp.next.prev = temp.prev

    def uniques(self) -> list[str]:
        result = []

        current = self.none
        while current.next != None:
            current = current.next
            if current.next not in result:
                result.append(current.data)

        return result


def merge(list1: LinkedList, list2: LinkedList) -> LinkedList | None:
    if list1.head == None and list2.head == None:
        return None
    if list1.head == None:
        return list2
    if list2.head == None:
        return list1

    result = copy.deepcopy(list1)

    current = result.none
    while current.next != None:
        current = current.next
    current.next = list2.head

    list1.head = None
    list1.none.next = None
    list2.head = None
    list2.none.next = None

    return result
