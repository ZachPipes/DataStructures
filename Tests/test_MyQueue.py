import unittest
from Structures.MyQueue import MyQueue

class TestMyQueue(unittest.TestCase):

    def setUp(self):
        """Initialize a fresh queue before each test"""
        self.queue = MyQueue()

    def test_enqueue_and_peek(self):
        self.queue.enqueue(10)
        self.assertEqual(self.queue.peek(), 10)
        self.queue.enqueue(20)
        self.assertEqual(self.queue.peek(), 10)  # peek should return the first enqueued item

    def test_dequeue(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        value = self.queue.dequeue()
        self.assertEqual(value, 1)
        self.assertEqual(self.queue.peek(), 2)

    def test_dequeue_empty(self):
        with self.assertRaises(IndexError):
            self.queue.dequeue()

    def test_peek_empty(self):
        with self.assertRaises(IndexError):
            self.queue.peek()

    def test_is_empty(self):
        self.assertTrue(self.queue.is_empty())
        self.queue.enqueue(5)
        self.assertFalse(self.queue.is_empty())
        self.queue.dequeue()
        self.assertTrue(self.queue.is_empty())

    def test_size(self):
        self.assertEqual(self.queue.size(), 0)
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.assertEqual(self.queue.size(), 2)
        self.queue.dequeue()
        self.assertEqual(self.queue.size(), 1)

if __name__ == "__main__":
    unittest.main()
