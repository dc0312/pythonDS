# Create a Stack using LinkedList.
# Author : DC
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

class Stack:

    def __init__(self):
        self.ll = LinkedList()

    def __str__(self):
        values = ([str(x.val) for x in self.ll])
        return "\n".join(values)

    def isEmpty(self):
        return self.ll.head is None

    def push(self,val):
        node = Node(val)
        node.next = self.ll.head
        self.ll.head = node

    def pop(self):
        if self.ll.head is None:
            print("The stack is empty.")
        else:
            tempVal = self.ll.head.val
            self.ll.head = self.ll.head.next
            return tempVal

    def peek(self):
        if self.ll.head is None:
            print("The stack is empty.")
        else:
            return self.ll.head.val

if __name__ == '__main__':
    s = Stack()
    print(s.isEmpty())
    s.push(1)
    s.push(2)
    s.push(3)
    print(s)
    print("Popped element : "+str(s.pop()))
    print(s)
    print("Peeked element : "+str(s.peek()))
    print(s)