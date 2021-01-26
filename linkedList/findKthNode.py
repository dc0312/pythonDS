# Program to find the KthNode from the last in a list
# Author : DC
from linkedList.LinkedList import LinkedList


class KthNode:

    def kthNode(self, ll, k):
        slow = ll.head
        fast = ll.head
        for i in range(k):
            fast = fast.next
            if fast is None:
                print("Out of range node.")
                return

        while fast:
            slow = slow.next
            fast = fast.next

        return slow


if __name__ == '__main__':
    kNode = KthNode()
    ll = LinkedList()
    ll.generate(10, 0, 10)
    print(ll)
    print(kNode.kthNode(ll, 2))
