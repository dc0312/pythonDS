#Given the head of a linked list and a value x, partition it such that all
# nodes less than x come before nodes greater than or equal to x.
# You should preserve the original relative order of the nodes in each of the two partitions.
# Author : DC
class Node:

    def __init__(self,value):
        self.value = value
        self.next = None

    def __iter__(self):
        node = self
        while node:
            yield node
            node = node.next

    def __str__(self):
        values = [str(x.value) for x in self]
        return '->'.join(values)

class Solution:

    def partition(self,head,value):
        before = before_head = Node(0)
        after = after_head = Node(0)

        while head:
            if head.value < value :
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next
            head = head.next

        after.next = None
        before.next = after_head.next

        return before_head.next

if __name__ == '__main__':
    sol = Solution()
    node = Node(1)
    node.next = Node(4)
    node.next.next = Node(3)
    node.next.next.next = Node(2)
    node.next.next.next.next = Node(5)
    node.next.next.next.next.next = Node(2)
    print(node)

    print(sol.partition(node,3))
