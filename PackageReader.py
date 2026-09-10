## TO DOS:
#   so I need to overhaul this. I need to sort out the
#   CSV data READER,
#   HashMap,
#   Package,
#   Truck,
# and I'm not sure what else right now. I'm having a hard time with readability and I need to clean things up
#
#
import csv
from HashMap import HashMap
from Package import Package


class PackageReader:
    def __init__(self):
        self.package_hash_table = HashMap()
        self.MAX_PKGS = 40
        self.packages = {}
        self.build_package_table()

    def insert(self, package):
        self.packages[package.id] = package

    def build_package_table(self):
        with open("WGUPS-package-file.csv") as csvfile:
             reader = csv.reader(csvfile, delimiter=',', quotechar='"')
             for line in reader:
                 package_id, address, city, state, zipcode, deadline, weight, status = line
                 package = Package(package_id, address, city, state, zipcode, deadline, weight, status)
                # insert package into packages set
                self.insert(package)
                # add to hashMap
                self.package_hash_table.add(package_id)



## officially overwhelmed myself, taking a break. So far I think I got a somewhat better functioning hashmap/table
## I'm not sure what I need to do exactly. successfully read package info into the hash again. Then actually lookup single values to print
## then read in distance table/ adjacency matrix for further use in shortest path.

# ###################################################################################################
# def get_package_info(package_file_path):
#     loading_list = []
#     with open(package_file_path) as csvfile:
#         reader = csv.reader(csvfile, delimiter=',', quotechar='"')
#         for line in reader:
#             package_id, address, city, state, zipcode, deadline, weight, status = line
#             loading_list.append(Package(package_id, address, city, state, zipcode, deadline, weight, status))
#     return loading_list
#
# # populate list of packages from source CSV file
# package_list = get_package_info("WGUPS-package-file.csv")
#
# ###################################################################################################
# ###################################################################################################
# def get_distance_info(distance_file_path):
#     distance_table = []
#     with open(distance_file_path) as csvfile:
#         reader = csv.reader(csvfile, delimiter=',', quotechar='"')
#         for line in reader:
#             address_distance = []
#             for data in line:
#                 address_distance.append(data)
#             distance_table.append(address_distance)
#     return distance_table
#
# package_distance_table = get_distance_info("WGUPS-distance-table.csv")
# ###################################################################################################
# location_distance_values = []
# for location in package_distance_table:
#     distance_values = location[1:] # take only number values after addresses
#     location_distance_values.append(distance_values) # this is more efficient than a 2d for loop, which I initially had here, which created a list of values from location 2-end, but this is way better
#
# for i in location_distance_values:
#     print(i)
#     print("********************************")
#
# ###################################################################################################