import csv
import packageObject as pkg

package_list = []

def get_package_info(package_file_path):
    with open(package_file_path) as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')

        for line in reader:
            package_id, address, city, state, zipcode, deadline, weight, status = line
            package_list.append(pkg.Package(package_id, address, city, state, zipcode, deadline, weight, status))

#pkg.Package.print_info(package_list[22])

# populate list of packages from source CSV file
get_package_info("WGUPS-package-file.csv")

# print for testing purposes
for item in package_list:
    pkg.Package.print_info(item)


###################################################################################################
# right now I have a list of Objects, which I need to assign to a hash table
###################

# TESTING A HASH TABLE IMPLEMENTATION
hash_list = [
    [],[],[],[],[],[],[],[],[],[]
]

def hash_function(item):
    return item % 10

# we need to grab the ID, hash that value, and store the entire piece of data into the "bucket"
def add_hash(package, hash_list):
    index = hash_function(int(package.get_id()))
    #print(index)
    hash_list[index].append(package)
    #return index

# hash each package in list by id
for package in package_list:
    add_hash(package, hash_list)

# print hash list for testing
for bucket in hash_list:
    for item in bucket:
        pkg.Package.print_info(item)
