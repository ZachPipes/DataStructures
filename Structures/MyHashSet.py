def _hash(key):
    """
    Compute and return the hash index for the given key.
    """
    return hash(key)


class MyHashSet:
    def __init__(self, initial_capacity=16):
        """
        Initialize the hash set with an optional initial capacity.
        """
        self.capacity = initial_capacity
        self.buckets = [[] for i in range(initial_capacity)]
        self.size = 0

    def add(self, key):
        """
        Add a key to the set. If it already exists, do nothing.
        """
        index = _hash(key) % self.capacity
        bucket = self.buckets[index]

        for k in bucket:
            if k == key:
                return

        bucket.append(key)
        self.size += 1

    def remove(self, key):
        """
        Remove a key from the set. If it does not exist, do nothing.
        """
        index = _hash(key) % self.capacity
        bucket = self.buckets[index]

        for i, k in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.size -= 1
                return

    def contains(self, key):
        """
        Check if the set contains the given key. Return True or False.
        """
        index = _hash(key) % self.capacity
        bucket = self.buckets[index]

        for k in bucket:
            if k == key:
                return True
        return False

    def __len__(self):
        """
        Return the number of elements in the set.
        """
        return self.size

    def __str__(self):
        """
        Return a human-readable string representation of the set.
        """
        return '{' + ','.join(str(k) for bucket in self.buckets for k in bucket) + '}'
