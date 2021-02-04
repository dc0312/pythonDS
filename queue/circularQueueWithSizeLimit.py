# Create a Circular Queue using List with size limit.
# Author : DC

class CircularQueue:

    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.queue = maxSize * [None]
        self.top = -1
        self.start = -1

    def __str__(self):
        values = [str(x) for x in self.queue]
        return ' '.join(values)

    def isEmpty(self):
        return self.top == -1 and self.start == -1

    def isFull(self):
        if self.start == self.top + 1:
            return True
        elif self.start == 0 and self.top + 1 == self.maxSize:
            return True
        else:
            return False

    def enqueue(self, val):
        if self.isFull():
            print("The queue is full.")
        elif self.isEmpty():
            self.top = 0
            self.start = 0
            self.queue[self.top] = val
        elif self.top + 1 == self.maxSize:
            self.top = 0
            self.queue[self.top] = val
        else:
            self.top += 1
            self.queue[self.top] = val

    def dequeue(self):
        if self.isEmpty():
            print("The queue is empty.")
        else:
            temp = self.queue[self.start]
            start = self.start
            if self.start == self.top:
                self.start = -1
                self.top = -1
            elif self.start + 1 == self.maxSize:
                self.start = 0
            else:
                self.start += 1
            self.queue[start] = None
            return temp

    def peek(self):
        if self.isEmpty():
            print("The queue is empty.")
        else:
            return self.queue[self.start]

    def delete(self):
        self.queue = self.maxSize * [None]
        self.top = -1
        self.start = -1


if __name__ == '__main__':
    c = CircularQueue(4)
    print(c.isEmpty())
    print(c.isFull())
    c.enqueue(1)
    c.enqueue(2)
    c.enqueue(3)
    c.enqueue(4)
    print(c)
    print("Popped item " + str(c.dequeue()))
    print(c)
    c.enqueue(5)
    print(c)
    print("Popped item " + str(c.dequeue()))
    print(c)
    print("Peeked item " + str(c.peek()))
    print(c)
