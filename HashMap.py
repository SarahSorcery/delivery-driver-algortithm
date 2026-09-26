# Sam Merrill ID: 012638734
from Package import Package

class HashMap:
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def __init__(self):
        self.size = 10
        self.map = [None] * self.size
        self.length = 0

    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def hash_function(self, item):
        return int(item) % self.size

    # Time Complexity: O(1) avg (O(n) worst case)
    # Space Complexity: O(1)
    def add(self, key, val):
        index = self.hash_function(key)
        value = [key, val]

        # If the key doesn't exist in the map yet, add it
        if self.map[index] is None:
            self.map[index] = [value]
            self.length += 1
            return True

        for pair in self.map[index]:
            # overwrite value if key is same
            if pair[0] == key:
                pair[1] = val
                return True
            # otherwise append to bucket list
        self.map[index].append(value)
        self.length += 1
        return True

    # Time Complexity: O(1) avg (O(n) worst case)
    # Space Complexity: O(1)    
    def get(self, key):
        index = self.hash_function(key)
        if self.map[index] is not None:
            for pair in self.map[index]:
                if pair[0] == key:
                    return pair[1]
        # return None if key value pair doesn't exist
        return None

    # Time Complexity: O(1) avg (O(n) worst case)
    # Space Complexity: O(1)
    def delete(self, value):
        index = self.hash_function(value)
        bucket = self.map[index]
        for drop in bucket:
            if value == Package.get_id(drop):
                bucket.remove(drop)
                self.length -= 1
                return True


    # Time Complexity: O(1) avg (O(n) worst case)
    # Space Complexity: O(1)
    def print_value(self, key):
        index = self.hash_function(key)
        bucket = self.map[index]
        for drop in bucket:
            if key == Package.get_id(drop):
                Package.print_info(drop)
