# Program contains all the basic functions related to the doubly single linked list
# Author : DC

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def insert(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
            elif location == 1:
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                newNode.next = tempNode.next
                tempNode.next.prev = newNode
                tempNode.next = newNode
                newNode.prev = tempNode

    def traversal(self):
        if self.head is None:
            print("The list is empty while traversal.")
            return
        node = self.head
        while node:
            print(node.value)
            node = node.next

    def revTraversal(self):
        if self.head is None:
            print("The list is empty while reverse traversal.")
            return
        node = self.tail
        while node:
            print(node.value)
            node = node.prev

    def search(self, value):
        if self.head is None:
            print("The list is empty while searching.")
            return
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == value:
                    print("Value found")
                    return
                tempNode = tempNode.next
            print("Value not found.")

    def delete(self, location):
        if self.head is None:
            print("The list is empty while deleting.")
            return
        else:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                if location == 0:
                    self.head = self.head.next
                    self.head.prev = None
                elif location == 1:
                    self.tail = self.tail.prev
                    self.tail.next = None
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
    dll = DoublyLinkedList()
    dll.insert(1, 0)
    dll.insert(2, 0)
    dll.insert(3, 0)
    dll.insert(4, 1)
    dll.insert(6, 1)
    dll.insert(5, 4)
    print([node.value for node in dll])
    dll.traversal()
    print("============")
    dll.revTraversal()
    dll.search(12)
    dll.delete(0)
    print([node.value for node in dll])
    dll.delete(1)
    print([node.value for node in dll])
    dll.delete(-1)
    print([node.value for node in dll])
