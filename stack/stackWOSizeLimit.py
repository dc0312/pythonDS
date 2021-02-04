# Create a Stack using List with no size limit.
# Author : DC
class Stack:

    def __init__(self):
        self.list = []

    def __str__(self):
        tempList = []
        tempList.extend(self.list)
        tempList.reverse()
        values = ([ str(x) for x in tempList])
        return "\n".join(values)

    def isEmpty(self):
        return self.list == []

    def push(self,value):
        self.list.append(value)

    def pop(self):
        if self.isEmpty():
            print("The stack is empty.")
        else:
            return self.list.pop()

    def peek(self):
        if self.isEmpty():
            print("The stack is empty.")
        else:
            return self.list[len(self.list)-1]

    def delete(self):
        if self.isEmpty():
            print("The stack is empty.")
        else:
            self.list = []

if __name__ == '__main__':

    s = Stack()
    print(s.isEmpty())
    s.push(1)
    s.push(2)
    s.push(3)
    print(s)
    print("=====> Popped Element : "+ str(s.pop()))
    print("=====> Peeked Element : "+ str(s.peek()))
    print(s)
    s.delete()
    print(s)