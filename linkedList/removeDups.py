# Program to remove duplicates from the list
# Author : DC

from linkedList.LinkedList import LinkedList


class RemoveDups:

    def __init__(self):
        pass

    def removeDups(self, ll):
        if ll.head is None:
            print("The list is empty.")
        else:
            tempNode = ll.head
            visited = set([tempNode.value])
            while tempNode.next:
                if tempNode.next.value in visited:
                    tempNode.next = tempNode.next.next
                else:
                    visited.add(tempNode.next.value)
                    tempNode = tempNode.next
            return ll

    def removeDups1(self,ll):
        if ll.head is None:
            print("The list is empty.")
        else:
            tempNode = ll.head
            while tempNode:
                runner = tempNode
                while runner.next:
                    if tempNode.value == runner.next.value:
                        runner.next = runner.next.next
                    else:
                        runner = runner.next
                tempNode = tempNode.next
        return ll


if __name__ == '__main__':
    rd = RemoveDups()
    ll = LinkedList()
    ll.generate(10, 0, 6)
    print(ll)
    rd.removeDups1(ll)
    print(ll)
