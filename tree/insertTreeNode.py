# Program to insert node in TreeNode
# Author : DC
class Node:

    def __init__(self, val):
        self.val = val
        self.next = None

class  LinkedList:

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
            return "Queue is empty."
        elif self.ll.head == self.ll.tail:
            temp = self.ll.head
            self.ll.head = None
            self.ll.tail = None
            return temp
        else:
            temp = self.ll.head
            self.ll.head = self.ll.head.next
            return temp

    def isEmpty(self):
        return self.ll.head is None


class TreeNode:

    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def insert(self,rootNode,val):
        if rootNode is None:
            rootNode = TreeNode(val)
        else:
            customQueue = Queue()
            customQueue.enqueue(rootNode)
            while not (customQueue.isEmpty()):
                root = customQueue.dequeue()
                if root.val.leftChild is None:
                    root.val.leftChild = TreeNode(val)
                    return
                else:
                    customQueue.enqueue(root.val.leftChild)
                if root.val.rightChild is None:
                    root.val.rightChild = TreeNode(val)
                    return
                else:
                    customQueue.enqueue(root.val.rightChild)

    def levelOrderTraversal(self,rootNode):
        if rootNode is None:
            return "Empty TreeNode"
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

if __name__ == '__main__':
    node = TreeNode("Drinks")
    node.insert(node,"Hot")
    node.insert(node,"Cold")
    node.insert(node,"Tea")
    node.levelOrderTraversal(node)

