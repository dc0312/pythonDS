# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
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

class MinStack(object):

    def __init__(self):
        self.ll = LinkedList()
        self.min = None

    def push(self, x):
        node = Node(x)
        if self.ll.head is None:
            self.ll.head = node
            self.min = Node(x,self.min)
        else:
            if x < self.min.val:
                self.min = Node(x,self.min)
            else:
                self.min = Node(self.min.val, self.min)
            node.next = self.ll.head
            self.ll.head = node

    def pop(self):
        if self.ll.head is None:
            print("The stack is empty")
        else:
            self.min = self.min.next
            temp = self.ll.head
            self.ll.head = self.ll.head.next
            return temp

    def top(self):
        return self.ll.head

    def getMin(self):
        return self.min

if __name__ == '__main__':
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print("Min : "+str(minStack.min))
    print("Top : "+str(minStack.min))
    print("Pop Item : "+str(minStack.pop()))
    print("Min : " + str(minStack.min))
    print("Top : " + str(minStack.min))
