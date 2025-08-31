from Structures.MyDoubleLinkedList import MyDoubleLinkedList

class MyQueue:
    def __init__(self):
        """Initialize an empty queue"""
        self.queue = MyDoubleLinkedList()

    def enqueue(self, value):
        """Add a value to the end of the queue"""
        self.queue.insert_at_tail(value)

    def dequeue(self):
        """Remove and return the value at the front of the queue"""
        value = self.queue.pop()
        return value

    def peek(self):
        """Return the value at the front without removing it"""
        return self.queue.peek()

    def is_empty(self):
        """Return True if the queue has no elements, else False"""
        return len(self.queue) == 0

    def size(self):
        """Return the number of elements in the queue"""
        return len(self.queue)
