# Program to find intersection of two linked list
# Author : DC
from linkedList.LinkedList import LinkedList, Node


class Intersection:

    def getIntersection(self,lla,llb):
        if lla.tail is not llb.tail:
            return False
        lenA = LinkedList.len(lla)
        lenB = LinkedList.len(llb)

        shorter = lla if lenA < lenB else llb
        longer = llb if lenB > lenA else lla

        diff = LinkedList.len(longer) - LinkedList.len(shorter)
        shorter = shorter.head
        longer = longer.head
        for i in range(diff):
            longer = longer.next

        while shorter != longer:
            shorter = shorter.next
            longer = longer.next

        return shorter.value

if __name__ == '__main__':
    ll = LinkedList()
    ll.head = Node(1)
    ll.head.next = Node(2)
    ll.head.next.next = Node(3)
    ll.head.next.next.next = Node(4)

    ll1 = LinkedList()
    ll1.head = Node(1)
    ll1.head.next = Node(2)
    ll1.head.next.next = Node(2)
    ll1.head.next.next.next = ll.head.next.next

    print(ll)
    print(ll1)

    i = Intersection()
    print(i.getIntersection(ll,ll1))