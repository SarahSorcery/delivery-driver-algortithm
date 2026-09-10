import csv
import Package as pkg
Pack = pkg.Package

def get_package_info(package_file_path):
    loading_list = []
    with open(package_file_path) as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')

        for line in reader:
            package_id, address, city, state, zipcode, deadline, weight, status = line
            loading_list.append(pkg.Package(package_id, address, city, state, zipcode, deadline, weight, status))
    return loading_list

# populate list of packages from source CSV file
package_list = get_package_info("WGUPS-package-file.csv")

###################################################################################################
# assigning package_list items to hash table
###################

# TESTING A HASH TABLE IMPLEMENTATION
hash_list = [
    [],[],[],[],[],[],[],[],[],[]
]

def hash_function(item):
    return item % 10

def add(value):
    index = hash_function(value)
    bucket = hash_list[index]
    if value not in bucket:
        bucket.append(value)

def add_hash(package, hash_list):
    index = hash_function(int(package.get_id()))
    bucket = hash_list[index]
    if package not in bucket:
        bucket.append(package)
    #return index

## Keep syntax, it works
def contains(value):
    index = hash_function(value)
    bucket = hash_list[index]
    for drop in bucket:
        if value == Pack.get_id(drop):
            return True
        else:
            return False
    return None


# hash each package in list by id
# for package in package_list:
#     add_hash(package, hash_list)
#     #add(int(package.get_id()))

def hash_packages(package_list):
    for package in package_list:
        add_hash(package, hash_list)

hash_packages(package_list)

#print out single pkg info by ID
print("INFO FOR SINGLE PKG TESTING")
item_id = 22
hash_id = hash_function(item_id)
print(item_id)
#pkg.Package.print_info_by_id(hash_list[hash_id[item_id]], item_id)


# # print hash list for testing
def print_hash_table():
    for bucket in hash_list:
        for item in bucket:
            print(item)
            Pack.print_info(item)

print_hash_table()

###################################################################################################
def get_distance_info(distance_file_path):
    distance_table = []
    with open(distance_file_path) as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for line in reader:
            address_distance = []
            for data in line:
                address_distance.append(data)
            distance_table.append(address_distance)
    return distance_table

package_distance_table = get_distance_info("WGUPS-distance-table.csv")
###################################################################################################
location_distance_values = []
for location in package_distance_table:
    distance_values = location[1:] # take only number values after addresses
    location_distance_values.append(distance_values) # this is more efficient than a 2d for loop, which I initially had here, which created a list of values from location 2-end, but this is way better

for i in location_distance_values:
    print(i)
    print("********************************")

###################################################################################################
def print_statuses():
    for bucket in hash_list:
        for package in bucket:
            if Pack.get_status(package) != "":
                print(str(Pack.get_id(package)) + "  |  " + Pack.get_status(package))
print_statuses()
###################################################################################################

# selected_id = input("Enter which package ID: " )

# enter an ID and search the HASH LIST for the package

### TO DOS
    # [ ] assign route lists
            #  group by status constraints? : below, make into function if needed


## this was working i thought, now it 's not
# print(contains(27))

# ****** excess old code from above: ******
# we need to grab the ID, hash that value, and store the entire piece of data into the "bucket"
# def add_hash(package, hash_list):
#     index = hash_function(int(package.get_id()))
#     hash_list[index].append(package)
#     #return index
# def remove_hash(package, hash_list):
#     index = hash_function(int(package.get_id()))
#     hash_list[index].remove(package)
#
# def update_hash(package, hash_list):
#     index = hash_function(int(package.get_id()))
#     hash_list[index].append(package)
