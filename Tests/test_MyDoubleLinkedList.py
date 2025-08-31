import unittest
from Structures.MyDoubleLinkedList import MyDoubleLinkedList

class TestDoublyLinkedList(unittest.TestCase):

    def setUp(self):
        self.dll = MyDoubleLinkedList()

    def test_insert_at_head(self):
        self.dll.insert_at_head(10)
        self.assertEqual(self.dll.head.value, 10)
        self.assertEqual(self.dll.tail.value, 10)
        self.dll.insert_at_head(20)
        self.assertEqual(self.dll.head.value, 20)

    def test_insert_at_tail(self):
        self.dll.insert_at_tail(1)
        self.assertEqual(self.dll.tail.value, 1)
        self.dll.insert_at_tail(2)
        self.assertEqual(self.dll.tail.value, 2)

    def test_delete_value(self):
        self.dll.insert_at_tail(1)
        self.dll.insert_at_tail(2)
        self.dll.delete_value(1)
        self.assertEqual(self.dll.head.value, 2)
        self.dll.delete_value(2)
        self.assertIsNone(self.dll.head)
        self.assertIsNone(self.dll.tail)

    def test_find(self):
        self.dll.insert_at_tail(5)
        self.dll.insert_at_tail(10)
        node = self.dll.find(10)
        self.assertEqual(node.value, 10)
        self.assertIsNone(self.dll.find(20))

    def test_is_empty(self):
        self.assertTrue(self.dll.is_empty())
        self.dll.insert_at_head(1)
        self.assertFalse(self.dll.is_empty())

if __name__ == "__main__":
    unittest.main()
