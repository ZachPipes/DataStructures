import unittest
from Structures.MyLinkedList import MyLinkedList, MyNode

class TestMyLinkedList(unittest.TestCase):

    # 1. Creation & Initialization
    def test_empty_list(self):
        ll = MyLinkedList()
        self.assertIsNone(ll.head)

    def test_single_node(self):
        node = MyNode(10)
        self.assertEqual(node.value, 10)
        self.assertIsNone(node.next)

    # 2. Insertion
    def test_insert_at_head(self):
        ll = MyLinkedList()
        ll.insert_at_head(5)
        self.assertEqual(ll.head.value, 5)

    def test_insert_at_tail(self):
        ll = MyLinkedList()
        ll.insert_at_tail(7)
        self.assertIn(ll.head.value, [7, None])

    def test_insert_at_index(self):
        ll = MyLinkedList()
        ll.insert_at_tail(1)
        ll.insert_at_tail(3)
        ll.insert_at_index(1, 2)
        current = ll.head
        for _ in range(1):
            current = current.next

        self.assertEqual(current.value, 2)

    def test_insert_after_node(self):
        ll = MyLinkedList()
        ll.head = MyNode(1)  # Initialize the list with one node
        node = ll.head  # Reference to the head node
        ll.insert_after_node(node, 2)
        self.assertEqual(ll.head.next.value, 2)

    # 3. Deletion
    def test_delete_head(self):
        ll = MyLinkedList()
        ll.insert_at_head(1)
        ll.insert_at_head(2)
        ll.delete_head()
        self.assertEqual(ll.head.value, 1)

    def test_delete_tail(self):
        ll = MyLinkedList()
        ll.insert_at_tail(1)
        ll.insert_at_tail(2)
        ll.delete_tail()
        self.assertIsNone(ll.head.next)

    def test_delete_by_value(self):
        ll = MyLinkedList()
        ll.insert_at_tail(1)
        ll.insert_at_tail(2)
        ll.delete_value(1)
        self.assertEqual(ll.head.value, 2)

    def test_delete_at_index(self):
        ll = MyLinkedList()
        ll.insert_at_tail(1)
        ll.insert_at_tail(2)
        ll.insert_at_tail(3)
        ll.delete_at_index(1)
        self.assertEqual(ll.head.next.value, 3)

    # 4. Traversal & Search
    def test_traverse(self):
        ll = MyLinkedList()
        values = [1,2,3]
        for v in values:
            ll.insert_at_tail(v)
        collected = []
        current = ll.head
        while current:
            collected.append(current.value)
            current = current.next
        self.assertEqual(collected, values)

    def test_find(self):
        ll = MyLinkedList()
        ll.insert_at_tail(1)
        ll.insert_at_tail(2)
        node = ll.find(2)
        self.assertEqual(node.value, 2)

    def test_contains(self):
        ll = MyLinkedList()
        ll.insert_at_tail(5)
        self.assertTrue(5 in ll)
        self.assertFalse(10 in ll)

    # 5. Size & Length
    def test_size(self):
        ll = MyLinkedList()
        ll.insert_at_tail(1)
        ll.insert_at_tail(2)
        self.assertEqual(ll.size(), 2)

    def test_empty_check(self):
        ll = MyLinkedList()
        self.assertIsNone(ll.head)

    # 6. Reversal
    def test_reverse(self):
        ll = MyLinkedList()
        for v in [1,2,3]:
            ll.insert_at_tail(v)
        ll.reverse()
        values = []
        current = ll.head
        while current:
            values.append(current.value)
            current = current.next
        self.assertEqual(values, [3,2,1])

    def test_reverse_empty(self):
        ll = MyLinkedList()
        ll.reverse()
        self.assertIsNone(ll.head)

    def test_reverse_single(self):
        ll = MyLinkedList()
        ll.insert_at_head(1)
        ll.reverse()
        self.assertEqual(ll.head.value, 1)

    # 7. Advanced Operations
    def test_sort(self):
        ll = MyLinkedList()
        for v in [3,1,2]:
            ll.insert_at_tail(v)
        ll.sort()
        values = []
        current = ll.head
        while current:
            values.append(current.value)
            current = current.next
        self.assertEqual(values, [1,2,3])

    def test_merge(self):
        ll1 = MyLinkedList()
        ll2 = MyLinkedList()
        for v in [1,3]: ll1.insert_at_tail(v)
        for v in [2,4]: ll2.insert_at_tail(v)
        ll1.merge(ll2)
        values = []
        current = ll1.head
        while current:
            values.append(current.value)
            current = current.next
        self.assertEqual(values, [1,3,2,4])

if __name__ == '__main__':
    unittest.main()
