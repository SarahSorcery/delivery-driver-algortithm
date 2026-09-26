# Sam Merrill ID: 012638734
import csv
from HashMap import HashMap
from Package import Package

class PackageReader:
    def __init__(self):
        self.package_hash_table = HashMap()
        self.MAX_PKGS = 40
        self.packages = {}
        self.build_package_table()

    def __len__(self):
        return len(self.packages)

    def insert(self, package):
        self.packages[package.id] = package

    # builds package hash table/map from data in each row of a csv file
    # Time Complexity: O(n)     n = # of packages
    # Space Complexity: O(n)
    def build_package_table(self):
        with open("WGUPS-package-file.csv") as csvfile:
             reader = csv.reader(csvfile, delimiter=',', quotechar='"')
             for line in reader:
                package_id, address, city, state, zipcode, deadline, weight, status = line
                current_package = Package(package_id, address, city, state, zipcode, deadline, weight, status)
                # insert package into packages set O(1)
                self.insert(current_package)
                # add to hashMap O(1)
                self.package_hash_table.add(package_id, current_package)

    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def get_package_by_id(self, id):
        return self.package_hash_table.get(id) # uses hashmap's get() to get id

# ###################################################################################################