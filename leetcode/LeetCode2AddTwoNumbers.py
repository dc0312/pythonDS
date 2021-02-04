# Program :  You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
# Author : DC

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __iter__(self):
        node = self
        while node:
            yield node
            node = node.next

    def __str__(self):
        values = [str(x.val) for x in self]
        return '->'.join(values)


class LeetCode2AddTwoNumbers:
    def addTwoNumbers(self, l1, l2):
        ll = ListNode()
        ll_head = ll
        carry = 0
        while l1 or l2:
            result = carry
            if l1 is not None:
                result += l1.val
                l1 = l1.next
            if l2 is not None:
                result += l2.val
                l2 = l2.next
            ll.next = ListNode(int(result % 10))
            ll = ll.next

            carry = result // 10
        if carry > 0 :
            ll.next = ListNode(carry)
        return ll_head.next


if __name__ == '__main__':
    lla = ListNode(9)
    lla.next = ListNode(9)
    lla.next.next = ListNode(9)

    llb = ListNode(9)
    llb.next = ListNode(9)
    llb.next.next = ListNode(9)
    llb.next.next.next = ListNode(9)
    llb.next.next.next.next = ListNode(9)

    s = LeetCode2AddTwoNumbers()

    print(s.addTwoNumbers(lla, llb))
