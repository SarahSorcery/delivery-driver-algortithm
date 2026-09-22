# Sam Merrill ID #

# useful infor for late:     
    # start_time = 8:00 am
    # AVAILABLE_DRIVERS = 2
    # AVAILABLE_TRUCKS = 3

from HashMap import HashMap
from queue import Queue

class Truck:
    def __init__(self, id):
        self.id = id
        self.MAX_PKGS = 16
        self.AVG_MPH = 18
        self.packages = HashMap()
        #
        self.delivery_route = Queue()
        self.pkg_count = 0


    # returns ID & remaining packages as an f-string
    # Time Complexity is O(1)
    # Space Complexity is O(1)
    def __str__(self):
        return f"Truck #{self.id} currently has {self.pkg_count} remaining packages."

    # returns a list of packages
    # Time Complexity is O(1)
    # Space Complexity is O(1)
    def get_packages(self):
        return self.packages

    # adds a package to Truck
    # Time Complexity is O(3) --> O(1)
     # Space Complexity is O(1)
    def add_package(self, package):
        if package is None:
            print(f"[DEBUG ALERT] Truck #{self.id} was handed a 'None' package! Skipping to prevent crash.")
            return
        self.packages.add(package.id, package) # add package to HashMap --> O(1)
        ### ADD TO NODE LIST
        self.pkg_count += 1

    # removes a package from Truck
    # Time Complexity is O(3) --> O(1)
    # Space Complexity is O(1)
    def remove_package(self, package):
        self.packages.delete(package.id, package) # remove package to HashMap --> O(1)
        ### ADD TO NODE LIST
        self.pkg_count -= 1 # decrement

