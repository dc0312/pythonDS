# Program contains all the basic functions related to the circular doubly single linked list
# Author : DC

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class CircularDoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break

    def insert(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            newNode.next = newNode
            newNode.prev = newNode
        else:
            if location == 0:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.head = newNode
                self.tail.next = newNode
            elif location == 1:
                newNode.prev = self.tail
                newNode.next = self.head
                self.head.prev = newNode
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                newNode.next = tempNode.next
                newNode.prev = tempNode
                tempNode.next.prev = newNode
                tempNode.next = newNode

    def traversal(self):
        if self.head is None:
            print("The list is empty while traversal.")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    break

    def delete(self, location):
        if self.head is None:
            print("The list is empty during delete.")
        else:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                if location == 0:
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head
                elif location == 1:
                    # self.head.prev = self.tail.prev
                    # self.tail.prev.prev = self.head
                    # self.tail = self.tail.prev
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
                else:
                    tempNode = self.head
                    index = 0
                    while index < location - 1:
                        tempNode = tempNode.next
                        index += 1
                    tempNode.next = tempNode.next.next
                    tempNode.next.prev = tempNode

class Main:

    def __init__(self):
        pass


if __name__ == '__main__':
    dcll = CircularDoublyLinkedList()
    dcll.insert(2, 0)
    dcll.insert(1, 0)
    dcll.insert(3, 1)
    dcll.insert(5, 1)
    dcll.insert(4, 3)
    print([node.value for node in dcll])
    dcll.traversal()
    dcll.delete(0)
    print([node.value for node in dcll])
    dcll.delete(1)
    print([node.value for node in dcll])
