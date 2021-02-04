# Create a Queue using LinkedList
# Author : DC

class Node:

    def __init__(self,val):
        self.val = val
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head

        while node:
            yield node
            node = node.next

class Queue:

    def __init__(self):
        self.ll = LinkedList()

    def __str__(self):
        values = [str(x.val) for x in self.ll]
        return ' '.join(values)

    def isEmpty(self):
        return self.ll.head is None

    def enqueue(self,val):
        node = Node(val)

        if self.isEmpty():
            self.ll.head = node
            self.ll.tail = node
        else:
            self.ll.tail.next = node
            self.ll.tail = node

    def dequeue(self):
        if self.isEmpty():
            print("The queue is empty.")
        else:
            temp = self.ll.head.val
            if self.ll.head == self.ll.tail:
                self.ll.head = None
                self.ll.tail = None
            else:
                self.ll.head = self.ll.head.next
            return temp

    def peek(self):
        if self.isEmpty():
            print("The queue is empty.")
        else:
            temp = self.ll.head.val
            return temp

if __name__ == '__main__':
    q = Queue()
    print(q.isEmpty())
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q)
    print("Popped Item : "+str(q.dequeue()))
    print("Popped Item : "+str(q.dequeue()))
    print("Popped Item : "+str(q.dequeue()))
    print(q)
    print("Peeked Item : " + str(q.peek()))
    print(q)

