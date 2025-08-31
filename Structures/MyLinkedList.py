class MyNode:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.next = nextNode


class MyLinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        return MyLinkedListIterator(self)

    def __str__(self):
        values = [str(value) for value in self]
        return '[' + ', '.join(values) + ']'

    def __contains__(self, value):
        curr = self.head

        while curr:
            if curr.value is value:
                return True
            curr = curr.next

        return False

    def insert_at_head(self, value):
        # If there are no nodes in the list
        if self.head is None:
            self.head = MyNode(value)
            return

        secondNode = self.head
        self.head = MyNode(value, secondNode)

    def insert_at_tail(self, value):
        # If there are zero nodes in the list
        if self.head is None:
            self.head = MyNode(value)
            return

        # Iterates to the last node
        nodeIter = self.head
        while nodeIter.next is not None:
            nodeIter = nodeIter.next

        nodeIter.next = MyNode(value)

    def insert_at_index(self, index, value):
        # Iterate until the specified index is present
        ptr = self.head
        i = 0
        while i < index:
            if ptr.next is None:
                return IndexError("insert_at_index: Index out of bounds")
            ptr = ptr.next
            i += 1

        # Inserting node
        duplicatedNode = MyNode(ptr.value, ptr.next)
        ptr.value = value
        ptr.next = duplicatedNode

    def insert_after_node(self, node, value):
        nextNode = node.next
        node.next = MyNode(value, nextNode)

    def delete_head(self):
        if self.head is not None:
            self.head = self.head.next

    def delete_tail(self):
        # If no nodes
        if self.head is None:
            return

        # If one node
        if self.head.next is None:
            self.head = None

        # Iterates to the last node
        nodeIter = self.head
        while nodeIter.next.next is not None:
            nodeIter = nodeIter.next

        nodeIter.next = None

    def delete_value(self, value):
        # If no nodes
        if self.head is None:
            return

        # Iterating to the specified valued node
        curr = self.head
        prev = curr

        # If it's the very first node
        if curr.value is value:
            self.head = curr.next
            return

        while curr.value is not value:
            prev = curr
            curr = curr.next
        prev.next = curr.next

    def delete_at_index(self, index):
        if index < 0: return IndexError("delete_at_index: Index out of bounds")

        # Iterating to the specified index
        i = 0
        curr = self.head
        prev = curr
        while i != index:
            if curr.next.next is None: return IndexError("delete_at_index: Index out of bounds")
            prev = curr
            curr = curr.next
            i += 1
        prev.next = curr.next

    def find(self, value):
        curr = self.head

        while curr:
            if curr.value is value:
                return curr
            curr = curr.next

        return None

    def size(self):
        i = 0
        curr = self.head
        while curr:
            i += 1
            curr = curr.next
        return i

    def reverse(self):
        # If empty
        if self.head is None:
            return

        # If only one element
        if self.head.next is None:
            return

        prev = None
        curr = self.head
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        self.head = prev

    def merge(self, ll2):
        # Nothing to merge
        if ll2.head is None:
            return
        # Starting ll is empty
        if self.head is None:
            self.head = ll2.head

        # Iterate to end of first list
        ptr1 = self.head
        while ptr1.next:
            ptr1 = ptr1.next

        ptr1.next = ll2.head

    def sort(self):
        # If empty
        if self.head is None:
            return self.head

        # If only one node
        if self.head.next is None:
            return self.head

        self.head = _sort_ll(self.head)

        return self.head



def _sort_ll(head):
    # If empty
    if head is None:
        return head

    # If only one node
    if head.next is None:
        return head

    left_head, right_head = _split_heads(head)

    left_sorted = _sort_ll(left_head)
    right_sorted = _sort_ll(right_head)

    return _merge(left_sorted, right_sorted)

def _split_heads(head):
    fastptr = head
    slowptr = head

    prev = None
    while fastptr:
        prev = slowptr
        slowptr = slowptr.next
        if fastptr.next:
            fastptr = fastptr.next.next
        else:
            fastptr = fastptr.next

    prev.next = None

    return head, slowptr

def _merge(h1, h2):
    if h1 is None and h2 is None:
        return None
    if h1 is None:
        return h2
    if h2 is None:
        return h1

    dummy = MyNode(0)
    ptr = dummy

    while h1 and h2:
        if h1.value < h2.value:
            ptr.next = h1
            h1 = h1.next

        else:
            ptr.next = h2
            h2 = h2.next

        ptr = ptr.next

    # Appending the rest of the variables
    ptr.next = h1 or h2

    return dummy.next



class MyLinkedListIterator:
    def __init__(self, mylinkedlist):
        self._current = mylinkedlist.head

    def __next__(self):
        if self._current is None:
            raise StopIteration

        value = self._current.value
        self._current = self._current.next
        return value

    def __iter__(self):
        return self
