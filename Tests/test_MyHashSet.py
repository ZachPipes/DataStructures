import unittest
from Structures.MyHashSet import MyHashSet

class TestHashSet(unittest.TestCase):
    def setUp(self):
        """Create a fresh HashSet before each test."""
        self.set = MyHashSet()

    def test_add_new_key(self):
        self.set.add("a")
        self.assertTrue(self.set.contains("a"))
        self.assertEqual(len(self.set), 1)

    def test_add_duplicate_key(self):
        self.set.add("a")
        self.set.add("a")  # duplicate
        self.assertEqual(len(self.set), 1)

    def test_contains_true(self):
        self.set.add("b")
        self.assertTrue(self.set.contains("b"))

    def test_contains_false(self):
        self.assertFalse(self.set.contains("missing"))

    def test_remove_existing_key(self):
        self.set.add("c")
        self.set.remove("c")
        self.assertFalse(self.set.contains("c"))
        self.assertEqual(len(self.set), 0)

    def test_remove_nonexistent_key(self):
        # Removing a key that doesn’t exist should not raise an error
        self.set.remove("missing")
        self.assertEqual(len(self.set), 0)

    def test_len(self):
        self.assertEqual(len(self.set), 0)
        self.set.add("x")
        self.set.add("y")
        self.assertEqual(len(self.set), 2)
        self.set.remove("x")
        self.assertEqual(len(self.set), 1)

    def test_str(self):
        self.set.add("p")
        self.set.add("q")
        result = str(self.set)
        self.assertIn("p", result)
        self.assertIn("q", result)

if __name__ == "__main__":
    unittest.main()
