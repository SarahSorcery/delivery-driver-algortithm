import csv
from asyncio.windows_events import NULL

import packageObject as pkg
Pack = pkg.Package


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
# for item in package_list:
#     Pack.print_info(item)


###################################################################################################
# right now I have a list of Objects, which I need to assign to a hash table
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
for package in package_list:
    add_hash(package, hash_list)
    #add(int(package.get_id()))



#print out single pkg info by ID
print("INFO FOR SINGLE PKG TESTING")
item_id = 22
hash_id = hash_function(item_id)
print(item_id)
#pkg.Package.print_info_by_id(hash_list[hash_id[item_id]], item_id)


# # print hash list for testing
for bucket in hash_list:
    for item in bucket:
        print(item)
        Pack.print_info(item)

###################################################################################################
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

distance_table = []

def get_distance_info(distance_file_path):
    with open(distance_file_path) as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')

        for line in reader:
            address_distance = []
            for data in line:
                address_distance.append(data)
            distance_table.append(address_distance)




get_distance_info("WGUPS-distance-table.csv")
#
# for location in distance_table:
#     for distance in location:
#         print(distance)
#     print("********************************")
location_distance_values = []
for location in distance_table:
    distance_values = location[1:] # take only number values after addresses
    location_distance_values.append(distance_values) # this is more efficient than a 2d for loop, which I initially had here, which created a list of values from location 2-end, but this is way better


for i in location_distance_values:
    print(i)
    print("********************************")



################################

# selected_id = input("Enter which package ID: " )


# enter an ID and search the HASH LIST for the package




### TO DOS
    # [ ] assign route lists
            #  group by status constraints? : below, make into function if needed

for bucket in hash_list:
    for package in bucket:
        if Pack.get_status(package) != "":
            print(Pack.get_id(package))
            print(Pack.get_status(package))




## this was working i thought, now it 's not
# print(contains(27))