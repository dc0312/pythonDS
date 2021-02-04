# Program :  You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
# Author : DC
from linkedList.LinkedList import LinkedList


class SumOfLinkedLists:

    def sumoflinkedList(self, lla, llb):
        n1 = lla.head
        n2 = llb.head
        carry = 0
        ll = LinkedList()
        while n1 or n2:
            result = carry
            if n1 is not None:
                result += n1.value
                n1 = n1.next
            if n2 is not None:
                result += n2.value
                n2 = n2.next
            ll.add(int(result % 10))
            carry = result / 10

        return ll


if __name__ == '__main__':
    s = SumOfLinkedLists()
    lla = LinkedList()
    lla.add(7)
    lla.add(1)
    lla.add(6)
    llb = LinkedList()
    llb.add(5)
    llb.add(9)
    llb.add(2)

    print(s.sumoflinkedList(lla, llb))
