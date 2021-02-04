# Create a Queue using List with no size limit.
# Author : DC

class Queue:

    def __init__(self):
        self.queue = []

    def __str__(self):
        values = ([str(x) for x in self.queue])
        return ' '.join(values)

    def isEmpty(self):
        return self.queue == []

    def enqueue(self,value):
        self.queue.append(value)

    def dequeue(self):
        if self.isEmpty():
            print("The queue is empty.")
        else:
            return self.queue.pop(0)

    def peek(self):
        if self.isEmpty():
            print("The queue is empty.")
        else:
            return self.queue[0]
if __name__ == '__main__':
    q = Queue()
    print(q.isEmpty())
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q)
    print("Popped Item : "+str(q.dequeue()))
    print(q)
    print("Peeked Item : " + str(q.peek()))
    print(q)