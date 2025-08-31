import unittest
from Structures.MyStack import MyStack

class TestMyStack(unittest.TestCase):

    def setUp(self):
        self.stack = MyStack()

    def test_push_and_peek(self):
        self.stack.push(10)
        self.assertEqual(self.stack.peek(), 10)
        self.stack.push(20)
        self.assertEqual(self.stack.peek(), 20)

    def test_pop(self):
        self.stack.push(1)
        self.stack.push(2)
        value = self.stack.pop()
        self.assertEqual(value, 2)
        self.assertEqual(self.stack.peek(), 1)

    def test_pop_empty(self):
        with self.assertRaises(IndexError):
            self.stack.pop()

    def test_peek_empty(self):
        with self.assertRaises(IndexError):
            self.stack.peek()

    def test_is_empty(self):
        self.assertTrue(self.stack.is_empty())
        self.stack.push(5)
        self.assertFalse(self.stack.is_empty())
        self.stack.pop()
        self.assertTrue(self.stack.is_empty())

    def test_size(self):
        self.assertEqual(self.stack.size(), 0)
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.size(), 2)
        self.stack.pop()
        self.assertEqual(self.stack.size(), 1)

if __name__ == "__main__":
    unittest.main()