# Program to traverse nodes as per level
# Author : DC

class Node:

    def __init__(self,val):
        self.val = val
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

class Queue:

    def __init__(self):
        self.ll = LinkedList()

    def enqueue(self,val):
        node = Node(val)
        if self.ll.head is None:
            self.ll.head = node
            self.ll.tail = node
        else:
            self.ll.tail.next = node
            self.ll.tail = node

    def dequeue(self):
        if self.ll.head is None:
            return
        tempNode = self.ll.head
        if self.ll.head == self.ll.tail:
            self.ll.head = None
            self.ll.tail = None
        else:
            self.ll.head = self.ll.head.next
        return tempNode

    def isEmpty(self):
        return self.ll.head is None

class TreeNode:

    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def levelOrderTraversal(self,rootNode):
        if rootNode is None:
            return
        else:
            customQueue = Queue()
            customQueue.enqueue(rootNode)
            while not (customQueue.isEmpty()):
                root = customQueue.dequeue()
                print(root.val.data)
                if root.val.leftChild is not None:
                    customQueue.enqueue(root.val.leftChild)

                if root.val.rightChild is not None:
                    customQueue.enqueue(root.val.rightChild)

    def searchNode(self,rootNode,val):
        if rootNode is None:
            return "Not found."
        else:
            customQueue = Queue()
            customQueue.enqueue(rootNode)
            while not(customQueue.isEmpty()):
                root = customQueue.dequeue()
                if root.val.data == val:
                    return "Match Found"
                if root.val.leftChild is not None:
                    customQueue.enqueue(root.val.leftChild)
                if root.val.leftChild is not None:
                    customQueue.enqueue(root.val.leftChild)
            return "Not found."


if __name__ == '__main__':
    node = TreeNode("N1")
    node.leftChild = TreeNode("N2")
    node.rightChild = TreeNode("N3")
    node.leftChild.leftChild = TreeNode("N4")
    node.leftChild.rightChild = TreeNode("N5")
    node.rightChild.leftChild = TreeNode("N6")
    node.rightChild.rightChild = TreeNode("N7")
    node.leftChild.leftChild.leftChild = TreeNode("N8")
    node.leftChild.leftChild.rightChild = TreeNode("N9")

    node.levelOrderTraversal(node)

    print(node.searchNode(node,"N10"))

