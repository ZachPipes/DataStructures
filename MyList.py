class MyList:
    def __init__(self, capacity=10):
        """Initialize the array with optional capacity"""
        self.data = [None] * capacity # Internal storage
        self.capacity = capacity      # Maximum allocated space
        self.length = 0               # Current # of elements

    def append(self, value):
        """Add value to the end of the array"""
        # Edge Cases
        if self.length == self.capacity:      # Doubling the capacity if maxed out
            self.double_capacity()

        self.data[self.length] = value        # Append new element
        self.length += 1                      # Increase length by 1

    def extend(self, values):
        """Add a list of values to the end of the array"""
        for i in range(len(values)):
            self.append(values[i])

    def insert(self, index, value):
        """Insert value at a specific index"""
        # Edge Cases
        if index > self.length:                # If the index is out of bounds
            raise IndexError
        if self.length == self.capacity:        # Doubling the capacity if maxed out
            self.double_capacity()

        for i in range(self.length, index, -1): # Shifting elements one to the right
            self.data[i] = self.data[i-1]

        self.data[index] = value                # Append new element
        self.length += 1                        # Increase length by 1

    def remove(self, value):
        """Remove first occurrence of value"""
        for i in range(len(self)):                  # Iterate through each element
            if self.data[i] == value:               # Is the element the value to remove?
                for j in range(i, self.length - 1):  # Iterate through each element after the ith value
                    self.data[j] = self.data[j + 1] # Replace the jth element with the next
                self.data[self.length - 1] = None   # Delete the ith element
                self.length -= 1                    # Reduce array size by 1
                return
        raise ValueError("remove: value not present in array")

    def pop(self, index=None):
        """Remove and return the last element or element at index"""
        # Edge Cases
        if self.length == 0:
            raise IndexError("Pop: from empty array")

        if index is None:
            index = self.length - 1
        elif index < 0 or index >= self.length:
            raise IndexError("Pop: index out of range")

        if index == self.length - 1:
            popped = self.data[index]
            self.data[index] = None
            self.length -= 1
            return popped

        popped = self.data[index] # Get value to be popped

        for i in range(index, self.length - 1): # Shift all elements left
            self.data[i] = self.data[i+1]

        self.data[self.length - 1] = None # Delete the last element
        self.length -= 1        # Reduce array size by 1
        return popped

    def clear(self):
        """Clear the entire array"""
        for i in range(self.length - 1):
            self.data[i] = None
        self.length = 0

    def get(self, index):
        """Return element at index"""
        if index >= self.length:
            raise IndexError("Get: index out of range")
        #TODO: Make option to start at end of array
        return self.data[index]

    def set(self, index, value):
        """Set element at index to value"""
        if index < 0 or index >= self.length:
            raise IndexError("Set: index out of range")
        self.data[index] = value

    def contains(self, value):
        """Return True if value is in array"""
        for i in range(len(self)):
            if self.data[i] == value:
                return True
        return False

    def index_of(self, value):
        """Return index of first occurrence of value, -1 if not found"""
        for i in range(len(self)):
            if self.data[i] == value:
                return i

        raise ValueError("index_of: Value not present in array")

    def double_capacity(self):
        """Double the capacity of the array"""

        self.capacity *= 2                # Doubling max allocated space
        new_data = [None] * self.capacity # Create a new space for the extended array to live, with doubled space
        new_data[:self.length] = self.data[:self.length]
        self.data = new_data              # Assign old space to be new space

    def reverse(self):
        """Reverse the array in-place"""
        beg = 0
        end = self.length - 1
        while beg < end:
            self.data[beg], self.data[end] = self.data[end], self.data[beg]
            beg += 1
            end -= 1

    def copy(self):
        """Return a shallow copy of the array"""
        new_list = MyList(self.capacity)
        for i in range(self.length):
            new_list.append(self.data[i])
        return new_list

    def count(self, value):
        """Return the number of occurrences of value"""
        counter = 0
        for i in range(self.length):
            if self.data[i] == value:
                counter += 1
        return counter

    def slice(self, start=0, end=None):
        """Return a slice of the array as a new MyList"""
        if start < 0:
            raise IndexError("slice: start must be >= 0")
        if end is not None and end > self.length:
            raise IndexError("slice: end must be <= length")
        else:
            end = self.length

        sliced = MyList(end - start)
        for i in range(start, end):
            sliced.append(self.data[i])

        return sliced

    def __iter__(self):
        """Make the array iterable"""
        return MyListIterator(self)

    def __str__(self):
        """Return string representation of the array"""
        output = "["
        for i in range(self.length):
            output += str(self.data[i])
            if i != self.length - 1:
                output += ", "
        output += "]"
        return output

    def __getitem__(self, index):
        """Enable array[index] syntax"""
        return self.get(index)

    def __setitem__(self, index, value):
        """Enable array[index] = value syntax"""
        return self.set(index, value)

    def __len__(self):
        """Enable len(array)"""
        return self.length

    def __contains__(self, value):
        return self.contains(value)


class MyListIterator:
    def __init__(self, mylist):
        self._list = mylist
        self._index = 0

    def __next__(self):
        if self._index < self._list.length:
            value = self._list.data[self._index]
            self._index += 1
            return value
        else:
            raise StopIteration

    def __iter__(self):
        return self