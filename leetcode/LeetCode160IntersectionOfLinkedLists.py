# Write a program to find the node at which the intersection of two singly linked lists begins.
# Author : DC
class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None

    def __iter__(self):
        node = self
        while node:
            yield node
            node = node.next

    def __str__(self):
        values = [str(x.val) for x in self]
        return '->'.join(values)


class Solution:
    def getIntersectionNode(self, llA, llB):
        lenA = 0
        lenB = 0
        node1 = llA
        node2 = llB

        while node1:
            lenA += 1
            node1 = node1.next

        while node2:
            lenB += 1
            node2 = node2.next

        shorter = llA if lenA < lenB else llB
        longer = llB if lenB > lenA else llA

        diff = abs(lenA - lenB)

        for i in range(diff):
            longer = longer.next

        while shorter != longer:
            shorter = shorter.next
            longer = longer.next

        return shorter.val

    def getIntersectionNode2(self, llA, llB):
        headA = llA
        headB = llB

        while headA != headB:
            headA = llB if headA is None else headA.next
            headB = llA if headB is None else headB.next

        return headB.val

if __name__=='__main__':
    llA = ListNode('a1')
    llA.next = ListNode('a2')
    llA.next.next = ListNode('c1')
    llA.next.next.next = ListNode('c2')
    llA.next.next.next.next = ListNode('c3')

    llB = ListNode('b1')
    llB.next = ListNode('b2')
    llB.next.next = ListNode('b3')
    llB.next.next.next = llA.next.next

    print(llA)
    print(llB)

    s = Solution()
    print(s.getIntersectionNode(llA,llB))
    print(s.getIntersectionNode2(llA,llB))

