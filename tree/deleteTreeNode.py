# Program to delete the given node
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
            print("Queue is empty.")
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

    def findDeepestNode(sel,rootNode):
        if rootNode is None:
            print("Tree is empty")
            return
        else:
            customQueue = Queue()
            customQueue.enqueue(rootNode)
            while not (customQueue.isEmpty()):
                root = customQueue.dequeue()
                dNode = root.val
                if root.val.leftChild is not None:
                    customQueue.enqueue(root.val.leftChild)
                if root.val.rightChild is not None:
                    customQueue.enqueue(root.val.rightChild)
            return dNode

    def deleteDeepestNode(self,rootNode):
        dNode = self.findDeepestNode(rootNode)
        if rootNode is None:
            return
        else:
            customQueue = Queue()
            customQueue.enqueue(rootNode)
            while not(customQueue.isEmpty()):
                root = customQueue.dequeue()
                if root.val.rightChild:
                    if root.val.rightChild is dNode:
                        root.val.rightChild = None
                        return
                    else:
                        customQueue.enqueue(root.val.rightChild)
                if root.val.leftChild:
                    if root.val.leftChild is dNode:
                        root.val.leftChild = None
                        return
                    else:
                        customQueue.enqueue(root.val.leftChild)

    def deleteNode(self,rootNode,node):
        if rootNode is None:
            return
        else:
            customQueue = Queue()
            customQueue.enqueue(rootNode)
            while not customQueue.isEmpty():
                root = customQueue.dequeue()
                if root.val.data == node:
                    dNode = self.findDeepestNode(rootNode)
                    root.val.data = dNode.data
                    self.deleteDeepestNode(rootNode)
                    return
                if root.val.leftChild is not None:
                    customQueue.enqueue(root.val.leftChild)
                if root.val.rightChild is not None:
                    customQueue.enqueue(root.val.rightChild)

    def levelOrderTraversal(self,rootNode):
        if rootNode is None:
            return
        else:
            customQueue = Queue()
            customQueue.enqueue(rootNode)
            while not customQueue.isEmpty():
                root = customQueue.dequeue()
                print(root.val.data)
                if root.val.leftChild is not None:
                    customQueue.enqueue(root.val.leftChild)
                if root.val.rightChild is not None:
                    customQueue.enqueue(root.val.rightChild)

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

    print(node.findDeepestNode(node).data)
    node.deleteDeepestNode(node)
    print(node.findDeepestNode(node).data)
    node.deleteNode(node,"N4")
    node.levelOrderTraversal(node)
