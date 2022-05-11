from typing import Any

def hashStringToIntA(string: str, tableSize: int,  i: int = 0, acc: int = 0) -> int:
    if len(string) == 1:
        return (ord(string) + acc + i) % tableSize

    return hashStringToIntA(string[1:], tableSize, i, ord(string[0]) % tableSize)


def hashStringToIntB(string: str, tableSize: int, i: int = 0, acc: int = 0) -> int:
    if len(string) == 1:
        return (ord(string) + acc + i**2) % tableSize
    return hashStringToIntB(string[1:], tableSize, i, (ord(string[0]) + acc) % tableSize)


def hashStringToIntC(string: str, tableSize: int, i: int = 0, acc: int = 0) -> int:
    if len(string) == 1:
        return (ord(string) % tableSize + i * (1 + (ord(string) % (tableSize - 2))) + acc) % tableSize

    return hashStringToIntC(string[1:], tableSize, i, ord(string[0]) % tableSize + i * (1 + (ord(string[0]) % (tableSize - 2)) + acc))


class HashTable:
    def __init__(self, initialSize: int) -> None:
        self.table = [None for _ in range(initialSize)]
        self.numItems = 0
        self.loadFactor = self.numItems / len(self.table)

    def resize(self) -> None:
        newTable = HashTable(len(self.table) * 2)

        for item in self.table:
            newTable.setItem(item[1], item)

        self.table = newTable.table

    def setItem(self, key: str, value) -> int:
        self.numItems += 1
        self.loadFactor = self.numItems / len(self.table)

        if self.loadFactor > 1:
            self.resize()

        i = 0
        counter = 0
        while True:
            index = hashStringToIntA(key, len(self.table), i)

            if self.table[index] == None:
                self.table[index] = value
                break

            i += 1
            counter += 1

        return counter

    def getItem(self, key) -> Any:
        i = 0
        while True:
            index = hashStringToIntA(key, len(self.table), i)

            if self.table[index] == None:
                return None
            elif self.table[index][1] == key:
                return self.table[index]

            i += 1
