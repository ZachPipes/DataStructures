def getLeftChildIndex(parentidx):
    return 2 * parentidx + 1
def getRightChildIndex(parentidx):
    return 2 * parentidx + 2
def getParentIndex(childidx):
    return (childidx - 1) // 2

class MyHeap:
    def __init__(self, capacity=100):
        """
        Initialize an empty heap.
        """
        self.capacity = capacity
        self.size = 0
        self.heap = []

    def hasLeftChild(self, idx):
        return getLeftChildIndex(idx) < self.size
    def hasRightChild(self, idx):
        return getRightChildIndex(idx) < self.size
    def hasParent(self, idx):
        return getParentIndex(idx) >= 0

    def leftChild(self, idx):
        return self.heap[getLeftChildIndex(idx)]
    def rightChild(self, idx):
        return self.heap[getRightChildIndex(idx)]
    def parent(self, idx):
        return self.heap[getParentIndex(idx)]

    def insert(self, value):
        """
        Insert a new value into the heap, maintaining the heap property.
        """
        if self.size == self.capacity:
            raise IndexError(f"Heap is at full capacity: {self.capacity}")

        self.heap.append(value)
        self.size += 1
        index = self.size - 1

        while self.hasParent(index) and self.parent(index) > self.heap[index]:
            parentIndex = getParentIndex(index)
            self.heap[parentIndex], self.heap[index] = self.heap[index], self.heap[parentIndex]
            index = parentIndex

    def extract_min(self):
        """
        Remove and return the minimum value from the heap (for min-heap).
        Return None if the heap is empty.
        """
        if self.size == 0:
            return None

        popped = self.heap[0]
        self.heap[0] = self.heap[self.size - 1]
        self.heap.pop()
        self.size -= 1

        # HeapyDown
        index = 0
        while self.hasLeftChild(index):
            smallerChildIndex = getLeftChildIndex(index)
            if self.hasRightChild(index) and self.heap[getRightChildIndex(index)] < self.heap[smallerChildIndex]:
                smallerChildIndex = getRightChildIndex(index)

            if self.heap[index] <= self.heap[smallerChildIndex]:
                break
            else:
                self.heap[index], self.heap[smallerChildIndex] = self.heap[smallerChildIndex], self.heap[index]

            index = smallerChildIndex
        ###

        return popped

    def peek(self):
        """
        Return the minimum value without removing it.
        Return None if the heap is empty.
        """
        if self.size > 0:
            return self.heap[0]
        return None

    def __len__(self):
        """
        Return the number of elements currently in the heap.
        """
        return self.size

    def to_list(self):
        """
        Return a list representation of the heap (mainly for testing/debugging).
        """
        return self.heap
