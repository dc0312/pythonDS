# Design a stack which in addition to push and pop has a function min
# which returns the minimum element
# Author : DC

class Node:

    def __init__(self, val,next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


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
        self.min = None

    def __str__(self):
        values = [str(x.val) for x in self.ll]
        return "\n".join(values)

    def isEmpty(self):
        return self.ll.head is None

    def push(self, val):
        node = Node(val)
        if self.isEmpty():
            self.ll.head = node
            self.ll.tail = node
            self.min = Node(val,node)
        else:
            if node.val < self.min.val:
                self.min = Node(val,self.min)
            else:
                self.min = Node(self.min.val,self.min)
            node.next = self.ll.head
            self.ll.head = node

    def pop(self):
        if self.isEmpty():
            print("The stack is empty.")
        else:
            self.min = self.min.next
            temp = self.ll.head
            self.ll.head = self.ll.head.next
            return temp


if __name__ == '__main__':
    s = Stack()
    print(s.isEmpty())
    s.push(5)
    s.push(6)
    s.push(3)
    s.push(7)
    print(s)
    print("Minimum Number : " + str(s.min))
    print("Popped Item : " + str(s.pop()))
    print(s)
    print("Minimum Number : " + str(s.min))
    print("Popped Item : " + str(s.pop()))
    print(s)
    print("Minimum Number : " + str(s.min))
