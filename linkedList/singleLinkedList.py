# Program contains all the basic functions related to the single linked list
# Author : DC

class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class SingleLinkedList:

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
                self.head = newNode
            elif location == 1:
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                newNode.next = tempNode.next
                tempNode.next = newNode

    def delete(self, location):
        if self.head is None:
            print("The single linked list does not exist during delete")
            return
        else:
            if self.head.next is None:
                self.head = None
                self.tail = None
            elif location == 0:
                self.head = self.head.next
            elif location == 1:
                # tempNode = self.head
                # prevNode = self.head
                # while tempNode.next is not None:
                #     print("printnode ----> " + str(tempNode.value))
                #     prevNode = tempNode
                #     tempNode = tempNode.next
                # self.tail = prevNode
                # prevNode.next = None
                tempNode = self.head
                while tempNode is not None:
                    if self.tail == tempNode.next:
                        break
                    tempNode = tempNode.next
                tempNode.next = None
                self.tail = tempNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next

    def traverse(self):
        if self.head is None:
            print("The single linked list does not exist during traversing.")
            return
        tempNode = self.head
        while tempNode is not None:
            print(tempNode.value)
            tempNode = tempNode.next

    def clear(self):
        if self.head is None:
            print("The single linked list does not exist during clear.")
        else:
            self.head = None
            self.tail = None

    def search(self,value):
        if self.head is None:
            print("The single linked list does not exist during search.")
            return
        else:
            tempNode = self.head
            while tempNode is not None:
                if tempNode.value == value:
                    print("Value found")
                    return
                tempNode = tempNode.next
            print("The value not found in SLL")
            return




class Main:

    def __init__(self):
        pass


if __name__ == '__main__':
    sll = SingleLinkedList()
    sll.insert(1, 0)
    sll.insert(2, 1)
    sll.insert(4, 1)
    sll.insert(3, 2)
    sll.traverse()
    sll.delete(2)
    sll.traverse()
    sll.search(3)
    print([node.value for node in sll])