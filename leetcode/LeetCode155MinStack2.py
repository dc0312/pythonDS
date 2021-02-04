# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
# Author : DC
class MinStack(object):

    def __init__(self):
        self.stack = []

    def __str__(self):
        return ",".join(str(self.stack))

    def push(self, x):
        curMin = self.getMin()
        if curMin == None or x < curMin:
            curMin = x
        self.stack.append((x, curMin))

    def pop(self):
        return self.stack.pop()

    def top(self):
        if len(self.stack) == 0:
            return None
        return self.stack[len(self.stack) - 1][0]

    def getMin(self):
        if len(self.stack) == 0:
            return None
        return self.stack[len(self.stack) - 1][1]


if __name__ == '__main__':
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print("Min : " + str(minStack.getMin()))
    print("Top : " + str(minStack.top()))
    print("Pop Item : " + str(minStack.pop()))
    print("Stack : " + str(minStack))
    print("Min : " + str(minStack.getMin()))
    print("Top : " + str(minStack.top()))
