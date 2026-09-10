from Package import Package

class HashMap:
    def __init__(self):
        self.size = 10
        self.map = [None] * self.size
        self.length = 0

        # assigning package_list items to hash table
        hash_list = [
            [], [], [], [], [], [], [], [], [], []
        ]

    def hash_function(self, item):
        return item % self.size

    # def add(self, value):
    #     index = hash_function(value)
    #     bucket = hash_list[index]
    #     if value not in bucket:
    #         bucket.append(value)

    def add(self, key, val):
        index = self.hash_function(key)
        value = [key, val]

        # If the key doesn't exist in the map yet, add it
        if self.map[index] is None:
            self.map[index] = [[key, val]]
            self.length += 1
            return True

        for pair in self.map[index]:
            # overwrite value if key is same
            if pair[0] == key:
                pair[1] = value
                return True
            # otherwise append to list
        self.map[index].append(value)
        self.length += 1
        return True

    ## FIX ALL BELOW, not using "hash_list" anymore, using self.map which is a list
    def contains(self, value):
        index = self.hash_function(value)
        bucket = self.map[index]
        for drop in bucket:
            if value == Package.get_id(drop):
                return True
            else:
                return False
        return None

    def delete(self, value):
        index = self.hash_function(value)
        bucket = self.map[index]
        for drop in bucket:
            if value == Package.get_id(drop):
                bucket.pop(drop)

    # def hash_packages(self, package_list):
    #     for package in package_list:
    #         self.add(package)

    def print_value(self, key):
        index = self.hash_function(key)
        bucket = self.map[index]
        for drop in bucket:
            if key == Package.get_id(drop):
                Package.print_info(drop)


    ## print hash list for testing
    # def print_hash_table():
    #     for bucket in self.map:
    #         for item in bucket:
    #             print(item)
    #             Package.print_info(item)

    #
    # hash_packages(package_list)
    #
    # # print out single pkg info by ID
    # print("INFO FOR SINGLE PKG TESTING")
    # item_id = 22
    # hash_id = hash_function(item_id)
    # print(item_id)
    #
    # # pkg.Package.print_info_by_id(hash_list[hash_id[item_id]], item_id)
    #
    #
    #
    # print_hash_table()
