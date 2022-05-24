from binaryTree import Node, MyBST, printTree

if __name__ == "__main__":
    tree = MyBST()

    [node1, node2, node3, node4, node5, node6, node7] = [Node("jeden"), Node(
        "dwa"), Node("trzy"), Node("trzy1"), Node("trz"), Node("dwa1"), Node("dwa2")]

    tree.BSTinsert(node1)
    tree.BSTinsert(node2)
    tree.BSTinsert(node3)
    tree.BSTinsert(node4)
    tree.BSTinsert(node5)
    tree.BSTinsert(node6)
    tree.BSTinsert(node7)

    printTree(tree.root)
