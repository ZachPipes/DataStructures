import unittest
from Structures.MyHeap import MyHeap

class TestHeap(unittest.TestCase):
    def setUp(self):
        """
        Create a fresh Heap instance before each test.
        """
        self.heap = MyHeap()

    def test_insert_single(self):
        """Test inserting a single element into the heap."""
        self.heap.insert(10)
        self.assertEqual(len(self.heap), 1)
        self.assertEqual(self.heap.peek(), 10)

    def test_insert_multiple(self):
        """Test inserting multiple elements maintains heap property."""
        elements = [5, 3, 8, 1]
        for e in elements:
            self.heap.insert(e)
        self.assertEqual(self.heap.peek(), min(elements))

    def test_extract_min(self):
        """Test extracting the minimum element."""
        elements = [7, 2, 6]
        for e in elements:
            self.heap.insert(e)
        min_elem = self.heap.extract_min()
        self.assertEqual(min_elem, min(elements))
        self.assertNotIn(min_elem, self.heap.to_list())  # assuming to_list() returns all elements

    def test_heap_property_after_insert(self):
        """Test heap property is maintained after multiple inserts."""
        elements = [4, 1, 3, 2]
        for e in elements:
            self.heap.insert(e)
        heap_list = self.heap.to_list()
        # The minimum element should always be at the root
        self.assertEqual(heap_list[0], min(elements))

    def test_heap_property_after_extract(self):
        """Test heap property is maintained after extraction."""
        elements = [9, 4, 6, 2]
        for e in elements:
            self.heap.insert(e)
        self.heap.extract_min()
        heap_list = self.heap.to_list()
        self.assertEqual(heap_list[0], min(heap_list))  # root is still min

    def test_len(self):
        """Test length of heap is updated correctly."""
        self.assertEqual(len(self.heap), 0)
        self.heap.insert(1)
        self.assertEqual(len(self.heap), 1)
        self.heap.insert(2)
        self.assertEqual(len(self.heap), 2)
        self.heap.extract_min()
        self.assertEqual(len(self.heap), 1)

    def test_peek_empty(self):
        """Peeking on an empty heap should return None or raise an exception."""
        self.assertIsNone(self.heap.peek())

    def test_extract_empty(self):
        """Extracting from an empty heap should return None or raise an exception."""
        self.assertIsNone(self.heap.extract_min())


if __name__ == "__main__":
    unittest.main()
