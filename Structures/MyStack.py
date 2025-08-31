from Structures.MyLinkedList import MyLinkedList, MyNode

class MyStack:
    def __init__(self):
        self.stack = MyLinkedList()

    def push(self, value):
        self.stack.head = MyNode(value, self.stack.head)

    def pop(self):
        if self.stack.head is None:
            raise IndexError("pop: Empty stack.")
        value = self.stack.head.value
        self.stack.delete_head()

        return value

    def peek(self):
        if self.stack.head is None:
            raise IndexError("peek: Empty stack.")
        return self.stack.head.value

    def is_empty(self):
        if self.stack.head is not None:
            return False
        return True

    def size(self):
        return self.stack.size()
