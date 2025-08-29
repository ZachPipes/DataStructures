import unittest
from Structures.MyList import MyList

class TestMyList(unittest.TestCase):
    def setUp(self):
        self.arr = MyList()

    # --------------------
    # Append and Length
    # --------------------
    def test_append_and_len(self):
        self.arr.append(10)
        self.arr.append(20)
        self.assertEqual(len(self.arr), 2)
        self.assertEqual(self.arr[0], 10)
        self.assertEqual(self.arr[1], 20)

    def test_append_triggers_resize(self):
        small = MyList(2)
        small.append(1)
        small.append(2)
        self.assertEqual(small.capacity, 2)
        small.append(3)  # should trigger double_capacity
        self.assertEqual(small.capacity, 4)
        self.assertEqual(len(small), 3)

    # --------------------
    # Insert
    # --------------------
    def test_insert_middle(self):
        self.arr.append(1)
        self.arr.append(3)
        self.arr.insert(1, 2)
        self.assertEqual(str(self.arr), "[1, 2, 3]")

    def test_insert_at_start(self):
        self.arr.append(1)
        self.arr.append(2)
        self.arr.insert(0, 0)
        self.assertEqual(str(self.arr), "[0, 1, 2]")

    def test_insert_at_end(self):
        self.arr.append(1)
        self.arr.insert(len(self.arr), 2)
        self.assertEqual(str(self.arr), "[1, 2]")

    def test_insert_out_of_bounds(self):
        with self.assertRaises(IndexError):
            self.arr.insert(5, 100)

    # --------------------
    # Pop
    # --------------------
    def test_pop_last(self):
        self.arr.append(5)
        self.arr.append(6)
        val = self.arr.pop()
        self.assertEqual(val, 6)
        self.assertEqual(len(self.arr), 1)

    def test_pop_index(self):
        self.arr.append(1)
        self.arr.append(2)
        self.arr.append(3)
        val = self.arr.pop(1)
        self.assertEqual(val, 2)
        self.assertEqual(str(self.arr), "[1, 3]")

    def test_pop_empty_raises(self):
        with self.assertRaises(IndexError):
            self.arr.pop()

    def test_pop_index_out_of_range(self):
        self.arr.append(1)
        with self.assertRaises(IndexError):
            self.arr.pop(5)

    # --------------------
    # Remove
    # --------------------
    def test_remove_existing(self):
        self.arr.append(1)
        self.arr.append(2)
        self.arr.append(1)
        self.arr.remove(1)  # should remove first occurrence
        self.assertEqual(str(self.arr), "[2, 1]")

    def test_remove_not_found(self):
        self.arr.append(1)
        with self.assertRaises(ValueError):
            self.arr.remove(2)

    # --------------------
    # Get / Set
    # --------------------
    def test_get_valid(self):
        self.arr.append(42)
        self.assertEqual(self.arr.get(0), 42)

    def test_get_out_of_range(self):
        with self.assertRaises(IndexError):
            self.arr.get(0)

    def test_set_valid(self):
        self.arr.append(1)
        self.arr[0] = 99
        self.assertEqual(self.arr[0], 99)

    def test_set_out_of_range(self):
        with self.assertRaises(IndexError):
            self.arr.set(1, 100)

    # --------------------
    # Contains & Index Of
    # --------------------
    def test_contains_and_in_operator(self):
        self.arr.append(10)
        self.arr.append(20)
        self.assertTrue(self.arr.contains(10))
        self.assertTrue(20 in self.arr)
        self.assertFalse(30 in self.arr)

    def test_index_of_found(self):
        self.arr.append(7)
        self.arr.append(8)
        self.assertEqual(self.arr.index_of(8), 1)

    def test_index_of_not_found(self):
        self.arr.append(1)
        with self.assertRaises(ValueError):
            self.arr.index_of(9)

    # --------------------
    # String Representation
    # --------------------
    def test_str_empty(self):
        self.assertEqual(str(self.arr), "[]")

    def test_str_nonempty(self):
        self.arr.append(1)
        self.arr.append(2)
        self.assertEqual(str(self.arr), "[1, 2]")

    # --------------------
    # Stress Test
    # --------------------
    def test_large_append(self):
        for i in range(1000):
            self.arr.append(i)
        self.assertEqual(len(self.arr), 1000)
        self.assertEqual(self.arr[0], 0)
        self.assertEqual(self.arr[999], 999)

    def test_reverse(self):
        arr = MyList()
        arr.extend([1, 2, 3, 4, 5])

        arr.reverse()

        # Check that the elements are reversed
        self.assertEqual(arr[0], 5)
        self.assertEqual(arr[1], 4)
        self.assertEqual(arr[2], 3)
        self.assertEqual(arr[3], 2)
        self.assertEqual(arr[4], 1)

        # Check that the length is unchanged
        self.assertEqual(len(arr), 5)

    def test_copy(self):
        arr = MyList()
        arr.extend([1, 2, 3, 4, 5])

        copied_arr = arr.copy()

        # Check that the elements are the same
        for i in range(len(arr)):
            self.assertEqual(arr[i], copied_arr[i])

        # Check that modifying the copy does not affect the original container
        copied_arr.append(6)
        self.assertEqual(len(copied_arr), 6)
        self.assertEqual(len(arr), 5)

        # Check that it is a shallow copy (same object references)
        self.assertIs(arr[0], copied_arr[0])

    def test_count(self):
        arr = MyList()
        arr.extend([1, 2, 3, 2, 4, 2, 5])

        # Count occurrences of 2
        self.assertEqual(arr.count(2), 3)

        # Count occurrences of 1
        self.assertEqual(arr.count(1), 1)

        # Count occurrences of a value not in the array
        self.assertEqual(arr.count(99), 0)

        # Count in an empty array
        empty_arr = MyList()
        self.assertEqual(empty_arr.count(1), 0)

    def test_slice(self):
        arr = MyList()
        arr.extend([1, 2, 3, 4, 5])

        # Slice from index 1 to 4 (should include 1,2,3,4? check Python behavior)
        sliced_arr = arr.slice(1, 4)

        # Check that the sliced elements are correct
        self.assertEqual(len(sliced_arr), 4)
        self.assertEqual(sliced_arr[0], 2)
        self.assertEqual(sliced_arr[1], 3)
        self.assertEqual(sliced_arr[2], 4)

        # Ensure original array is unchanged
        self.assertEqual(len(arr), 5)
        self.assertEqual(arr[0], 1)
        self.assertEqual(arr[4], 5)

        # Test slicing with end=None (should go to the end)
        sliced_arr2 = arr.slice(2)
        self.assertEqual(len(sliced_arr2), 3)
        self.assertEqual(sliced_arr2[0], 3)
        self.assertEqual(sliced_arr2[2], 5)

        # Test slicing entire array
        full_slice = arr.slice()
        self.assertEqual(len(full_slice), 5)
        self.assertEqual(full_slice[0], 1)
        self.assertEqual(full_slice[4], 5)

    def test_iter(self):
        arr = MyList()
        arr.extend([10, 20, 30, 40, 50])

        # Collect elements using a for loop
        collected = []
        for val in arr:
            collected.append(val)

        # Check that all elements are returned in correct order
        self.assertEqual(collected, [10, 20, 30, 40, 50])

        # Check that the iterator works with built-in functions
        self.assertEqual(sum(arr), 150)  # 10+20+30+40+50
        self.assertTrue(20 in arr)
        self.assertFalse(99 in arr)

        # Check iteration on empty list
        empty_arr = MyList()
        collected_empty = [x for x in empty_arr]
        self.assertEqual(collected_empty, [])


if __name__ == "__main__":
    unittest.main()
