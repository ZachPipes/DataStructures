class MyDoubleNode:
    def __init__(self, value, nextNode=None, prevNode=None):
        self.value = value
        self.next = nextNode
        self.prev = prevNode

class MyDoubleLinkedList:
    def __init__(self):
        """Initialize an empty doubly linked list"""
        self.head = None
        self.tail = None

    def __len__(self):
        i = 0
        curr = self.head
        while curr:
            i += 1
            curr = curr.next
        return i

    def pop(self):
        if self.head is None:
            raise IndexError("pop: DoubleLinkedList is empty.")
        value = self.head.value
        self.delete_value(value)

        return value

    def peek(self):
        if self.head is None:
            raise IndexError("pop: DoubleLinkedList is empty.")
        value = self.head.value

        return value

    def insert_at_head(self, value):
        """Insert a new node with value at the head"""
        # If there are no nodes in the list
        newNode = MyDoubleNode(value, nextNode=self.head)
        if self.head:
            self.head.prev = newNode
        else:
            # Empty list
            self.tail = newNode
        self.head = newNode

    def insert_at_tail(self, value):
        """Insert a new node with value at the tail"""
        newNode = MyDoubleNode(value, prevNode=self.tail)
        if self.tail:
            self.tail.next = newNode
        else:
            # Empty list
            self.head = newNode
        self.tail = newNode

    def delete_value(self, value):
        curr = self.head
        while curr:
            if curr.value == value:
                # Update previous node
                if curr.prev:
                    curr.prev.next = curr.next
                else:
                    # Deleting the head
                    self.head = curr.next

                # Update next node
                if curr.next:
                    curr.next.prev = curr.prev
                else:
                    # Deleting the tail
                    self.tail = curr.prev
                return
            curr = curr.next

    def find(self, value):
        """Return the node containing value, or None if not found"""
        curr = self.head

        while curr:
            if curr.value is value:
                return curr
            curr = curr.next

        return None

    def is_empty(self):
        """Return True if the list has no elements, else False"""
        return self.head is None
