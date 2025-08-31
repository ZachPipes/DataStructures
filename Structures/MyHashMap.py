def _hash(key):
    return hash(key)

class MyHashMap:
    def __init__(self, initial_capacity=16):
        self.capacity = initial_capacity
        self.buckets = [[] for i in range(initial_capacity)]
        self.size = 0

    def put(self, key, value):
        """
        Insert or update the key-value pair in the hash map.
        If the key already exists, update its value.
        """
        index = _hash(key) % self.capacity
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))
        # Increasing size variable to match new bucket size
        self.size += 1

    def get(self, key):
        """
        Retrieve the value associated with the given key.
        Return None (or raise an error) if the key is not found.
        """
        index = _hash(key) % self.capacity
        bucket = self.buckets[index]

        for k, v in bucket:
            if k == key:
                return v

        return None

    def remove(self, key):
        """
        Remove the key-value pair associated with the given key.
        If the key does not exist, do nothing or handle the case gracefully.
        """
        index = _hash(key) % self.capacity
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.size -= 1

    def contains_key(self, key):
        """
        Check if the given key exists in the hash map.
        Return True if found, otherwise False.
        """
        index = _hash(key) % self.capacity
        bucket = self.buckets[index]

        for k, v in bucket:
            if k == key:
                return True

        return False

    def keys(self):
        """
        Return a collection (e.g., list) of all keys in the hash map.
        """
        keys = []

        for bucket in self.buckets:
            for k, v in bucket:
                keys.append(k)

        return keys

    def values(self):
        """
        Return a collection (e.g., list) of all values in the hash map.
        """
        values = []

        for bucket in self.buckets:
            for k, v in bucket:
                values.append(v)

        return values

    def __len__(self):
        """
        Return the number of key-value pairs stored in the hash map.
        """
        return self.size

    def __str__(self):
        """
        Return a human-readable string representation of the hash map.
        """
        items = []

        for bucket in self.buckets:
            for k, v in bucket:
                stringbuilder = f"'{k}': "
                stringbuilder += str(v)
                items.append(stringbuilder)

        return '{' + ','.join(items) + '}'