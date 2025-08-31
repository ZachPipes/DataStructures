import unittest
from Structures.MyHashMap import MyHashMap

class TestHashMap(unittest.TestCase):
    def setUp(self):
        """
        Set up a fresh HashMap instance before each test.
        """
        self.map = MyHashMap()

    def test_put_new_key(self):
        self.map.put("a", 1)
        self.assertEqual(self.map.get("a"), 1)

    def test_put_update_key(self):
        self.map.put("a", 1)
        self.map.put("a", 2)
        self.assertEqual(self.map.get("a"), 2)

    def test_get_existing_key(self):
        self.map.put("a", 10)
        self.assertEqual(self.map.get("a"), 10)

    def test_get_nonexistent_key(self):
        self.assertIsNone(self.map.get("missing"))

    def test_remove_existing_key(self):
        self.map.put("a", 1)
        self.map.remove("a")
        self.assertIsNone(self.map.get("a"))
        self.assertFalse(self.map.contains_key("a"))

    def test_remove_nonexistent_key(self):
        # Should not raise an error
        self.map.remove("missing")
        self.assertEqual(len(self.map), 0)

    def test_contains_key_true(self):
        self.map.put("a", 1)
        self.assertTrue(self.map.contains_key("a"))

    def test_contains_key_false(self):
        self.assertFalse(self.map.contains_key("missing"))

    def test_keys(self):
        keys_to_add = ["a", "b", "c"]
        for k in keys_to_add:
            self.map.put(k, k.upper())
        keys = self.map.keys()
        self.assertCountEqual(keys, keys_to_add)

    def test_values(self):
        values_to_add = {"a": 1, "b": 2, "c": 3}
        for k, v in values_to_add.items():
            self.map.put(k, v)
        values = self.map.values()
        self.assertCountEqual(values, values_to_add.values())

    def test_len(self):
        self.assertEqual(len(self.map), 0)
        self.map.put("a", 1)
        self.map.put("b", 2)
        self.assertEqual(len(self.map), 2)
        self.map.remove("a")
        self.assertEqual(len(self.map), 1)

    def test_str(self):
        self.map.put("x", 42)
        result = str(self.map)
        self.assertIn("x", result)
        self.assertIn("42", result)


if __name__ == "__main__":
    unittest.main()
