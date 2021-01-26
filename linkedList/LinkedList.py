# Program contains methods related to linked list.
# Author : DC
from random import randint


class Node:

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def __str__(self):
        values = [str(x.value) for x in self]
        return '->'.join(values)

    def len(self):
        count = 0
        node = self.head
        while node:
            node = node.next
            count += 1
        return count

    def add(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        return self.tail

    def generate(self, n, min_val, max_val):
        for i in range(n):
            self.add(randint(min_val, max_val))
        return self

# class Main:
#
#     def __init__(self):
#         pass
#
# if __name__ == '__main__':
#     ll = LinkedList()
#     ll.generate(10,0,99)
#     print(ll)
