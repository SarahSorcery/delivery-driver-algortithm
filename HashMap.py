from Package import Package

class HashMap:
    def __init__(self):
        self.size = 10
        self.map = [] * self.size
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
            if self.map[hash] is None:
                self.map[hash] = list([value])
                self.length += 1
            else:
                for pair in self.map[index]:
                    # overwrite value if key is same
                    if pair[0] == key:
                        pair[1] = value
                        return True
                    # otherwise append to list
                    self.map[index].append(value)
                    self.length += 1
                    return True


        ## Keep syntax??
        def contains(value):
            index = hash_function(value)
            bucket = hash_list[index]
            for drop in bucket:
                if value == Package.get_id(drop):
                    return True
                else:
                    return False
            return None

        def delete(value):
            index = hash_function(value)
            bucket = hash_list[index]
            for drop in bucket:
                if value == Package.get_id(drop):
                    bucket.pop(drop)

        def hash_packages(package_list):
            for package in package_list:
                add(package)

        def print_value(key):
            index = hash_function(key)
            bucket = hash_list[index]
            for drop in bucket:
                if key == Package.get_id(drop):
                    print(drop)

        ## print hash list for testing
        def print_hash_table():
            for bucket in hash_list:
                for item in bucket:
                    print(item)
                    Package.print_info(item)




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