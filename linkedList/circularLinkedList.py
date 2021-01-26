# Program contains all the basic functions related to the circular single linked list
# Author : DC
class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class CircularSingleLinkedList:

    counter = 0

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
           self.counter +=1
        else:
            if location >= self.counter:
                location = 1
            if location == 0:
                newNode .next = self.head
                self.head = newNode
                self.tail.next = newNode
                self.counter += 1
            elif location == 1:
                newNode.next = self.tail.next
                self.tail.next = newNode
                self.tail = newNode
                self.counter += 1

            else:
                tempNode = self.head
                index = 0
                while index < location-1:
                    tempNode = tempNode.next
                    index+=1
                newNode.next = tempNode.next
                tempNode.next = newNode
                self.counter += 1

    def traverse(self):
        if self.head is None:
            print("The list is empty for traversing")
        else:
            tempNode = self.head
            while True:
                print(tempNode.value)
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    break

    def delete(self,location):
        if self.head is None:
            print("The list is empty for delete")
        else:
            if self.head == self.tail:
                self.head.next = None
                self.head = None
                self.tail = None
                return 
            if location >  self.counter:
                location =  1
            if location == 0:
                self.head = self.head.next
                self.tail.next = self.head
            elif location == 1:
                tempNode = self.head

                while tempNode is not None:
                    if self.tail == tempNode.next:
                        break
                    tempNode = tempNode.next
                tempNode.next = self.tail.next
                self.tail = tempNode
            else:
                tempNode = self.head
                index = 0
                while index < location-1:
                    tempNode = tempNode.next
                    index+=1
                tempNode.next = tempNode.next.next

    def search(self,location):
        if self.head is None:
            print("The list is empty for delete")
            return
        tempNode = self.head
        index = 0
        while index != location:
            tempNode = tempNode.next
            if tempNode == self.tail.next:
                print("Location not found.")
                return
            index+=1
        print("Value found : "+str(tempNode.value))



class Main:

    def __init__(self):
        pass

if __name__ == '__main__':
    csll = CircularSingleLinkedList()
    csll.insert(1,0)
    csll.insert(0,0)
    csll.insert(2,1)
    csll.insert(4,1)
    csll.insert(3,3)
    csll.insert(5,6)
    csll.insert(6,7)

    print([ node.value for node in csll ])

    csll.traverse()

    csll.delete(0)

    print([node.value for node in csll])
    csll.delete(1)

    print([node.value for node in csll])

    csll.delete(15)

    print([node.value for node in csll])
    csll.search(3)