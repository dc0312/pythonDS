# Create a Stack using List with size limit.
# Author : DC
class Stack:

    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = []

    def __str__(self):
        tempList = []
        tempList.extend(self.list)
        tempList.reverse()
        values = ([str(x) for x in tempList])
        return "\n".join(values)

    def isEmpty(self):
        return self.list == []

    def isFull(self):
        return len(self.list) == self.maxSize

    def push(self, value):
        if self.isFull():
            print("The stack is full. Cannot add new element")
        else:
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
            return self.list[len(self.list) - 1]


if __name__ == '__main__':
    s = Stack(4)
    print(s.isEmpty())
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    print(s)
    s.push(5)
    print("==>Popped Item : "+str(s.pop()))
    print("==>Peek Item : "+str(s.peek()))
