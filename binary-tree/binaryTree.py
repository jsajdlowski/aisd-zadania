class Node:
    def __init__(self, x):
        self.key = x
        self.left = None
        self.right = None
        self.parent = None


class MyBST:
    def __init__(self):
        self.root = None

    def BSTsearch(self, key):
        x = self.root
        while x != None and x.key != key:
            if key < x.key:
                x = x.left
            else:
                x = x.right
        return x

    def BSTinsert(self, z):
        x = self.root
        y = None
        while x != None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right

        z.parent = y
        if y == None:
            self.root = z
        else:
            if z.key < y.key:
                y.left = z
            else:
                y.right = z

    def bstMinimum(self, x):
        while x.left != None:
            x = x.left
            return x

    def bstDelete(self, z):
        if z.left == None and z.right == None:
            if z == self.root:
                self.root = None
            else:
                if z == z.parent.left:
                    z.parent.left = None
                else:
                    z.parent.right = None
        elif z.left != None and z.right != None:
            y = self.bstMinimum(z.right)
            z.key = y.key
            self.bstDelete(y)


def printTree(root, level=0):
    if root != None:
        printTree(root.left, level + 1)
        print(' ' * 4 * level + '-> ' + root.key)
        printTree(root.right, level + 1)
