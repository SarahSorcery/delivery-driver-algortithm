# Sam Merrill ID: 012638734
from HashMap import HashMap

class Truck:
    # constructor
    def __init__(self, id):
        self.id = id
        self.package_list = []
        self.pkg_count = 0

    # returns ID & remaining packages as an f-string
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def __str__(self):
        return f"Truck #{self.id} currently has {self.pkg_count} remaining packages."

    # returns a list of packages
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def get_package_list(self):
        return self.package_list

    # adds a package to Truck
    # Time Complexity: O(3) --> O(1)
    # Space Complexity: O(1)
    def add_package(self, package):
        if package is None:
            print(f"#{self.id}: 'None' package was detected. Skipping over id.")
            return
        self.package_list.append(package) # add to list
        self.pkg_count += 1

    # removes a package from Truck
    # Time Complexity: O(3) --> O(1)
    # Space Complexity: O(1)
    def remove_package(self, package):
        self.package_list.remove(package) # remove from list
        self.pkg_count -= 1 # decrement

