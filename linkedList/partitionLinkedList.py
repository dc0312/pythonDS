# Program to partition a linked list around value x, such that
# all nodes less than x come before all nodes greater than or equal to x
# Author : DC
from linkedList.LinkedList import LinkedList, Node


class Partition:

    def partition(self, ll, value):
        head = ll.head
        before = before_head = Node(0)
        after = after_head = Node(0)
        while head:
            # If the original list node is lesser than the given x,
            # assign it to the before list.
            if head.value < value:
                before.next = head
                before = before.next
            else:
                # If the original list node is greater or equal to the given x,
                # assign it to the after list.
                after.next = head
                after = after.next

            # move ahead in the original list
            head = head.next

            # Last node of "after" list would also be ending node of the reformed list
        after.next = None
            # Once all the nodes are correctly assigned to the two lists,
        # combine them to form a single list which would be returned.
        before.next = after_head.next
        newll = LinkedList()
        newll.head = before_head.next
        return newll


if __name__ == '__main__':
    part = Partition()
    ll = LinkedList()
    ll.add(5)
    ll.add(2)
    ll.add(3)
    ll.add(1)
    ll.add(4)
    print(ll)
    print(part.partition(ll, 3))
